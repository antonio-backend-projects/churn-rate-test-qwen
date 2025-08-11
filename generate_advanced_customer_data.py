"""
Script per generare un dataset sintetico avanzato per il churn rate calculator.
Include una vasta gamma di caratteristiche predittive identificate.
"""

import csv
import random
from datetime import datetime, timedelta
import itertools

# --- Configurazione ---
NUM_RECORDS = 1000  # Numero di righe da generare
OUTPUT_FILE = "customer_data_advanced.csv"

# --- Liste di valori possibili per le colonne categoriche ---
NAMES = [
    "Marco", "Giulia", "Luca", "Sofia", "Alessandro", "Chiara", "Francesco", "Elena", "Matteo", "Valentina",
    "Andrea", "Alessia", "Simone", "Camilla", "Davide", "Federica", "Stefano", "Elisa", "Roberto", "Martina",
    "Paolo", "Silvia", "Marco", "Ilaria", "Luigi", "Gaia", "Giorgio", "Sara", "Antonio", "Arianna",
    "Fabio", "Nicole", "Daniele", "Veronica", "Angelo", "Michela", "Vincenzo", "Debora", "Salvatore", "Serena"
]

SURNAMES = [
    "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Gallo", "Costa", "Fontana", "Conti",
    "Ricci", "Bruno", "Moretti", "Marino", "Barbieri", "Lombardi", "Giordano", "Innocenti", "Colombo", "Mancini",
    "Longo", "Gentile", "Martinelli", "Marchetti", "Bianco", "Lombardo", "Coppola", "Ferrara", "Morelli", "Vitale",
    "Caruso", "De Luca", "Santoro", "Marini", "Benedetti", "Romano", "Sanna", "Fiore", "Bellini", "Basile"
]

PAYMENT_METHODS = ["Credit card", "Bank transfer", "Electronic check", "Mailed check"]
BILLING_METHODS = ["Paper", "Email", "Online Portal"]
SERVICE_TYPES = ["electricity", "gas", "both"]
CONTRACT_TYPES = ["month-to-month", "one year", "two year"]
CUSTOMER_TENURE_TYPES = ["Owner", "Tenant"]

# -----------------------

def generate_customer_data(num_records):
    """
    Genera una lista di dizionari rappresentanti i dati dei clienti.
    """
    data = []
    customer_id_counter = itertools.count(10001) # Inizia da 10001

    for _ in range(num_records):
        customer_id = next(customer_id_counter)
        name = f"{random.choice(NAMES)} {random.choice(SURNAMES)}"
        
        # Genera contract_start_date negli ultimi 5 anni
        start_date = datetime.now() - timedelta(days=random.randint(0, 365 * 5))
        contract_start_date = start_date.strftime("%Y-%m-%d")

        contract_type = random.choices(CONTRACT_TYPES, weights=[0.4, 0.35, 0.25])[0] # Più probabilità per month-to-month
        
        # Genera tenure_months coerente con contract_type
        if contract_type == "month-to-month":
            tenure_months = random.randint(1, 24)
        elif contract_type == "one year":
             # Un po' di flessibilità: 10-15 mesi per "one year"
            tenure_months = random.randint(10, 15) 
        else: # two year
            # Un po' di flessibilità: 20-28 mesi per "two year"
            tenure_months = random.randint(20, 28) 

        # Genera contract_end_date
        contract_end_date = ""
        # Se il contratto è scaduto (es. 30% di probabilità per month-to-month, 10% per gli altri)
        churn_flag = False
        if (contract_type == "month-to-month" and random.random() < 0.3) or \
           (contract_type != "month-to-month" and random.random() < 0.1):
            # Imposta una data di fine coerente con tenure_months
            end_date = start_date + timedelta(days=tenure_months * 30) # Approssimazione
            # Aggiungi un po' di variabilità alla data di fine
            end_date += timedelta(days=random.randint(-15, 15))
            contract_end_date = end_date.strftime("%Y-%m-%d")
            churn_flag = True

        service_type = random.choice(SERVICE_TYPES)
        payment_method = random.choice(PAYMENT_METHODS)
        billing_method = random.choice(BILLING_METHODS)
        customer_tenure_type = random.choice(CUSTOMER_TENURE_TYPES)
        
        # Genera monthly_charges
        base_monthly_charge = random.uniform(50.0, 120.0)
        # Per i clienti che abbandonano, potrebbe esserci un leggero calo nei costi nei mesi finali
        if churn_flag and random.random() < 0.4:
             monthly_charges = round(base_monthly_charge * random.uniform(0.8, 0.95), 1)
        else:
             monthly_charges = round(base_monthly_charge, 1)
        
        # Calcola total_charges (con un po' di variabilità)
        variability_factor = random.uniform(0.95, 1.05)
        total_charges = round(monthly_charges * tenure_months * variability_factor, 1)
        
        # --- Caratteristiche relative al consumo ---
        # avg_monthly_consumption_kwh: Consumo medio mensile in Kwh (simulato)
        if service_type == "electricity":
            avg_monthly_consumption_kwh = random.randint(200, 400)
        elif service_type == "gas":
            avg_monthly_consumption_kwh = random.randint(1000, 2000)
        else: # both
            avg_monthly_consumption_kwh = random.randint(1200, 2400)
            
        # consumption_volatility: Deviazione standard del consumo (simulata)
        # Clienti con alto supporto tendono ad avere più volatilità
        base_volatility = random.uniform(0.1, 0.3) # 10% - 30%
        if churn_flag:
            volatility = base_volatility * random.uniform(1.2, 2.0)
        else:
            volatility = base_volatility
        consumption_volatility = round(volatility, 4)
        
        # consumption_trend: Pendenza del consumo negli ultimi 6 mesi (simulata)
        # Trend negativo per clienti in procinto di churn
        if churn_flag and random.random() < 0.6:
            consumption_trend = round(random.uniform(-0.05, -0.01), 4) # -1% to -5% change per month
        else:
            consumption_trend = round(random.uniform(-0.01, 0.01), 4) # -1% to +1% change per month
            
        # consumption_vs_local_avg_ratio: Rispetto alla media locale (simulato)
        # Clienti con consumo molto basso rispetto alla media possono essere a rischio
        if churn_flag and random.random() < 0.4:
            consumption_vs_local_avg_ratio = round(random.uniform(0.5, 0.9), 2)
        else:
            consumption_vs_local_avg_ratio = round(random.uniform(0.9, 1.2), 2)
            
        # peak_hour_consumption_ratio: Percentuale in fascia F3/F2 (simulato)
        peak_hour_consumption_ratio = round(random.uniform(0.2, 0.5), 2)
        
        # smart_meter_flag: Ha un contatore intelligente?
        smart_meter_flag = random.choices([True, False], weights=[0.7, 0.3])[0]
        
        # --- Caratteristiche Contrattuali e di Fatturazione ---
        # has_promo: E' in una promo?
        has_promo = random.choices([True, False], weights=[0.3, 0.7])[0]
        
        # days_since_last_promo_end: Giorni dalla fine dell'ultima promo (se non in promo)
        if not has_promo:
            # Se non è in promo, ipotizziamo che l'ultima sia finita da 30 a 365 giorni
            days_since_last_promo_end = random.randint(30, 365)
        else:
            days_since_last_promo_end = 0 # O un valore speciale come -1?
            
        # num_price_changes_last_year
        num_price_changes_last_year = random.choices([0, 1, 2, 3], weights=[0.5, 0.3, 0.15, 0.05])[0]
        
        # last_bill_amount_vs_avg: Scostamento dell'ultima bolletta
        # Bollette molto alte possono causare churn
        if churn_flag and random.random() < 0.5:
            last_bill_amount_vs_avg = round(random.uniform(1.5, 3.0), 2) # Bolletta 1.5x - 3x la media
        else:
            last_bill_amount_vs_avg = round(random.uniform(0.8, 1.3), 2) # Bolletta 80% - 130% della media
            
        # num_late_payments e avg_days_late_payment
        if churn_flag:
            num_late_payments = random.randint(1, 5)
        else:
            num_late_payments = random.choices([0, 1, 2], weights=[0.8, 0.15, 0.05])[0]
            
        if num_late_payments > 0:
            avg_days_late_payment = random.randint(5, 30)
        else:
            avg_days_late_payment = 0
            
        # contract_renewal_reminder_sent: Per contratti a termine
        if contract_type != "month-to-month":
            contract_renewal_reminder_sent = random.choices([True, False], weights=[0.8, 0.2])[0]
        else:
            contract_renewal_reminder_sent = False # Non applicabile
            
        # days_to_contract_end: Giorni alla scadenza (solo per clienti attivi con contratto a termine)
        days_to_contract_end = ""
        if not churn_flag and contract_type != "month-to-month":
            # Tra 1 e 180 giorni
            days_to_contract_end = random.randint(1, 180)
            
        # --- Caratteristiche Comportamentali ---
        # has_online_account
        has_online_account = random.choices([True, False], weights=[0.6, 0.4])[0]
        
        # num_logins_last_month (solo se ha un account)
        if has_online_account:
            num_logins_last_month = random.randint(0, 20)
        else:
            num_logins_last_month = 0
            
        # num_paperless_bills_sent
        if billing_method in ["Email", "Online Portal"]:
            num_paperless_bills_sent = tenure_months # Assumiamo una bolletta al mese
        else:
            num_paperless_bills_sent = 0
            
        # last_survey_satisfaction_score (NPS-like, da 0 a 10)
        # Clienti insoddisfatti hanno un punteggio basso
        if churn_flag:
            last_survey_satisfaction_score = random.randint(0, 6)
        else:
            last_survey_satisfaction_score = random.randint(7, 10)
            
        # num_support_contacts_last_year (già presente, ma ricalcolata per coerenza)
        # Rafforziamo la correlazione con churn_flag
        if churn_flag:
            num_support_contacts_last_year = random.randint(3, 15)
        else:
            num_support_contacts_last_year = random.randint(0, 4)
            
        # num_complaints_last_year (sottoinsieme dei contatti di supporto)
        if num_support_contacts_last_year > 0:
            # Da 30% a 100% dei contatti possono essere lamentele
            complaint_ratio = random.uniform(0.3, 1.0)
            num_complaints_last_year = int(num_support_contacts_last_year * complaint_ratio)
        else:
            num_complaints_last_year = 0
            
        # complaint_resolution_time_avg
        if num_complaints_last_year > 0:
            # Risoluzione tra 1 e 30 giorni
            complaint_resolution_time_avg = random.randint(1, 30)
        else:
            complaint_resolution_time_avg = 0

        # --- Fine nuove caratteristiche ---

        data.append({
            "customer_id": customer_id,
            "contract_start_date": contract_start_date,
            "contract_end_date": contract_end_date,
            "monthly_charges": monthly_charges,
            "total_charges": total_charges,
            "payment_method": payment_method,
            "tenure_months": tenure_months,
            "service_type": service_type,
            "contract_type": contract_type,
            "name": name,
            # Nuove colonne
            "avg_monthly_consumption_kwh": avg_monthly_consumption_kwh,
            "num_support_contacts_last_year": num_support_contacts_last_year,
            # --- Nuove features avanzate ---
            "consumption_volatility": consumption_volatility,
            "consumption_trend": consumption_trend,
            "consumption_vs_local_avg_ratio": consumption_vs_local_avg_ratio,
            "peak_hour_consumption_ratio": peak_hour_consumption_ratio,
            "smart_meter_flag": smart_meter_flag,
            "has_promo": has_promo,
            "days_since_last_promo_end": days_since_last_promo_end,
            "num_price_changes_last_year": num_price_changes_last_year,
            "last_bill_amount_vs_avg": last_bill_amount_vs_avg,
            "num_late_payments": num_late_payments,
            "avg_days_late_payment": avg_days_late_payment,
            "billing_method": billing_method,
            "contract_renewal_reminder_sent": contract_renewal_reminder_sent,
            "days_to_contract_end": days_to_contract_end,
            "has_online_account": has_online_account,
            "num_logins_last_month": num_logins_last_month,
            "num_paperless_bills_sent": num_paperless_bills_sent,
            "last_survey_satisfaction_score": last_survey_satisfaction_score,
            "num_complaints_last_year": num_complaints_last_year,
            "complaint_resolution_time_avg": complaint_resolution_time_avg,
            # Demographic/Location (semplici simulazioni)
            "customer_tenure_type": customer_tenure_type
        })
        
    return data

def write_to_csv(data, filename):
    """
    Scrive i dati in un file CSV.
    """
    if not data:
        print("Nessun dato da scrivere.")
        return

    fieldnames = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Dataset avanzato generato e salvato in '{filename}' con {len(data)} record.")

if __name__ == "__main__":
    print("Generazione del dataset sintetico avanzato...")
    customer_data = generate_customer_data(NUM_RECORDS)
    write_to_csv(customer_data, OUTPUT_FILE)
    print("Operazione completata.")
