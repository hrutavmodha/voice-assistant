from flask import Flask, render_template, request, jsonify
from backend.model.main import main 
import webbrowser as web
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/process", methods = ["POST"])
def process():
    data = request.json
    cmd = data["command"]
    res = main(cmd)
    if res == "":
        res = "Command executed successfully. Please wait a while to see changes on your monitor."
    return jsonify({
        "status": "success", 
        "message": res
    })
if __name__ == "__main__":
    print(" * Opening browser...")
    web.open("http://localhost:3000")
    print(" * Initializing server")
    app.run(debug = True, host = "localhost", port = 3000)