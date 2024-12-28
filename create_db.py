import sqlite3

# Connexion à la base de données (elle sera créée si elle n'existe pas)
conn = sqlite3.connect('tasks.db')

# Création de la table tasks
conn.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    due_date TEXT,
    priority TEXT
);
''')

print("Base de données et table créées avec succès!")

# Fermeture de la connexion
conn.close()
