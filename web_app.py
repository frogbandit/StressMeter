from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("home.html")

if __name__ == "__main__":
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.bind(('localhost', 0))
   port = sock.getsockname()[1]
   sock.close()
   app.run(debug=True, host='0.0.0.0', port=port)

