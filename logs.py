from flask import Flask
from src.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("we are testing our logging file")
    return "Hello World"

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
