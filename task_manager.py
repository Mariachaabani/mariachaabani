from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route pour afficher la liste des tâches
@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route pour ajouter une tâche
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']

        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (name, description, due_date, priority) VALUES (?, ?, ?, ?)', 
                       (name, description, due_date, priority))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Route pour supprimer une tâche
@app.route('/delete_task/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route pour modifier une tâche
@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']

        cursor.execute('''
            UPDATE tasks
            SET name = ?, description = ?, due_date = ?, priority = ?
            WHERE id = ?
        ''', (name, description, due_date, priority, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()

    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
