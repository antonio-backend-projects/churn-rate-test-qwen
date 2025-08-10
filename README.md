# Churn Rate Calculator

Questa repository contiene due script Python per calcolare il churn rate per un'azienda di energia e gas: una versione base e una versione avanzata con machine learning.

## Script Disponibili

### 1. churn_calculator.py (Versione Base)
Uno script semplice che calcola il churn rate tradizionale basato sullo stato attuale dei clienti.

**Funzionalità:**
- Calcola il churn rate totale: (Numero di Clienti Persi / Numero Totale di Clienti) * 100
- Utilizza dati minimi sui clienti (solo customer_id e status)

### 2. churn_calculator_ml.py (Versione Avanzata)
Uno script avanzato che include calcoli temporali, analisi predittiva con machine learning e visualizzazione dei trend.

**Funzionalità:**
- Calcola churn rate mensile e trimestrale
- Predice i clienti con alta probabilità di churn usando machine learning
- Analizza pattern e trend del churn
- Genera grafici per la visualizzazione dei dati
- Fornisce report sulle performance del modello ML

## Requisiti

- Python 3.7+
- pandas
- scikit-learn
- matplotlib
- seaborn

## Installazione

1. Clona o scarica questa repository
2. Installa i pacchetti richiesti:
   ```
   pip install -r requirements.txt
   ```

## Utilizzo

### Versione Base (churn_calculator.py)

1. Prepara i dati dei clienti in un file CSV con queste colonne:
   - `customer_id`: Identificativo univoco del cliente
   - `status`: Stato del cliente ('churned' o 'active')

2. Esegui lo script:
   ```
   python churn_calculator.py
   ```

3. Quando richiesto, inserisci il percorso del tuo file CSV.

### Versione Avanzata (churn_calculator_ml.py)

1. Prepara i dati dei clienti in un file CSV con queste colonne:
   - `customer_id`: Identificativo univoco del cliente
   - `contract_start_date`: Data di inizio contratto (YYYY-MM-DD)
   - `contract_end_date`: Data di fine contratto (YYYY-MM-DD), vuoto se ancora attivo
   - `monthly_charges`: Addebiti mensili del cliente
   - `total_charges`: Addebiti totali del cliente
   - `payment_method`: Metodo di pagamento utilizzato dal cliente
   - `tenure_months`: Numero di mesi di fidelizzazione del cliente
   - `service_type`: Tipo di servizio (electricity, gas, both)
   - `contract_type`: Tipo di contratto (month-to-month, one year, two year)

2. Esegui lo script:
   ```
   python churn_calculator_ml.py [percorso_file_csv] [anno]
   ```
   
   Entrambi i parametri sono opzionali:
   - `percorso_file_csv`: Percorso al file CSV con i dati dei clienti
   - `anno`: Anno per l'analisi (es. 2023)

3. Se non forniti, lo script chiederà di inserire questi valori interattivamente.

## File di Esempio

Nella repository sono inclusi due file CSV di esempio:
- `sample_customer_data.csv`: File di esempio per la versione base
- `customer_data.csv`: File di esempio per la versione avanzata