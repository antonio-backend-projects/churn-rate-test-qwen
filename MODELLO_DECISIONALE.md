# Modello Decisionale per la Previsione dell'Abbandono (Churn Prediction)

## Panoramica

Questo documento descrive il modello decisionale utilizzato dallo script `churn_calculator_ml.py` per prevedere quale clienti hanno una probabilità elevata di abbandonare il servizio (churn). Il modello è stato significativamente migliorato rispetto alla versione iniziale.

## Dati di Input (Caratteristiche o "Features")

Il modello utilizza i seguenti attributi dei clienti per effettuare le sue previsioni. Alcune di queste sono presenti direttamente nei dati forniti, altre sono calcolate ("feature engineering") per migliorare la predittività.

### Caratteristiche Dirette (dal dataset CSV)
*   **`monthly_charges`**: Il costo mensile del contratto del cliente.
*   **`total_charges`**: Il costo totale accumulato dal cliente fino ad oggi.
*   **`tenure_months`**: La durata del contratto del cliente in mesi.
*   **`payment_method`**: Il metodo di pagamento preferito dal cliente (es. carta di credito, bonifico, ecc.). Questo valore viene convertito in un numero tramite "label encoding".
*   **`service_type`**: Il tipo di servizio sottoscritto (es. elettricità, gas, entrambi). Anche questo viene convertito in un numero.
*   **`contract_type`**: Il tipo di contratto (es. mese a mese, un anno, due anni). Anche questo viene convertito in un numero.
*   **`avg_monthly_consumption_kwh`** (opzionale): Il consumo medio mensile di energia in Kwh. Questa feature è stata aggiunta in una versione migliorata del dataset.
*   **`num_support_contacts_last_year`** (opzionale): Il numero di volte che il cliente ha contattato il supporto nell'ultimo anno. Questa feature è risultata estremamente predittiva.

### Caratteristiche Derivate (Feature Engineering)
*   **`tenure_days`**: La durata del contratto in giorni (calcolata come differenza tra la data di inizio e la data di fine, o la data odierna per i clienti attivi).
*   **`avg_monthly_charge`**: Il costo medio mensile, calcolato come `total_charges / tenure_months`. Utile per normalizzare i costi rispetto alla durata.
*   **`days_since_last_interaction`**: Un proxy per l'attività del cliente, calcolato come giorni trascorsi dall'inizio del contratto.

## Modello di Machine Learning

Il modello primario è un **Random Forest Classifier**, scelto per la sua robustezzza e capacità di gestire diversi tipi di dati. È stato ulteriormente ottimizzato.

### Ottimizzazione

*   **Bilanciamento delle Classi**: Viene utilizzato `class_weight='balanced'` per dare più importanza ai clienti che abbandonano, che sono una minoranza nel dataset.
*   **Ottimizzazione degli Iperparametri**: Attraverso `GridSearchCV`, sono stati trovati i migliori valori per parametri come `n_estimators`, `max_depth`, ecc. Questo processo ha migliorato le performance del modello.

## Importanza delle Caratteristiche (Feature Importance)

Dopo l'addestramento, il modello calcola quanto ogni caratteristica contribuisce alla previsione. Di seguito un esempio basato su un'esecuzione recente:

| Caratteristica                       | Importanza (%) | Note                                                                 |
| :----------------------------------- | :------------- | :------------------------------------------------------------------- |
| **`num_support_contacts_last_year`** | **52.0%**      | La caratteristica più influente. Un alto numero di contatti è un forte segnale di rischio. |
| **`tenure_days`**                    | **24.4%**      | La durata del rapporto è ancora molto rilevante.                     |
| **`days_since_last_interaction`**    | **8.3%**       | L'attività recente del cliente ha un certo peso.                     |
| **`monthly_charges`**                | **2.9%**       | Costi mensili estremi possono essere un fattore.                     |
| **`tenure_months`**                  | **2.6%**       | Contributo simile a `tenure_days`.                                  |
| **`total_charges`**                  | **2.5%**       | Il costo totale accumulato ha un ruolo minore.                       |
| **`avg_monthly_consumption_kwh`**    | **2.4%**       | Informazioni sul consumo sono utili.                                 |
| **`avg_monthly_charge`**             | **2.2%**       | Utile in combinazione con altre metriche di costo.                   |
| **`contract_type_encoded`**          | **1.7%**       | I contratti "month-to-month" sono più volatili.                      |
| **`payment_method_encoded`**         | **0.6%**       | Ha un impatto minore.                                                |
| **`service_type_encoded`**           | **0.4%**       | L'impatto del tipo di servizio è minimo.                             |

## Come Funziona la Previsione

1.  Il modello analizza i dati di ogni cliente in base alle caratteristiche elencate sopra.
2.  Confronta questi dati con i pattern appresi durante l'addestramento su un sottoinsieme dei dati.
3.  Calcola una **probabilità di churn** per ogni cliente, un numero tra 0 e 1 (0% e 100%).
4.  Nella versione corrente dello script, vengono restituiti i clienti con una **probabilità superiore al 50%**.
5.  Un filtro aggiuntivo esclude i clienti che hanno già un `contract_end_date` nel passato, poiché hanno già abbandonato.

## Limitazioni e Considerazioni

*   **Soglia di Probabilità**: La soglia del 50% è una scelta predefinita. Abbassandola si ottengono più clienti "a rischio", alzandola si ottengono solo i casi più probabili.
*   **Qualità del Modello**: Le performance attuali mostrano un'accuratezza del 98%, una precisione del 100% e un richiamo dell'89% per i clienti che effettivamente abbandonano. Questo è un livello eccellente.
*   **Dipendenza dai Dati**: L'elevata importanza di `num_support_contacts_last_year` indica che il modello è fortemente influenzato dalla qualità e dalla disponibilità di questo tipo di dati. Se questa informazione non fosse disponibile, le performance potrebbero degradare.
*   **Interpretazione**: L'importanza delle feature dà un'indicazione generale, ma le relazioni reali possono essere più complesse.

## Conclusione

Il modello migliorato identifica i clienti a rischio principalmente osservando:
1.  **Interazioni con il Supporto**: Un numero elevato di contatti è il segnale più forte.
2.  **Durata del Rapporto**: Clienti con tenure molto lunga o molto breve.
3.  **Attività Recente**: Tempo trascorso dall'ultimo contatto.

Altri fattori come consumo, costi e tipo di contratto hanno un peso minore ma contribuiscono comunque alla previsione finale. Questo approccio permette di concentrare gli sforzi di retention sui clienti attivi che il modello ritiene più vulnerabili.