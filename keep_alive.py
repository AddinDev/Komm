from flask import Flask
from threading import Thread

app = Flask('')

html = """
<h1>Komm</h1>
<p>hehe</p>
"""

@app.route('/')
def home():
    return html

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()