from flask import Flask, render_template, request, jsonify
from passwordGenerator import password_generator


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/password",methods=["POST"])
def password():
    try:
        symbols = True if request.form["symbols"] == "true" else False
    except:
        symbols = False
    try:
        length = int(request.form["length"])
        if length > 20:
            length = 20
        elif length < 8:
            length = 8
    except:
        length = 8
    password = password_generator(length,symbols)
    data = {"password":password}
    return jsonify(data)


if __name__ == "__main__":
    app.run()