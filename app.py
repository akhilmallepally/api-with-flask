from flask import Flask, jsonify           # import flask

app = Flask(__name__)             # create an app instance by using Flask constructor

books = [{"id":1,"name":"hello","writer":"me"}]
books = [{"id":2,"name":"raser","writer":"him"}]

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
        # on running python app.py # run the flask app

@app.route("/akhil/books")
def get_books():
    return jsonify({"books": books})

@app.route("/akhil/books/<int:book_id>", methods = ['GET'])
def get_book(book_id):
    return jsonify({"books": books})

    
if __name__ == "__main__":
    app.run()