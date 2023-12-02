from flask import Flask, render_template, request
from helpers import todo
import spacy

 
app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0
 
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
        
        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']
 
        if title == '':
            return render_template("create-todo.html")
 
        new_todo: todo = todo(todo_count, title, description, color)
        todo_list.append(new_todo)
 
        todo_count += 1
 
        return render_template("success.html", title=title, description=description)
    return render_template("create-todo.html")


@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)

nlp = spacy.load("chatbot_model")

@app.route('/chat')
def home():
    return render_template('index2.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    doc = nlp(user_input)

    bot_response = "I'm a simple chatbot, and I don't understand much yet!"

    return render_template('index2.html', user_input=user_input, bot_response=bot_response)


if __name__ == '__main__':
    app.run(debug=True)