from flask import Flask, request, render_template

app = Flask(__name__)
messages_list = []



def add_message(name, text):
    new_message = {
        "name": name,
        "text": text,
        "time": "28:69",
    }
    messages_list.append(new_message)


add_message("Mike", "Welcome to Chat")


@app.route("/")
def hello():
    return "Hello, welcome to PythonMessenger2000"


# 1. Display all chat messages: JSON
@app.route("/get_messages")
def get_messages():
    return {"messages": messages_list}


# 2. Ability to sent new messages
# HTTP GET
# http://127.0.0.1:5000/send_message?name=Mike&text=Hello
@app.route("/send_message")
def send_message():
    name = request.args.get("name")
    text = request.args.get("text")
    add_message(name, text)
    return "OK"


# 3. UI for messenger
@app.route("/chat")
def display_chat():
    return render_template("chat.html")

app.run()