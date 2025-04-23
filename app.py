from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []  # Stores list of task strings

@app.route('/')
def index():
    return render_template('index.html', tasks=enumerate(tasks))  # sends task with index

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
