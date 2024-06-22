from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

# Sample todo list
todos = [{"task": "Sample Todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    todo_task = request.form.get("todo")
    if todo_task:
        todos.append({"task": todo_task, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:todo_index>", methods=["GET", "POST"])
def edit_todo(todo_index):
    if 0 <= todo_index < len(todos):
        todo = todos[todo_index]
        if request.method == "POST":
            todo_task = request.form.get("todo")
            if todo_task:
                todos[todo_index]["task"] = todo_task
            return redirect(url_for('index'))
        return render_template("edit.html", todo=todo, index=todo_index)
    return redirect(url_for("index"))

@app.route("/check/<int:todo_index>")
def check_todo(todo_index):
    if 0 <= todo_index < len(todos):
        todos[todo_index]['done'] = not todos[todo_index]['done']
    return redirect(url_for('index'))

@app.route("/delete/<int:todo_index>")
def delete_todo(todo_index):
    if 0 <= todo_index < len(todos):
        del todos[todo_index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
