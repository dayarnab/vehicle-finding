from flask import Flask, render_template,request
import csv

app = Flask(__name__,template_folder = 'templates')
@app.route('/')
def index():
    return render_template('input-form.html')

@app.route('/', methods=['POST','GET'])
def getvalue():
    zipc= request.form['zipcode']
    dist= request.form['distance']
    fieldnames=['zipcode','distance']
    with open('data.csv','w') as inFile:
        writer= csv.DictWriter(inFile,fieldnames=fieldnames)
        writer.writerow({'zipcode':zipc,'distance':dist})
    return "Your entered values are"+ zipc +" "+dist
    


if __name__ == "__main__":
    app.run(host="localhost",debug=True)



