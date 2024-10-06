# Usa un'immagine di base
FROM python:3.10

# Imposta la cartella di lavoro
WORKDIR /app

# Copia i file di requisiti e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dell'applicazione
COPY . .

# Espone la porta 5000
EXPOSE 5000

# Comando per avviare l'app
CMD ["python", "app.py"]
