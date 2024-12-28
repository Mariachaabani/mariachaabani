import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('tasks.db')  # Assurez-vous que le chemin vers 'tasks.db' est correct
cursor = conn.cursor()

# Ajouter les nouvelles colonnes si elles n'existent pas déjà
try:
    cursor.execute('ALTER TABLE tasks ADD COLUMN due_date TEXT')
    cursor.execute('ALTER TABLE tasks ADD COLUMN priority TEXT')
    conn.commit()
    print("Colonnes 'due_date' et 'priority' ajoutées avec succès!")
except sqlite3.OperationalError as e:
    print(f"Erreur: {e}")

# Fermeture de la connexion
conn.close()
