# QWEN.md — Operative Coding Guide for Qwen Code

## 🎯 Missione
Assistere nello sviluppo, debug e miglioramento del progetto **Churn Rate Calculator**, mantenendo codice pulito, commentato in italiano e pronto per l’analisi dati di churn (base + ML).

---

## 🚀 Quick Commands
Usa questi comandi rapidi con Qwen:
- `/refactor churn_calculator.py` → Migliora codice base mantenendo logica
- `/add_feature churn_calculator_ml.py trend_plot` → Aggiungi grafico trend churn mensile
- `/fix_error churn_calculator_ml.py` → Correggi errori e bug
- `/optimize churn_calculator_ml.py performance` → Velocizza analisi su grandi dataset
- `/write_tests churn_calculator.py pytest` → Genera test unitari

---

## 📂 Struttura File & Ruolo
- `churn_calculator.py` → Calcolo churn semplice, input minimo (customer_id, status)
- `churn_calculator_ml.py` → Analisi avanzata, ML, grafici e report
- `requirements.txt` → Librerie richieste
- `sample_customer_data.csv` → Dati esempio base
- `customer_data.csv` → Dati esempio avanzato

---

## 🛠️ Requisiti Tecnici
- **Python**: ≥ 3.7
- **Librerie**: pandas, scikit-learn, matplotlib, seaborn
- **Stile**: PEP8, commenti in italiano
- **Compatibilità**: Windows e Linux

---

## 📌 Checklist Sviluppo
Quando lavori sul progetto:
1. **Import chiari** (ordinati per libreria standard, terze parti, locali)
2. **Gestione errori**:
   - File non trovato
   - Colonne mancanti
   - CSV vuoto
3. **Validazione input**:
   - Tipi corretti (date, numeri, stringhe)
   - Conversione formati (es. date in datetime)
4. **Analisi ML**:
   - Algoritmo interpretabile (LogisticRegression o RandomForest)
   - Split train/test
   - Metriche: accuracy, precision, recall, f1-score
5. **Visualizzazioni**:
   - Grafici chiari, etichette leggibili
   - Salvataggio PNG e possibilità di mostrare a schermo
6. **Output**:
   - Risultati stampati in console
   - File CSV o TXT con report

---

## 🔍 Scenari di Debug
Se il codice:
- **Dà errore di colonna mancante** → Controlla intestazioni CSV
- **Grafico non appare** → Aggiungi `plt.show()` o salva il file
- **ML non converge** → Normalizza i dati o riduci feature
- **Esecuzione lenta** → Usa `pandas.read_csv(..., chunksize=...)`

---

## 💬 Esempi Prompt per Qwen
- `Ottimizza churn_calculator_ml.py per gestire 1M+ record`
- `Aggiungi validazione che blocca il calcolo se manca la colonna tenure_months`
- `Integra un grafico a barre con churn rate per service_type`
- `Scrivi un report PDF automatico con matplotlib e reportlab`
- `Genera test pytest per la funzione calculate_monthly_churn`

---

## 📝 Note Finali
Questo file è progettato per rendere Qwen un assistente di sviluppo **proattivo**:  
- Suggerisce miglioramenti
- Risolve bug
- Aggiunge nuove funzionalità
- Mantiene codice leggibile e commentato

