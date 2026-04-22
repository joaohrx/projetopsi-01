from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():


    nome= request.form.get('nome')
    email=request.form.get('email')
    senha=request.form.get('senha')
    telefone=request.form.get('telefone')
    endereco=request.form.get('endereco')
    data_de_nascimento=request.form.get('data_de_nascimento')





    return render_template ('cadastro.html',nome=nome,email=email,senha=senha,telefone=telefone,endereco=endereco,data_de_nascimento=data_de_nascimento)


@app.route('/login')
def login():


    return render_template('login.html')


@app.route('/area_livros')
def area_livros():


    return render_template('area_livros.html')


@app.route('/carrinho')
def carrinho():
    
    return render_template('carrinho.html')

if __name__ == "__main__":
    app.run(debug=True)
