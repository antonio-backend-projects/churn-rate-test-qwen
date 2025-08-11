# Guida Completa all'Utilizzo del Churn Rate Calculator

## Introduzione

Il Churn Rate Calculator è un progetto Python progettato per calcolare e prevedere il tasso di abbandono (churn rate) dei clienti per un'azienda di energia e gas. Il progetto include due script principali: uno per il calcolo tradizionale del churn rate e uno avanzato che utilizza machine learning per la previsione.

## Installazione

1.  **Clonare o scaricare il repository**:
    Apri un terminale e naviga nella directory in cui desideri clonare il progetto. Esegui il seguente comando:
    ```bash
    git clone https://github.com/il-tuo-username/churn-rate-calculator.git
    ```
    Sostituisci `https://github.com/il-tuo-username/churn-rate-calculator.git` con l'URL effettivo del repository se è diverso.

2.  **Navigare nella directory del progetto**:
    ```bash
    cd churn-rate-calculator
    ```

3.  **Installare le dipendenze**:
    Assicurati di avere Python 3.7 o versione successiva installato. Quindi, installa le librerie necessarie eseguendo:
    ```bash
    pip install -r requirements.txt
    ```

## Struttura del Progetto

Una volta scaricato, il progetto avrà la seguente struttura:

```
churn-rate-calculator/
├── churn_calculator.py
├── churn_calculator_ml.py
├── sample_customer_data.csv
├── customer_data.csv
├── customer_data_large.csv
├── customer_data_enriched.csv
├── customer_data_advanced.csv
├── generate_large_customer_data.py
├── generate_enriched_customer_data.py
├── generate_advanced_customer_data.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── MODELLO_DECISIONALE.md
├── NEXT_STEPS.md
├── QWEN.md
├── RIASSUNTO_PROGETTO.md
├── SCRIPTS.md
└── assets/
    └── images/
        └── Calcolo_del_Tasso_di_Abbandono.png
```

*   **`churn_calculator.py`**: Script per il calcolo tradizionale del churn rate.
*   **`churn_calculator_ml.py`**: Script avanzato con analisi ML.
*   **`sample_customer_data.csv`**: Dataset minimale per `churn_calculator.py`.
*   **`customer_data.csv`**: Dataset standard per `churn_calculator_ml.py`.
*   **`customer_data_large.csv`**: Dataset sintetico più grande.
*   **`customer_data_enriched.csv`**: Dataset con caratteristiche aggiuntive.
*   **`customer_data_advanced.csv`**: Dataset con caratteristiche avanzate simulate.
*   **`generate_*.py`**: Script per generare dataset sintetici.
*   **`requirements.txt`**: Elenco delle dipendenze Python.
*   **`README.md`**: Documentazione principale del progetto.
*   **`CHANGELOG.md`**: Log delle modifiche.
*   **`MODELLO_DECISIONALE.md`**: Descrizione dettagliata del modello ML.
*   **`NEXT_STEPS.md`**: Guida per lo sviluppo futuro.
*   **`QWEN.md`**: Guida operativa per Qwen Code.
*   **`RIASSUNTO_PROGETTO.md`**: Panoramica del progetto.
*   **`SCRIPTS.md`**: Descrizione dettagliata degli script.
*   **`assets/`**: Directory per immagini e altri file statici.

## Utilizzo dello Script Base (`churn_calculator.py`)

### Funzionalità

Questo script calcola il churn rate totale utilizzando un approccio tradizionale basato sullo stato attuale dei clienti. La formula utilizzata è:
`Churn Rate = (Numero di Clienti Persi / Numero Totale di Clienti) * 100`

### Requisiti del Dataset

Il file CSV deve contenere almeno le seguenti colonne:

*   `customer_id`: Identificativo univoco del cliente (stringa o numero).
*   `status`: Stato del cliente. I valori accettati sono `'churned'` per i clienti persi e `'active'` per i clienti attivi. Altri valori saranno ignorati nel calcolo del churn rate.

Esempio di struttura del file CSV (`sample_customer_data.csv`):
```csv
customer_id,status
1,active
2,churned
3,active
4,churned
5,active
```

### Esecuzione

1.  Apri un terminale e naviga nella directory del progetto.
2.  Esegui il comando:
    ```bash
    python churn_calculator.py
    ```
3.  Quando richiesto, inserisci il percorso del file CSV contenente i dati dei clienti.
    Esempio:
    ```
    Inserisci il percorso del file CSV: sample_customer_data.csv
    ```
4.  Lo script calcolerà e visualizzerà il churn rate totale.
    Esempio di output:
    ```
    Churn Rate Totale: 40.00%
    ```

## Utilizzo dello Script Avanzato (`churn_calculator_ml.py`)

### Funzionalità

Questo script offre funzionalità avanzate:

1.  **Calcolo di churn rate mensili e trimestrali**: Analizza i dati per un anno specificato e calcola i tassi di abbandono per ogni mese e trimestre.
2.  **Predizione del churn con Machine Learning**: Utilizza modelli come Random Forest, XGBoost o Logistic Regression per prevedere quali clienti hanno un'alta probabilità di abbandonare.
3.  **Analisi e visualizzazione dei trend**: Genera grafici per visualizzare l'andamento del churn rate nel tempo.
4.  **Report sulle performance del modello**: Fornisce metriche dettagliate (Accuracy, Precision, Recall, F1-Score) per valutare l'efficacia del modello predittivo.
5.  **Importanza delle caratteristiche**: Mostra quali colonne del dataset sono più influenti nella previsione del churn.
6.  **Confronto tra modelli**: Permette di confrontare le performance di diversi modelli ML.

### Requisiti del Dataset

Il file CSV può contenere diverse colonne. Alcune sono obbligatorie per il calcolo base, altre sono utilizzate dal modello ML per migliorare le previsioni.

**Colonne Obbligatorie per il Calcolo del Churn Rate Temporale:**

*   `customer_id` (obbligatorio): Identificativo univoco del cliente.
*   `contract_start_date` (obbligatorio): Data di inizio del contratto (formato YYYY-MM-DD).
*   `contract_end_date` (obbligatorio): Data di fine del contratto (formato YYYY-MM-DD). Se il cliente è ancora attivo, questa cella deve essere vuota.

**Colonne Utilizzate per il Machine Learning (Consigliate):**

*   `monthly_charges`: Addebiti mensili del cliente.
*   `total_charges`: Addebiti totali accumulati dal cliente.
*   `payment_method`: Metodo di pagamento utilizzato (es. 'Credit card', 'Bank transfer').
*   `tenure_months`: Numero di mesi di fidelizzazione del cliente.
*   `service_type`: Tipo di servizio (es. 'electricity', 'gas', 'both').
*   `contract_type`: Tipo di contratto (es. 'month-to-month', 'one year', 'two year').
*   `avg_monthly_consumption_kwh` (opzionale): Consumo medio mensile in Kwh.
*   `num_support_contacts_last_year` (opzionale): Numero di contatti con il supporto nell'ultimo anno.
*   `consumption_volatility` (opzionale): Deviazione standard del consumo mensile.
*   `consumption_trend` (opzionale): Pendenza del consumo negli ultimi mesi.
*   `last_survey_satisfaction_score` (opzionale): Punteggio di soddisfazione da un'indagine recente.
*   `num_late_payments` (opzionale): Numero di pagamenti in ritardo negli ultimi 12 mesi.
*   `days_to_contract_end` (opzionale): Giorni mancanti alla scadenza del contratto corrente.
*   `has_online_account` (opzionale): Indica se il cliente ha un account online.
*   `num_complaints_last_year` (opzionale): Numero di lamentele registrate nell'ultimo anno.

Esempio di struttura del file CSV (`customer_data.csv`):
```csv
customer_id,contract_start_date,contract_end_date,monthly_charges,total_charges,payment_method,tenure_months,service_type,contract_type
1,2022-01-15,,75.50,906.00,Credit card,12,electricity,one year
2,2021-05-20,2022-05-20,60.00,720.00,Bank transfer,12,gas,one year
3,2023-03-10,,80.25,240.75,Credit card,3,both,month-to-month
```

### Esecuzione

1.  Apri un terminale e naviga nella directory del progetto.
2.  Esegui il comando:
    ```bash
    python churn_calculator_ml.py [percorso_file_csv] [anno] [modello]
    ```
    *   **`percorso_file_csv`**: (Opzionale) Percorso al file CSV con i dati dei clienti. Se non specificato, lo script chiederà di inserirlo.
    *   **`anno`**: (Opzionale) Anno per l'analisi (es. 2023). Se non specificato, lo script chiederà di inserirlo.
    *   **`modello`**: (Opzionale) Modello ML da utilizzare (`random_forest`, `xgboost`, `logistic_regression`). Se non specificato, verrà utilizzato `random_forest`.

    **Esempi:**
    *   Esecuzione con parametri interattivi:
        ```bash
        python churn_calculator_ml.py
        ```
    *   Esecuzione specificando il file CSV e l'anno:
        ```bash
        python churn_calculator_ml.py customer_data.csv 2023
        ```
    *   Esecuzione specificando il file CSV, l'anno e il modello:
        ```bash
        python churn_calculator_ml.py customer_data.csv 2023 xgboost
        ```

3.  Se i parametri non vengono forniti come argomenti, lo script li chiederà interattivamente:
    ```
    Inserisci il percorso del file CSV (default: customer_data.csv):
    Inserisci l'anno per l'analisi (es. 2023):
    Scegli il modello ML (random_forest, xgboost, logistic_regression) (default: random_forest):
    ```

### Output dello Script Avanzato

L'esecuzione dello script `churn_calculator_ml.py` produrrà diversi tipi di output:

1.  **Churn Rate Mensili e Trimestrali**: Verrà stampato un elenco dei churn rate per ogni mese e trimestre dell'anno specificato.
    Esempio:
    ```
    --- Churn Rate Mensile per il 2023 ---
    Gennaio 2023: 5.00%
    Febbraio 2023: 3.00%
    ...
    --- Churn Rate Trimestrale per il 2023 ---
    Q1 2023: 4.00%
    Q2 2023: 3.50%
    ...
    ```

2.  **Grafici dei Trend**: Verranno generati e mostrati due grafici:
    *   Un grafico a linee che mostra l'andamento del churn rate mensile.
    *   Un grafico a barre che mostra il churn rate trimestrale.
    Questi grafici vengono visualizzati in finestre separate. Chiudi le finestre dei grafici per continuare l'esecuzione dello script.

3.  **Addestramento del Modello ML**: Lo script addestrerà il modello ML selezionato sui dati forniti. Verrà mostrato un messaggio di conferma.
    Esempio:
    ```
    Addestramento del modello Random Forest in corso...
    Modello Random Forest addestrato con successo.
    ```

4.  **Report sulle Performance del Modello**: Verranno visualizzate le metriche di performance del modello.
    Esempio:
    ```
    --- Performance del Modello ---
    Accuracy: 0.98
    Precision: 1.00
    Recall: 0.89
    F1-Score: 0.94
    ```

5.  **Importanza delle Caratteristiche**: Verrà mostrata una lista delle caratteristiche del dataset ordinate per importanza nel modello.
    Esempio:
    ```
    --- Importanza delle Caratteristiche ---
    Feature: num_support_contacts_last_year, Importance: 0.52
    Feature: tenure_days, Importance: 0.15
    ...
    ```

6.  **Predizione del Churn**: Lo script predice i clienti con un'alta probabilità (soglia > 50%) di abbandonare il servizio. Verrà stampato un elenco di questi clienti, escludendo quelli che hanno già un `contract_end_date` nel passato.
    Esempio:
    ```
    --- Clienti con Alta Probabilità di Churn (Probabilità > 50%) ---
    Customer ID: 101, Probabilità: 92.5%
    Customer ID: 205, Probabilità: 87.3%
    ...
    ```

7.  **Confronto tra Modelli (se richiesto)**: Se si utilizza il metodo `compare_models`, verrà mostrato un report comparativo delle performance di tutti i modelli disponibili.

## Generazione di Dataset Sintetici

Il progetto include script per generare dataset sintetici di diverse dimensioni e complessità:

1.  **`generate_large_customer_data.py`**: Crea un dataset `customer_data_large.csv` con un numero elevato di clienti (50000 per default). Utile per testare le performance con grandi volumi di dati.
    ```bash
    python generate_large_customer_data.py
    ```

2.  **`generate_enriched_customer_data.py`**: Crea un dataset `customer_data_enriched.csv` con caratteristiche aggiuntive come `avg_monthly_consumption_kwh` e `num_support_contacts_last_year`. Queste caratteristiche sono cruciali per ottenere performance elevate con il modello ML.
    ```bash
    python generate_enriched_customer_data.py
    ```

3.  **`generate_advanced_customer_data.py`**: Crea un dataset `customer_data_advanced.csv` con un'ampia gamma di caratteristiche simulate, tra cui `consumption_volatility`, `consumption_trend`, `last_survey_satisfaction_score`, ecc. Questo dataset è ideale per testare il modello con il set completo di features previste.
    ```bash
    python generate_advanced_customer_data.py
    ```

## Analisi delle Performance

Le performance del modello ML sono state ottimizzate e testate. I risultati attuali con il dataset `customer_data_enriched.csv` e `customer_data_advanced.csv` sono eccellenti:

*   **Accuratezza**: 98%
*   **Precisione per i clienti che abbandonano**: 100%
*   **Richiamo (Recall) per i clienti che abbandonano**: 89%

La caratteristica più predittiva identificata è il **numero di contatti con il supporto nell'ultimo anno** (`num_support_contacts_last_year`).

## Risoluzione dei Problemi (Troubleshooting)

*   **Errore "FileNotFoundError"**: Verifica che il percorso del file CSV fornito sia corretto e che il file esista nella directory specificata.
*   **Errore "KeyError" o colonne mancanti**: Controlla che il file CSV contenga tutte le colonne obbligatorie con i nomi esatti. I nomi delle colonne sono case-sensitive.
*   **Grafico non appare**: Assicurati che il tuo ambiente supporti la visualizzazione di grafici matplotlib. Se stai eseguendo lo script in un ambiente server senza GUI, i grafici potrebbero non essere visualizzati. In tal caso, puoi modificare lo script per salvare i grafici come file immagine.
*   **Performance del modello basse**: Le eccellenti performance sono fortemente legate alla qualità e completezza delle feature di input. Se molte delle colonne opzionali non sono presenti nel dataset, le performance del modello ML potrebbero calare. Utilizza i dataset forniti (`customer_data_enriched.csv` o `customer_data_advanced.csv`) per ottenere i migliori risultati.

## Personalizzazione e Sviluppo

Il progetto è progettato per essere estensibile. Puoi:

*   **Aggiungere nuove features**: Modifica lo script `churn_calculator_ml.py` per includere nuove colonne nel dataset e adattare la logica di preparazione dei dati (`prepare_ml_data`).
*   **Implementare nuovi modelli**: Segui la struttura esistente per aggiungere supporto ad altri algoritmi di machine learning.
*   **Migliorare la validazione dei dati**: Espandi le funzioni di caricamento e validazione per rendere lo script più robusto alla presenza di dati errati o mancanti.
*   **Creare un'API**: Sviluppa un'interfaccia REST per esporre le funzionalità del modello.
*   **Integrare SHAP**: Aggiungi la libreria SHAP per fornire spiegazioni dettagliate delle predizioni del modello.

## Contribuire al Progetto

Se desideri contribuire a questo progetto, segui questi passaggi:

1.  Forka il repository.
2.  Crea un nuovo branch per la tua feature o correzione di bug (`git checkout -b feature/nuova-feature`).
3.  Esegui il commit delle tue modifiche (`git commit -am 'Aggiungi nuova feature'`).
4.  Esegui il push del branch (`git push origin feature/nuova-feature`).
5.  Apri una Pull Request.

Assicurati che il tuo codice sia ben documentato e che tutti i test passino prima di inviare una Pull Request.