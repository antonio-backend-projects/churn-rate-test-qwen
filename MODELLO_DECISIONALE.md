# Modello Decisionale per la Previsione dell'Abbandono (Churn Prediction)

## Panoramica

Questo documento descrive il modello decisionale utilizzato dallo script `churn_calculator_ml.py` per prevedere quale clienti hanno una probabilità elevata di abbandonare il servizio (churn).

## Dati di Input

Il modello utilizza i seguenti attributi (caratteristiche o "features") dei clienti per effettuare le sue previsioni:

*   **`monthly_charges`**: Il costo mensile del contratto del cliente.
*   **`total_charges`**: Il costo totale accumulato dal cliente fino ad oggi.
*   **`tenure_months`**: La durata del contratto del cliente in mesi.
*   **`tenure_days`**: La durata del contratto del cliente in giorni (calcolata come differenza tra la data di inizio e la data di fine, o la data odierna per i clienti attivi).
*   **`payment_method`**: Il metodo di pagamento preferito dal cliente (es. carta di credito, bonifico, ecc.). Questo valore viene convertito in un numero tramite "label encoding".
*   **`service_type`**: Il tipo di servizio sottoscritto (es. elettricità, gas, entrambi). Anche questo viene convertito in un numero.
*   **`contract_type`**: Il tipo di contratto (es. mese a mese, un anno, due anni). Anche questo viene convertito in un numero.

## Modello di Machine Learning

Il modello utilizzato è un **Random Forest Classifier**. Questo tipo di modello è composto da molti alberi decisionali che lavorano insieme per prendere una decisione finale. È scelto per la sua capacità di gestire bene diversi tipi di dati e per fornire informazioni sull'importanza delle varie caratteristiche.

## Importanza delle Caratteristiche (Feature Importance)

Dopo l'addestramento, il modello calcola quanto ogni caratteristica contribuisce alla previsione. L'importanza è espressa come una percentuale. Di seguito un esempio basato su un'esecuzione del modello:

| Caratteristica             | Importanza (%) | Note                                                                 |
| :------------------------- | :------------- | :------------------------------------------------------------------- |
| **`tenure_days`**          | **42.9%**      | La caratteristica più influente. Una tenure molto lunga o molto breve può influenzare la previsione. |
| **`total_charges`**        | **16.9%**      | Un costo totale molto alto o molto basso può indicare rischio.       |
| **`monthly_charges`**      | **14.5%**      | Costi mensili estremi possono essere un fattore di rischio.          |
| **`tenure_months`**        | **12.0%**      | Simile a `tenure_days`, ma con un impatto leggermente minore.        |
| **`contract_type_encoded`**| **5.6%**       | I contratti "month-to-month" sono spesso più volatili.               |
| **`payment_method_encoded`**| **4.7%**      | Alcuni metodi di pagamento potrebbero essere associati a maggiore churn. |
| **`service_type_encoded`** | **3.5%**       | L'impatto del tipo di servizio è minore rispetto agli altri fattori. |

## Come Funziona la Previsione

1.  Il modello analizza i dati di ogni cliente in base alle caratteristiche elencate sopra.
2.  Confronta questi dati con i pattern appresi durante l'addestramento su un sottoinsieme dei dati.
3.  Calcola una **probabilità di churn** per ogni cliente, un numero tra 0 e 1 (0% e 100%).
4.  Nella versione corrente dello script, vengono restituiti i clienti con una **probabilità superiore al 50%**.
5.  Un filtro aggiuntivo esclude i clienti che hanno già un `contract_end_date` nel passato, poiché hanno già abbandonato.

## Limitazioni e Considerazioni

*   **Soglia di Probabilità**: La soglia del 50% è una scelta predefinita. Abbassandola si ottengono più clienti "a rischio", alzandola si ottengono solo i casi più probabili.
*   **Qualità del Modello**: Le performance attuali mostrano un'accuratezza del 89%, ma una precisione del 72% e un richiamo (recall) del 53% per i clienti che effettivamente abbandonano. Ciò significa che il modello potrebbe migliorare nel rilevare tutti i casi reali di churn.
*   **Interpretazione**: L'importanza delle feature dà un'indicazione generale, ma le relazioni reali possono essere più complesse (es. una combinazione di tenure corta e costi alti).

## Conclusione

Il modello identifica principalmente i clienti a rischio osservando **da quanto tempo sono clienti** (`tenure_days`, `tenure_months`) e **quanto hanno speso** (`total_charges`, `monthly_charges`). Altri fattori come il tipo di contratto hanno un peso minore ma contribuiscono comunque alla previsione finale. Questo approccio permette di concentrare gli sforzi di retention sui clienti attivi che il modello ritiene più vulnerabili.