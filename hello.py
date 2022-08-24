from flask import Flask, render_template, request,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aed'
 
mysql = MySQL(app)
	
@app.route('/', methods = [ 'GET', 'POST'])

def upload_file():
        user_name="u01"
        first_name = "file1"
        final_name = "enc001"
        size="25mb"
        type="img"
        password="Csmskjs"
        link="jndjdjbbcjbchjbc.com"
        
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO files (user_name,first_name,final_name,size,type,password,link) VALUES(%s,%s,%s,%s,%s,%s,%s)''',(user_name,first_name,final_name,size,type,password,link))
        mysql.connection.commit()
        cursor.close()
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
if __name__ == '__main__':
   app.run(debug = True)
