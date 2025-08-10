"""
Churn Rate Calculator for Energy and Gas Companies

This script calculates the churn rate for a company that sells
electricity and gas, based on customer data provided in a CSV file.

The churn rate is calculated using the formula:
Churn Rate = (Number of Customers Lost in Period / 
             Average Number of Customers in Period) * 100

For this initial version, we will:
- Read customer data from a CSV file.
- Assume the data contains at least 'customer_id' and 'status' columns.
- Define 'churned' customers as those with status 'churned'.
- Calculate the churn rate for a given period.
"""

import pandas as pd


def calculate_churn_rate(csv_file_path):
    """
    Calculates the churn rate based on customer data in a CSV file.

    :param csv_file_path: Path to the CSV file containing customer data.
    :return: Churn rate as a percentage.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Validate required columns
        required_columns = ['customer_id', 'status']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"CSV file must contain columns: {required_columns}")
        
        # Count total customers
        total_customers = len(df)
        
        # Count churned customers
        churned_customers = len(df[df['status'].str.lower() == 'churned'])
        
        # Calculate churn rate
        if total_customers == 0:
            return 0.0
        
        churn_rate = (churned_customers / total_customers) * 100
        return churn_rate
    
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None


def main():
    """
    Main function to run the churn rate calculator.
    """
    print("Churn Rate Calculator for Energy and Gas Companies")
    print("--------------------------------------------------")
    
    # Get CSV file path from user
    csv_file_path = input("Enter the path to your customer data CSV file: ").strip()
    
    # Calculate churn rate
    churn_rate = calculate_churn_rate(csv_file_path)
    
    if churn_rate is not None:
        print(f"\nChurn Rate: {churn_rate:.2f}%")


if __name__ == "__main__":
    main()