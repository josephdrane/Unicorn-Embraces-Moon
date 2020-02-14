import os

from flask import Flask, render_template

# Flask
app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 8001))
    app.run(host="0.0.0.0", port=port)
