from flask import Flask, render_template,request,redirect,url_for, session

app = Flask(__name__)
app.secret_key = "1234"

usuarios = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
     

        if not nome or not email or not senha:
            return redirect(url_for('cadastro'))
        
        usuarios.append({
            "nome":nome,
            "email": email,
            "senha": senha
        })
        
        return redirect(url_for('login')) 

    return render_template('cadastro.html')



@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')

        for usuario in usuarios:

            if usuario["email"] == email and usuario["senha"] == senha:

                session['logado'] = True
                session['usuario'] = usuario["nome"]

                return redirect(url_for('dashboard'))

        return redirect(url_for('cadastro'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if not session.get('logado'):
        return redirect(url_for('login'))

    return render_template('area_livros.html',usuario=session.get('usuario'))



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/sobrenos')
def sobrenos():
    return render_template('sobre_nos.html')

@app.route('/compra1')
def compra1():
    return render_template('compra1.html')

@app.route('/compra2')
def compra2():
    return render_template('compra2.html')

@app.route('/compra3')
def compra3():
    return render_template('compra3.html')

@app.route('/compra4')
def compra4():
    return render_template('compra4.html')

@app.route('/compra5')
def compra5():
    return render_template('compra5.html')

@app.route('/compra6')
def compra6():
    return render_template('compra6.html')

@app.route('/compra7')
def compra7():
    return render_template('compra7.html')

@app.route('/compra8')
def compra8():
    return render_template('compra8.html')

@app.route('/descricao1')
def desc1():
    return render_template('desc1.html')

@app.route('/descricao2')
def desc2():
    return render_template('desc2.html')

@app.route('/descricao3')
def desc3():
    return render_template('desc3.html')

@app.route('/descricao4')
def desc4():
    return render_template('desc4.html')

@app.route('/descricao5')
def desc5():
    return render_template('desc5.html')

@app.route('/descricao6')
def desc6():
    return render_template('desc6.html')

@app.route('/descricao7')
def desc7():
    return render_template('desc7.html')

@app.route('/descricao8')
def desc8():
    return render_template('desc8.html')




if __name__ == "__main__":
    app.run(debug=True)

