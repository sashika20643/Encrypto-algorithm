from urllib import response
from flask import Flask, render_template, request,jsonify


app = Flask(__name__)

@app.after_request
def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
@app.route('/test/', methods=['GET','POST'])
def test():
     clicked=None
     if request.method == "POST":
          clicked=request.get_json(force=True) 
          return clicked['data']

if __name__ == '__main__':
   app.run(debug = True)
