from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "The bot should be working just fine. Try reopening discord if the bot doesnt respond or get better wifi noob."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
