import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class ChurnCalculator:
    def __init__(self, data_file):
        """
        Initialize the Churn Calculator with customer data.
        
        :param data_file: Path to the CSV file containing customer data
        """
        self.data_file = data_file
        self.df = None
        self.model = None
        self.label_encoders = {}
        self.load_data()
    
    def load_data(self):
        """Load customer data from CSV file."""
        try:
            self.df = pd.read_csv(self.data_file)
            print(f"Successfully loaded data with {len(self.df)} customers")
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def calculate_period_churn_rate(self, start_date, end_date):
        """
        Calculate churn rate for a specific period.
        
        :param start_date: Start date of the period (YYYY-MM-DD)
        :param end_date: End date of the period (YYYY-MM-DD)
        :return: Churn rate for the period
        """
        # Convert string dates to datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        # Customers at the start of the period
        customers_at_start = self.df[
            (pd.to_datetime(self.df['contract_start_date']) <= start_date) &
            (self.df['contract_end_date'].isna() | (pd.to_datetime(self.df['contract_end_date']) > start_date))
        ]
        
        # Customers at the end of the period
        customers_at_end = self.df[
            (pd.to_datetime(self.df['contract_start_date']) <= end_date) &
            (self.df['contract_end_date'].isna() | (pd.to_datetime(self.df['contract_end_date']) > end_date))
        ]
        
        # Customers who churned during the period
        churned_customers = self.df[
            (pd.to_datetime(self.df['contract_end_date']) > start_date) &
            (pd.to_datetime(self.df['contract_end_date']) <= end_date)
        ]
        
        # Calculate churn rate
        if len(customers_at_start) > 0:
            churn_rate = (len(churned_customers) / len(customers_at_start)) * 100
            return {
                'period': f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
                'customers_at_start': len(customers_at_start),
                'customers_at_end': len(customers_at_end),
                'churned_customers': len(churned_customers),
                'churn_rate': round(churn_rate, 2)
            }
        else:
            return {
                'period': f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
                'customers_at_start': 0,
                'customers_at_end': 0,
                'churned_customers': 0,
                'churn_rate': 0.0
            }
    
    def calculate_monthly_churn_rates(self, year):
        """
        Calculate monthly churn rates for a specific year.
        
        :param year: Year for which to calculate monthly churn rates
        :return: DataFrame with monthly churn rates
        """
        monthly_rates = []
        
        for month in range(1, 13):
            # Calculate start and end dates for the month
            start_date = f"{year}-{month:02d}-01"
            
            # Calculate end date of the month
            if month == 12:
                end_date = f"{year+1}-01-01"
            else:
                end_date = f"{year}-{month+1:02d}-01"
            
            # Calculate churn rate for the month
            result = self.calculate_period_churn_rate(start_date, end_date)
            result['month'] = month
            monthly_rates.append(result)
        
        return pd.DataFrame(monthly_rates)
    
    def calculate_quarterly_churn_rates(self, year):
        """
        Calculate quarterly churn rates for a specific year.
        
        :param year: Year for which to calculate quarterly churn rates
        :return: DataFrame with quarterly churn rates
        """
        quarterly_rates = []
        quarters = [(1, 3), (4, 6), (7, 9), (10, 12)]
        
        for i, (start_month, end_month) in enumerate(quarters, 1):
            # Calculate start and end dates for the quarter
            start_date = f"{year}-{start_month:02d}-01"
            
            # Calculate end date of the quarter
            if end_month == 12:
                end_date = f"{year+1}-01-01"
            else:
                end_date = f"{year}-{end_month+1:02d}-01"
            
            # Calculate churn rate for the quarter
            result = self.calculate_period_churn_rate(start_date, end_date)
            result['quarter'] = i
            quarterly_rates.append(result)
        
        return pd.DataFrame(quarterly_rates)
    
    def prepare_ml_data(self):
        """Prepare data for machine learning model."""
        # Create a copy of the dataframe for ML
        ml_df = self.df.copy()
        
        # Create target variable (churned or not)
        # A customer is considered churned if they have an end date
        ml_df['churned'] = ~ml_df['contract_end_date'].isna()
        
        # Feature engineering
        # Calculate tenure in days
        ml_df['contract_start_date'] = pd.to_datetime(ml_df['contract_start_date'])
        ml_df['contract_end_date'] = pd.to_datetime(ml_df['contract_end_date'])
        
        # For active customers, use today's date as end date for tenure calculation
        ml_df['tenure_days'] = (
            ml_df['contract_end_date'].fillna(pd.to_datetime('today')) - 
            ml_df['contract_start_date']
        ).dt.days
        
        # Encode categorical variables
        categorical_columns = ['payment_method', 'service_type', 'contract_type']
        
        for col in categorical_columns:
            if col in ml_df.columns:
                le = LabelEncoder()
                ml_df[col + '_encoded'] = le.fit_transform(ml_df[col].astype(str))
                self.label_encoders[col] = le
        
        # Select features for the model
        feature_columns = [
            'monthly_charges', 'total_charges', 'tenure_months', 
            'tenure_days', 'payment_method_encoded', 'service_type_encoded', 
            'contract_type_encoded'
        ]
        
        # Remove any columns that don't exist in the dataframe
        feature_columns = [col for col in feature_columns if col in ml_df.columns]
        
        return ml_df, feature_columns
    
    def train_ml_model(self):
        """Train machine learning model to predict churn."""
        # Prepare data
        ml_df, feature_columns = self.prepare_ml_data()
        
        # Check if we have the required columns
        if 'churned' not in ml_df.columns:
            print("Error: 'churned' column not found in data")
            return
        
        # Prepare features and target
        X = ml_df[feature_columns]
        y = ml_df['churned']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train Random Forest model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Make predictions on test set
        y_pred = self.model.predict(X_test)
        
        # Print model performance
        print("\nMachine Learning Model Performance:")
        print("=" * 40)
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': feature_columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nFeature Importance:")
        print(feature_importance)
        
        return self.model
    
    def predict_churn(self):
        """Predict which customers are likely to churn."""
        if self.model is None:
            print("Model not trained yet. Please train the model first.")
            return None
        
        # Prepare data
        ml_df, feature_columns = self.prepare_ml_data()
        
        # Make predictions for all customers
        X = ml_df[feature_columns]
        predictions = self.model.predict_proba(X)[:, 1]  # Probability of churning
        
        # Add predictions to dataframe
        ml_df['churn_probability'] = predictions
        
        # Filter for customers with high probability of churning
        high_risk_customers = ml_df[ml_df['churn_probability'] > 0.5].sort_values(
            'churn_probability', ascending=False
        )
        
        # Exclude customers who have already churned (contract_end_date in the past)
        # Convert contract_end_date to datetime for comparison
        high_risk_customers = high_risk_customers.copy() # To avoid SettingWithCopyWarning
        high_risk_customers['contract_end_date'] = pd.to_datetime(high_risk_customers['contract_end_date'])
        
        # Filter out customers whose contract ended before today
        today = pd.to_datetime('today')
        future_risk_customers = high_risk_customers[
            (high_risk_customers['contract_end_date'].isna()) | 
            (high_risk_customers['contract_end_date'] > today)
        ]
        
        # Select and return relevant columns
        return future_risk_customers[['customer_id', 'churn_probability', 'contract_end_date']]
    
    def plot_churn_trends(self, year):
        """Plot monthly and quarterly churn trends."""
        # Calculate monthly churn rates
        monthly_df = self.calculate_monthly_churn_rates(year)
        
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot monthly churn rates
        ax1.plot(monthly_df['month'], monthly_df['churn_rate'], marker='o')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Churn Rate (%)')
        ax1.set_title(f'Monthly Churn Rates - {year}')
        ax1.set_xticks(range(1, 13))
        ax1.grid(True)
        
        # Calculate quarterly churn rates
        quarterly_df = self.calculate_quarterly_churn_rates(year)
        
        # Plot quarterly churn rates
        ax2.bar(quarterly_df['quarter'], quarterly_df['churn_rate'], 
                color=['skyblue', 'lightgreen', 'salmon', 'gold'])
        ax2.set_xlabel('Quarter')
        ax2.set_ylabel('Churn Rate (%)')
        ax2.set_title(f'Quarterly Churn Rates - {year}')
        ax2.set_xticks(quarterly_df['quarter'])
        ax2.grid(True, axis='y')
        
        plt.tight_layout()
        plt.show()
        
        return monthly_df, quarterly_df

def main():
    """Main function to run the churn calculator."""
    print("Churn Rate Calculator with Machine Learning")
    print("=" * 50)
    
    # Get CSV file path from command line arguments or user input
    import sys
    import datetime
    
    if len(sys.argv) > 1:
        csv_file_path = sys.argv[1]
    else:
        # Get CSV file path from user
        csv_file_path = input("Enter the path to your customer data CSV file: ").strip()
    
    # Initialize churn calculator
    calculator = ChurnCalculator(csv_file_path)
    
    if calculator.df is None:
        return
    
    # Get year for analysis from command line arguments or user input
    if len(sys.argv) > 2:
        try:
            year = int(sys.argv[2])
        except ValueError:
            print("Invalid year in command line argument. Using current year.")
            year = datetime.datetime.now().year
    else:
        try:
            year = int(input("Enter the year for analysis (e.g., 2023): "))
        except ValueError:
            print("Invalid year. Using current year.")
            year = datetime.datetime.now().year
    
    # Calculate and display monthly churn rates
    print(f"\nCalculating churn rates for {year}...")
    monthly_rates = calculator.calculate_monthly_churn_rates(year)
    print("\nMonthly Churn Rates:")
    print(monthly_rates[['month', 'customers_at_start', 'churned_customers', 'churn_rate']])
    
    # Calculate and display quarterly churn rates
    quarterly_rates = calculator.calculate_quarterly_churn_rates(year)
    print("\nQuarterly Churn Rates:")
    print(quarterly_rates[['quarter', 'customers_at_start', 'churned_customers', 'churn_rate']])
    
    # Train machine learning model
    print("\nTraining machine learning model...")
    calculator.train_ml_model()
    
    # Predict churn
    print("\nPredicting customers likely to churn...")
    high_risk_customers = calculator.predict_churn()
    
    if high_risk_customers is not None and not high_risk_customers.empty:
        print("\nCustomers with high probability of churning:")
        print(high_risk_customers.head(10))
    else:
        print("\nNo customers with high probability of churning found.")
    
    # Plot trends
    print("\nGenerating churn trend plots...")
    calculator.plot_churn_trends(year)

if __name__ == "__main__":
    main()