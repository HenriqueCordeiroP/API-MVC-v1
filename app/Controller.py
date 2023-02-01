from flask import Flask, request, jsonify
from View import ApiEndpoints

app = Flask(__name__)
view = ApiEndpoints()

@app.route("/")
def index():
    return "/books"

@app.route("/books", methods=['GET'])
def get():
    return view.read(), 200

@app.route("/books", methods=['POST'])
def post():
    book = request.get_json()
    print("AAAAAAA ", book)
    if not book:
        return default_error_handler("Missing Parameters.", 400)
    return view.create(book), 200

@app.route("/books/<int:id>", methods=['PUT','PATCH'])
def patch(id):
    updated_book = request.get_json()

    return view.update_method(id, updated_book), 200

    ## I treated this as an error, but it is not an acctual error
    ## So I removed it.
    # if not updated_book in view.book_list:
    #     return default_error_handler("Book not in book list.", 400)

@app.route("/books/<int:id>", methods=['DELETE'])
def delete(id):
    # if not id in view.book_list:
    #     return default_error_handler("Book not in book list.", 400)
    return view.delete(id), 200

@app.errorhandler(404)
def handler_404(_error):
    return jsonify({"Error 404": "Page not found."}), 404

@app.errorhandler(400)
def handler_400(_error):
    return jsonify({"Error 400":"Bad Request"})

@app.errorhandler(405)
def handler_405(_error):
    return jsonify({"Error 405":"Method Not Allowed"})

def default_error_handler(message, err):
    return f"Error {err}: {message}", err

app.run(debug=True)