import sqlite3

def filter_emails(input_file, output_file, internal_file, db_file):
    # Dominio aziendale permesso
    company_domain = "@azienda1.com"
    
    # Lista di domini di email pubbliche da filtrare
    public_domains = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@libero.it", "@alice.it", "@virgilio.it"
    ]
    
    # Connessione al database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Funzione per verificare se l'email è nel database
    def email_in_database(email):
        cursor.execute("SELECT 1 FROM registered_emails WHERE email = ?", (email,))
        return cursor.fetchone() is not None

    # Apri i file di input e output
    with open(input_file, "r") as infile, \
         open(output_file, "w") as outfile, \
         open(internal_file, "w") as internal_outfile:

        for line in infile:
            email = line.strip().lower()
            # Controlla se l'email appartiene al dominio aziendale
            if email.endswith(company_domain):
                # Verifica se l'email è registrata nel database
                if email_in_database(email):
                    outfile.write(email + "\n")
                else:
                    internal_outfile.write(email + "\n")
            # Filtra le email pubbliche
            elif any(public_domain in email for public_domain in public_domains):
                continue

    # Chiudi la connessione al database
    conn.close()

# Richiedi all'utente i nomi dei file
input_file = input("Inserisci il nome del file di input (es. emails.txt): ")
output_file = input("Inserisci il nome del file di output (es. filtered_emails.txt): ")
internal_file = "interne_non_registrate.txt"
db_file = input("Inserisci il nome del database SQLite (es. emails.db): ")

# Esegui la funzione di filtraggio
filter_emails(input_file, output_file, internal_file, db_file)

print(f"Filtraggio completato. Controlla i file '{output_file}' e '{internal_file}'.")
