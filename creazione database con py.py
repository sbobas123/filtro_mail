import sqlite3

# Crea il database e la tabella
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS registered_emails (
    email TEXT PRIMARY KEY
)
""")
# Inserisci alcune email di prova
emails = [
    ("mario.rossi@azienda1.com",),
    ("luigi.bianchi@azienda1.com",),
    ("admin@azienda1.com",)
]
cursor.executemany("INSERT OR IGNORE INTO registered_emails (email) VALUES (?)", emails)
conn.commit()
conn.close()

print("Database creato e popolato con email di esempio.")
