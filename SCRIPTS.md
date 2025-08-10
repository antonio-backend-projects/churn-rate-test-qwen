# Elenco degli Script

Questo documento fornisce una descrizione dettagliata di tutti gli script presenti nel progetto.

## 1. churn_calculator.py

### Descrizione
Script Python che calcola il churn rate per una azienda di energia e gas utilizzando un approccio tradizionale basato sui dati dei clienti presenti in un file CSV.

### Funzionalità Principali
- Calcola il churn rate totale in base allo stato dei clienti ('churned' o 'active')
- Utilizza la formula: Churn Rate = (Numero di Clienti Persi / Numero Totale di Clienti) * 100
- Legge i dati da un file CSV fornito dall'utente
- Gestisce errori come file non trovati o colonne mancanti

### Parametri Richiesti nel CSV
- `customer_id`: Identificativo univoco del cliente
- `status`: Stato del cliente ('churned' o 'active')

### Utilizzo
```bash
python churn_calculator.py
```
Lo script chiederà all'utente di inserire il percorso del file CSV contenente i dati dei clienti.

## 2. churn_calculator_ml.py

### Descrizione
Script Python avanzato che calcola il churn rate e utilizza modelli di machine learning per prevedere quali clienti potrebbero abbandonare il servizio. Include analisi temporale e visualizzazione dei trend.

### Funzionalità Principali
- Calcola churn rate mensile e trimestrale per un anno specificato
- Addestra un modello Random Forest per prevedere il churn
- Fornisce report sulle performance del modello ML
- Mostra l'importanza delle caratteristiche nel predire il churn
- Genera grafici per visualizzare i trend di churn
- Predice i clienti con alta probabilità di churn

### Parametri Richiesti nel CSV
- `customer_id`: Identificativo univoco del cliente
- `contract_start_date`: Data di inizio contratto (YYYY-MM-DD)
- `contract_end_date`: Data di fine contratto (YYYY-MM-DD), vuoto se ancora attivo
- `monthly_charges`: Addebiti mensili del cliente
- `total_charges`: Addebiti totali del cliente
- `payment_method`: Metodo di pagamento utilizzato dal cliente
- `tenure_months`: Numero di mesi di fidelizzazione del cliente
- `service_type`: Tipo di servizio (elettricità, gas, entrambi)
- `contract_type`: Tipo di contratto (mese-mese, un anno, due anni)

### Utilizzo
```bash
python churn_calculator_ml.py [percorso_file_csv] [anno]
```
Entrambi i parametri sono opzionali; se non forniti, lo script chiederà all'utente di inserirli.

### Classi e Metodi Principali
- `ChurnCalculator`: Classe principale per il calcolo del churn
  - `calculate_period_churn_rate(start_date, end_date)`: Calcola il churn rate per un periodo specifico
  - `calculate_monthly_churn_rates(year)`: Calcola i churn rate mensili per un anno
  - `calculate_quarterly_churn_rates(year)`: Calcola i churn rate trimestrali per un anno
  - `train_ml_model()`: Addestra il modello di machine learning
  - `predict_churn()`: Predice i clienti con alta probabilità di churn
  - `plot_churn_trends(year)`: Genera grafici dei trend di churn

## 3. File di Dati

### customer_data.csv
File CSV contenente dati dettagliati dei clienti per l'analisi avanzata con machine learning. Utilizzato dallo script `churn_calculator_ml.py`.

### sample_customer_data.csv
File CSV con dati minimi per il calcolo tradizionale del churn rate. Utilizzato dallo script `churn_calculator.py`.

## 4. File di Configurazione

### requirements.txt
Elenco delle dipendenze Python richieste per eseguire gli script:
- pandas (>=1.3.0)
- scikit-learn (>=1.0.0)
- matplotlib (>=3.5.0)
- seaborn (>=0.11.0)

### README.md
File di documentazione principale del progetto con istruzioni per l'installazione e l'utilizzo.