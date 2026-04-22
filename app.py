from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        data_de_nascimento = request.form.get('data_de_nascimento')

        if not nome or not email or not senha:
            return redirect(url_for('cadastro'))
        
        return redirect(url_for('login')) 

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if nome and senha:
            return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/area_livros')
def area_livros():


    return render_template('area_livros.html')


@app.route('/carrinho')
def carrinho():
    
    return render_template('carrinho.html')

if __name__ == "__main__":
    app.run(debug=True)
