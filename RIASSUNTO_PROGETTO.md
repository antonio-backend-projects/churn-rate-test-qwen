# Progetto Churn Rate Calculator - Riassunto e Piano di Miglioramento

## Panoramica del Progetto

Questo progetto mira a sviluppare un sistema affidabile per prevedere il churn (abbandono) dei clienti per un'azienda che fornisce energia elettrica e gas. Utilizza tecniche di Machine Learning su dati storici dei clienti per identificare quelli a rischio e consentire azioni di retention mirate.

## Componenti Principali

1.  **`churn_calculator.py`**: Script base per il calcolo di tassi di abbandono storici.
2.  **`churn_calculator_ml.py`**: Script avanzato che include analisi predittiva con Machine Learning.
3.  **Dataset**:
    *   `customer_data.csv`: Dataset originale di esempio.
    *   `customer_data_large.csv`: Dataset sintetico più grande per test.
    *   `customer_data_enriched.csv`: Dataset sintetico avanzato con caratteristiche aggiuntive.
    *   `customer_data_advanced.csv`: Nuovo dataset sintetico con caratteristiche avanzate.

## Evoluzione del Modello

Il modello è passato attraverso diverse fasi di miglioramento:

### Fase 1: Modello Base
*   **Caratteristiche**: `monthly_charges`, `total_charges`, `tenure_months`, `tenure_days`, codifica di `payment_method`, `service_type`, `contract_type`.
*   **Modello**: `RandomForestClassifier` con parametri predefiniti.
*   **Performance**: Accuratezza ~89%, Richiamo per "Abbandono" ~53%.

### Fase 2: Miglioramenti Iniziali
*   **Aggiunte**:
    *   Feature Engineering: `avg_monthly_charge`, `days_since_last_interaction`.
    *   Gestione del bilanciamento delle classi (`class_weight='balanced'`).
*   **Dataset**: `customer_data_enriched.csv` con `avg_monthly_consumption_kwh` e `num_support_contacts_last_year`.
*   **Performance**: Accuratezza 97%, Richiamo per "Abbandono" 84%.

### Fase 3: Ottimizzazione degli Iperparametri (Attuale)
*   **Aggiunte**:
    *   Integrazione di `GridSearchCV` per ottimizzare `RandomForestClassifier`.
*   **Migliori Iperparametri Trovati**: `max_depth=10`, `min_samples_leaf=1`, `min_samples_split=5`, `n_estimators=50`.
*   **Performance Attuali**: Accuratezza **98%**, Richiamo per "Abbandono" **89%**.
*   **Feature Importance Dominante**: `num_support_contacts_last_year` (52%).

## Piano di Miglioramento Completivo

### Fase 1: Analisi e Preparazione dei Dati Esistenti (Completata)
*   [x] Aggiunta di Feature Derivate (Feature Engineering).
*   [x] Gestione del Bilanciamento delle Classi.

### Fase 2: Ottimizzazione del Modello (Completata)
*   [x] Ricerca degli Iperparametri con `GridSearchCV`.

### Fase 3: Esplorazione di Altri Modelli (In Corso)
*   [x] Integrare e valutare altri modelli come `XGBoost`, `LogisticRegression`.
*   [ ] Implementare un classificatore ensemble per combinare predizioni.

### Fase 4: Integrazione di Nuove Fonti di Dati (In Corso)
*   [x] Espansione del dataset con caratteristiche simulate (`customer_data_enriched.csv`).
*   [x] Creazione di `customer_data_advanced.csv` con caratteristiche avanzate.
*   [ ] Definire un piano per integrare dati reali di consumo e assistenza.
*   [ ] Strutturare il processo per un flusso dati continuo.

### Fase 5: Interpretazione e Deployment (Futuro)
*   [ ] Sviluppare strumenti per interpretare le predizioni a livello individuale.
*   [ ] Creare un'interfaccia utente o un'API per esporre il modello.
*   [ ] Definire metriche di monitoraggio per il modello in produzione.

## Tecnologie Utilizzate

*   **Linguaggio**: Python 3.x
*   **Librerie Principali**:
    *   `pandas`, `numpy`: Per la manipolazione e l'analisi dei dati.
    *   `scikit-learn`: Per il machine learning.
    *   `matplotlib`, `seaborn`: Per la visualizzazione.
*   **Modelli ML**: `RandomForestClassifier` (primario), `XGBoost`, `LogisticRegression`.

## Conclusioni

Il progetto ha raggiunto un livello di maturità significativo. Il modello attuale è affidabile e fornisce risultati eccellenti grazie all'integrazione di dati contestuali critici (come le interazioni con il supporto) e all'ottimizzazione del modello. Il prossimo passo sarà l'esplorazione di altri modelli e la definizione di un percorso chiaro per l'integrazione di dati aziendali reali e il deployment in un ambiente di produzione.