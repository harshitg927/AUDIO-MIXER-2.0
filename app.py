from flask import Flask, render_template, request
import os 
import subprocess

app = Flask(__name__)





@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        os.subprocess('python main.py')        
    return render_template("index.html")

@app.route('/my-link/', methods=['POST', 'GET'])
def my_link():
    bg = request.form['background_music']
    vocals = request.form['vocals']

    print(vocals)
    print(bg)    

    return render_template("lastpage.html")
if __name__ == '__main__':
    app.run(debug=True)

