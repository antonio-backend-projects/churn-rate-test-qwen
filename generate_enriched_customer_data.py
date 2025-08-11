"""
Script per generare un dataset sintetico piu' grande e arricchito per il churn rate calculator.
Include nuove caratteristiche come consumo medio mensile e interazioni.
Basato sul formato del file customer_data.csv esistente.
"""

import csv
import random
from datetime import datetime, timedelta
import itertools

# --- Configurazione ---
NUM_RECORDS = 1000  # Numero di righe da generare
OUTPUT_FILE = "customer_data_enriched.csv"

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
SERVICE_TYPES = ["electricity", "gas", "both"]
CONTRACT_TYPES = ["month-to-month", "one year", "two year"]

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
        
        # Genera monthly_charges
        base_monthly_charge = random.uniform(50.0, 120.0)
        # Per i clienti che abbandonano, potrebbe esserci un leggero calo nei costi nei mesi finali
        if churn_flag and random.random() < 0.4:
             monthly_charges = round(base_monthly_charge * random.uniform(0.8, 0.95), 1)
        else:
             monthly_charges = round(base_monthly_charge, 1)
        
        # Calcola total_charges (con un po' di variabilità)
        # Potrebbe includere costi iniziali o arrotondamenti
        variability_factor = random.uniform(0.95, 1.05)
        total_charges = round(monthly_charges * tenure_months * variability_factor, 1)
        
        # --- Nuove caratteristiche ---
        # avg_monthly_consumption_kwh: Consumo medio mensile in Kwh (simulato)
        # Ipotizziamo un consumo medio di 300 Kwh per elettricità, 1500 per gas, e una combinazione per "both"
        if service_type == "electricity":
            avg_monthly_consumption_kwh = random.randint(200, 400)
        elif service_type == "gas":
            avg_monthly_consumption_kwh = random.randint(1000, 2000)
        else: # both
            avg_monthly_consumption_kwh = random.randint(1200, 2400)
            
        # num_support_contacts_last_year: Numero di contatti con il supporto nell'ultimo anno
        # Più alto per i clienti che abbandonano
        if churn_flag:
            num_support_contacts_last_year = random.randint(2, 10)
        else:
            num_support_contacts_last_year = random.randint(0, 3)
            
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
            "num_support_contacts_last_year": num_support_contacts_last_year
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
        
    print(f"Dataset generato e salvato in '{filename}' con {len(data)} record.")

if __name__ == "__main__":
    print("Generazione del dataset sintetico arricchito...")
    customer_data = generate_customer_data(NUM_RECORDS)
    write_to_csv(customer_data, OUTPUT_FILE)
    print("Operazione completata.")
