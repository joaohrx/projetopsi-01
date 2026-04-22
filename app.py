from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template ('cadastro.html')


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
