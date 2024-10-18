from flask import Flask, render_template, request, send_file, redirect, url_for
from waitress import serve
import subprocess

app = Flask(__name__)

@app.route("/documentation")
def error_page():
    return render_template("help.html")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/run_app')
def run_app():
    try:
        subprocess.Popen(["python", "main.py"])
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error running the app: {str(e)}"
    

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)