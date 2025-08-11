# Modello Decisionale per la Previsione dell'Abbandono (Churn Prediction)

## Panoramica

Questo documento descrive il modello decisionale utilizzato dallo script `churn_calculator_ml.py` per prevedere quale clienti hanno una probabilità elevata di abbandonare il servizio (churn). Il modello è stato significativamente migliorato ed è ora in grado di raggiungere livelli di accuratezza eccellenti grazie all'integrazione di un ampio set di caratteristiche predittive.

## Dati di Input (Caratteristiche o "Features")

Il modello utilizza un ampio insieme di attributi dei clienti per effettuare le sue previsioni. Alcune di queste sono presenti direttamente nei dati forniti, altre sono calcolate ("feature engineering") per migliorare la predittività.

### Caratteristiche Dirette (dal dataset CSV)

*   **`monthly_charges`**: Il costo mensile del contratto del cliente.
*   **`total_charges`**: Il costo totale accumulato dal cliente fino ad oggi.
*   **`tenure_months`**: La durata del contratto del cliente in mesi.
*   **`payment_method`**: Il metodo di pagamento preferito dal cliente. Questo valore viene convertito in un numero tramite "label encoding".
*   **`service_type`**: Il tipo di servizio sottoscritto (es. elettricità, gas, entrambi). Anche questo viene convertito in un numero.
*   **`contract_type`**: Il tipo di contratto (es. mese a mese, un anno, due anni). Anche questo viene convertito in un numero.
*   **`avg_monthly_consumption_kwh`**: Il consumo medio mensile di energia in Kwh.
*   **`num_support_contacts_last_year`**: Il numero di volte che il cliente ha contattato il supporto nell'ultimo anno.
*   **`consumption_volatility`**: Deviazione standard del consumo mensile negli ultimi mesi.
*   **`consumption_trend`**: La pendenza del consumo negli ultimi mesi (crescente o decrescente).
*   **`consumption_vs_local_avg_ratio`**: Rapporto tra il consumo del cliente e la media della sua zona.
*   **`peak_hour_consumption_ratio`**: Percentuale del consumo in fasce orarie di punta.
*   **`smart_meter_flag`**: Indica se il cliente ha un contatore intelligente.
*   **`has_promo`**: Indica se il cliente è attualmente in un periodo promozionale.
*   **`days_since_last_promo_end`**: Giorni trascorsi dalla fine dell'ultima promozione.
*   **`num_price_changes_last_year`**: Numero di cambiamenti al piano tariffario nell'ultimo anno.
*   **`last_bill_amount_vs_avg`**: Rapporto tra l'importo dell'ultima bolletta e la media.
*   **`num_late_payments`**: Numero di pagamenti in ritardo negli ultimi 12 mesi.
*   **`avg_days_late_payment`**: Media dei giorni di ritardo per i pagamenti.
*   **`billing_method`**: Metodo di fatturazione (carta, email, portale). Convertito in numero.
*   **`contract_renewal_reminder_sent`**: Indica se è stato inviato un promemoria per il rinnovo.
*   **`days_to_contract_end`**: Giorni mancanti alla scadenza del contratto corrente.
*   **`has_online_account`**: Indica se il cliente ha attivato un account online.
*   **`num_logins_last_month`**: Frequenza di accesso al portale online.
*   **`num_paperless_bills_sent`**: Numero di bollette inviate in digitale.
*   **`last_survey_satisfaction_score`**: Punteggio di soddisfazione da un'indagine recente.
*   **`num_complaints_last_year`**: Numero di lamentele registrate nell'ultimo anno.
*   **`complaint_resolution_time_avg`**: Tempo medio per risolvere le lamentele.
*   **`customer_tenure_type`**: Tipo di proprietà del cliente (proprietario, inquilino). Convertito in numero.

### Caratteristiche Derivate (Feature Engineering)

*   **`tenure_days`**: La durata del rapporto in giorni (calcolata come differenza tra la data di inizio e la data di fine, o la data odierna per i clienti attivi).
*   **`avg_monthly_charge`**: Il costo medio mensile, calcolato come `total_charges / tenure_months`.
*   **`days_since_last_interaction`**: Un proxy per l'attività del cliente, calcolato come giorni trascorsi dall'inizio del contratto.

## Modello di Machine Learning

Il modello primario è un **Random Forest Classifier**, scelto per la sua robustezza e capacità di gestire diversi tipi di dati. È stato ulteriormente ottimizzato.

### Ottimizzazione

*   **Bilanciamento delle Classi**: Viene utilizzato `class_weight='balanced'` per dare più importanza ai clienti che abbandonano.
*   **Ottimizzazione degli Iperparametri**: Attraverso `GridSearchCV`, sono stati trovati i migliori valori per parametri come `n_estimators`, `max_depth`, ecc.

## Importanza delle Caratteristiche (Feature Importance)

Dopo l'addestramento, il modello calcola quanto ogni caratteristica contribuisce alla previsione. Di seguito un esempio basato su un'esecuzione recente con il dataset avanzato:

| Caratteristica                       | Importanza (%) | Note                                                                 |
| :----------------------------------- | :------------- | :------------------------------------------------------------------- |
| **`last_survey_satisfaction_score`** | **24.9%**      | La caratteristica più influente. Un punteggio basso è un forte segnale. |
| **`num_support_contacts_last_year`** | **20.3%**      | Ancora molto rilevante. Un alto numero di contatti indica rischio.   |
| **`num_late_payments`**              | **12.7%**      | Problemi di pagamento sono un forte indicatore.                      |
| **`days_to_contract_end`**           | **8.2%**       | Periodo critico per il rinnovo.                                      |
| **`num_complaints_last_year`**       | **7.3%**       | Le lamentele specifiche sono un segnale forte.                       |
| **`avg_days_late_payment`**          | **6.8%**       | Non solo il numero, ma la gravità dei ritardi conta.                 |
| **`tenure_days`**                    | **5.4%**       | La durata del rapporto rimane importante.                            |
| **`consumption_trend`**              | **3.5%**       | Un consumo in calo è preoccupante.                                   |
| **`consumption_volatility`**         | **3.3%**       | Un consumo instabile può indicare problemi.                          |
| **`last_bill_amount_vs_avg`**        | **2.9%**       | Bollette improvvisamente alte possono spingere all'abbandono.        |
| **`contract_renewal_reminder_sent`** | **0.4%**       | Ha un peso minore.                                                   |
| **`billing_method_encoded`**         | **0.0%**       | Nessun impatto rilevante nel dataset corrente.                       |
| **`has_online_account`**             | **0.0%**       | Nessun impatto rilevante nel dataset corrente.                       |
| **`service_type_encoded`**           | **0.0%**       | Nessun impatto rilevante nel dataset corrente.                       |

## Come Funziona la Previsione

1.  Il modello analizza i dati di ogni cliente in base a tutte le caratteristiche elencate sopra.
2.  Confronta questi dati con i pattern appresi durante l'addestramento.
3.  Calcola una **probabilità di churn** per ogni cliente.
4.  Vengono restituiti i clienti con una **probabilità superiore al 50%**.
5.  Un filtro esclude i clienti che hanno già un `contract_end_date` nel passato.

## Limitazioni e Considerazioni

*   **Dipendenza dai Dati**: Le eccellenti performance sono fortemente legate alla qualità e completezza delle feature di input. Se molte di queste informazioni non fossero disponibili, le performance calerebbero.
*   **Dataset Sintetico**: I risultati ottimali sono stati ottenuti con un dataset sintetico. E' fondamentale testare il modello su dati reali per confermarne l'efficacia.
*   **Soglia di Probabilità**: La soglia del 50% è configurabile e impatta direttamente sui risultati.
*   **Interpretazione**: L'elenco dettagliato delle feature importance consente una lettura approfondita delle motivazioni della predizione.

## Conclusione

Il modello avanzato identifica i clienti a rischio valutando una combinazione estremamente ricca di fattori:

1.  **Soddisfazione del Cliente**: Misurata direttamente con sondaggi.
2.  **Comportamento di Pagamento**: Ritardi e inadempienze sono indicatori forti.
3.  **Interazioni con il Supporto**: Un alto numero di contatti, specialmente lamentele, è critico.
4.  **Consumo Energetico**: Trend, volatilità e confronto con la media locale.
5.  **Aspetti Contrattuali**: Vicinanza alla scadenza, cambiamenti tariffari, promozioni.

Questa visione olistica lo rende uno strumento potente per il team di retention.