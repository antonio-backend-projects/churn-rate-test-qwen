Perfetto, grazie per il link ufficiale.

Ho consultato il repository GitHub di Qwen Code e ho trovato le istruzioni ufficiali per l'installazione.&#x20;

---

### 🛠️ Procedura di installazione di Qwen Code

#### 1. **Prerequisiti**

Assicurati di avere **Node.js versione 20 o superiore** installato. Puoi verificarlo con:

```bash
node -v
```

Se non è installato o hai una versione inferiore, scaricalo e installalo da [nodejs.org](https://nodejs.org/).

#### 2. **Installazione tramite npm**

Il metodo consigliato è utilizzare npm (Node Package Manager):

```bash
npm install -g @qwen-code/qwen-code@latest
```

Dopo l'installazione, puoi verificare la versione di Qwen Code con:

```bash
qwen --version
```

#### 3. **Installazione da sorgente**

Se preferisci installare Qwen Code direttamente dal repository GitHub:

```bash
git clone https://github.com/QwenLM/qwen-code.git
cd qwen-code
npm install
npm install -g .
```

---

### 🚀 Avvio di Qwen Code

Per avviare Qwen Code, esegui:

```bash
qwen
```

Questo comando avvierà l'interfaccia a linea di comando di Qwen Code, dove potrai interagire con il sistema.

---

### ⚙️ Configurazione dell'API Key

Per utilizzare Qwen Code, è necessario configurare l'API Key. Puoi farlo in due modi:

* **Utilizzando variabili d'ambiente**: Crea un file `.env` nella directory principale del tuo progetto con il seguente contenuto:

  ```bash
  OPENAI_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  OPENAI_API_KEY=la_tua_api_key
  OPENAI_MODEL=qwen3-coder-plus
  ```

  Sostituisci `la_tua_api_key` con la tua chiave API personale.

* **Interattivamente**: Avvia Qwen Code senza variabili d'ambiente. Ti verrà chiesto di inserire l'API Key, l'URL di base e il nome del modello.

---

### ✅ Verifica dell'installazione

Dopo aver completato l'installazione e la configurazione, puoi testare Qwen Code con comandi come:

```bash
qwen
```

Esegui comandi come:

```bash
> Spiega questa struttura del codice
> Aiutami a rifattorizzare questa funzione
> Genera test unitari per questo modulo
```

---

Se desideri, posso aiutarti a creare uno script PowerShell che automatizza l'installazione e la configurazione di Qwen Code, inclusa la whitelist in Norton Antivirus. Fammi sapere se sei interessato!


Perfetto, ottimo lavoro! 🎉

Hai installato correttamente Qwen Code tramite npm, e la versione 0.0.5 è confermata con:

```powershell
qwen --version
```

---

Ora puoi iniziare a usarlo!

Ad esempio:

```powershell
qwen
```

Ti apre la CLI interattiva dove puoi scrivere comandi o chiedere aiuto su codice, come da documentazione.

---

Se vuoi configurare l’API key per usare i modelli, ti basta creare un file `.env` nella cartella da cui esegui `qwen` con:

```
OPENAI_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=la_tua_api_key
OPENAI_MODEL=qwen3-coder-plus
```

Oppure impostare queste variabili d’ambiente nel sistema.

---

Se vuoi ti aiuto a creare la configurazione, o a integrare Qwen Code nei tuoi workflow, o a fare whitelist Norton per evitare blocchi — dimmi pure!


Ottimo, sei dentro! 🎉

Qwen Code ti sta chiedendo come vuoi autenticarti per questo progetto:

* **1. Qwen OAuth**
* **2. OpenAI**

Se hai una API key OpenAI (o compatibile) puoi selezionare l’opzione 2 per usarla.
Altrimenti puoi provare l’OAuth Qwen, che è la modalità standard con Qwen.

---

### Come procedere ora:

* Premi **2** + Invio se vuoi usare OpenAI API key
* Ti chiederà di inserire la tua chiave API (la puoi trovare nel tuo account OpenAI o da altri servizi compatibili)
* Oppure scegli 1 per OAuth se hai un account Qwen e vuoi autorizzare via browser

---

### Consiglio:

Se non hai chiavi, o vuoi testare subito, scegli Qwen OAuth (1).
Se invece usi un servizio cloud (OpenAI, Alibaba, ecc.) e hai la API key, scegli OpenAI (2).

---

Se vuoi ti posso aiutare a configurare la API key in modo che Qwen la carichi automaticamente (via `.env` o variabili ambiente) così non te la chiede ogni volta.

Fammi sapere come preferisci andare avanti!


Perfetto, ecco i **trucchi da VIBE coder** per spremere Qwen Code al massimo senza rompere il flow:

---

## 🎯 1. Parti subito con `/new` e `/edit`

* **Creare file nuovi al volo**:

  ```bash
  /new scraper.py crea un semplice scraper con BeautifulSoup che salva titoli e link in CSV
  ```

  🔹 Qwen non ti scrive solo il codice, **ti crea direttamente il file** nella cartella corrente.

* **Modificare un file già esistente**:

  ```bash
  /edit utils.py aggiungi funzione parse_date che accetta formati multipli
  ```

  🔹 Qwen apre il file, legge il contenuto e applica la modifica **in contesto**, senza perdere quello che già hai.

---

## ⚡ 2. Prompt “full context”

Quando fai domande tecniche, Qwen vede **tutto il progetto** se sei nella cartella, quindi puoi chiedere:

```bash
/refactor rendi più veloce la funzione search_results
```

e lui sa dove e come intervenire.
Gemini CLI non ha questo accesso diretto ai file, devi incollare tu il codice.

---

## 🛠 3. Comando `/run` con feedback

Puoi **eseguire il codice** direttamente e chiedere correzioni se crasha:

```bash
/run scraper.py
```

Se c’è un errore, Qwen può leggerlo e patchare subito il file.

---

## 📚 4. File “QWEN.md” per settaggi di stile

Crea un file `QWEN.md` nella root del progetto con istruzioni tipo:

```
- Preferisci codice Python conciso
- Evita librerie esterne se non strettamente necessarie
- Scrivi sempre docstring dettagliate
```

Così ogni comando seguirà **il tuo vibe**.

---

## 🧠 5. Usa le slash command smart

* `/help` → guida rapida a tutti i comandi
* `/context` → mostra cosa Qwen sta leggendo
* `/history` → rivedi i comandi passati
* `/undo` → annulla l’ultima modifica

---

💡 Trucco extra:
Se Norton rompe, puoi avviare Qwen Code così:

```bash
npx qwen-code
```

Così gira senza usare l’eseguibile globale e Norton tende a non segnalare.

---

Vuoi che ti faccia **una mini cheat sheet grafica** di questi comandi per tenerla accanto mentre lavori? Sarebbe tipo una “VIBE coder Qwen Quick Ref” 😎

