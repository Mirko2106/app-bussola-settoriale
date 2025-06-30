Appunti importanti:



requirements.txt è la lista di librerie 
Chi scarica il tuo progetto può eseguire:
pip install -r requirements.txt
E in pochi secondi ha tutte le librerie necessarie.




nella cartella data è presente il foglio last_update: 
quest'ultimo presenterà l'ultima data nella quale sono stati effettuati gli append dei dati
questo per non sovraccaricare le richieste a yahoo finance


@st.cache_data
def get_etf_data(ticker: str) -> pd.DataFrame:
Questa è una funzione con cache: se richiami get_etf_data("XLF") più volte, 
il risultato viene memorizzato nella RAM di Streamlit per evitare di rileggere da disco.









