# Changelog

Tutte le modifiche importanti a questo progetto saranno documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e questo progetto aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Aggiunto supporto per il modello XGBoost in `churn_calculator_ml.py`.
- Aggiunto supporto per il modello Logistic Regression in `churn_calculator_ml.py`.
- Aggiunta funzionalità di confronto delle performance tra diversi modelli ML.
- Creato script `generate_advanced_customer_data.py` per generare un dataset con nuove features avanzate.
- Aggiunto file `CHANGELOG.md` per tracciare le modifiche al progetto.

### Changed
- Aggiornata la documentazione in `RIASSUNTO_PROGETTO.md` per riflettere l'aggiunta di nuovi modelli e il piano di miglioramento.
- Aggiornata la documentazione in `MODELLO_DECISIONALE.md` con l'importanza delle features per il modello Logistic Regression.
- Aggiornata la documentazione in `NEXT_STEPS.md` con dettagli su come implementare XGBoost e Logistic Regression.
- Aggiornata la documentazione in `SCRIPTS.md` con la descrizione dei nuovi modelli e dello script `generate_advanced_customer_data.py`.
- Aggiornato `README.md` con informazioni sui nuovi modelli e sul nuovo dataset `customer_data_advanced.csv`.

### Fixed
- Corretto un bug nella funzione `predict_churn` che non gestiva correttamente i modelli diversi da RandomForest.
