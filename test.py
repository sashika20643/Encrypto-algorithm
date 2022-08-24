from flask import Flask, render_template, request

app = Flask(__name__)

	
@app.route('/', methods = ['GET', 'POST'])

def upload_file():
   if request.method == 'POST':
         print(request.json)
         return("done")
if __name__ == '__main__':
   app.run(debug = True)
