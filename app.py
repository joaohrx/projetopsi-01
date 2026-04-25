from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

logado = False


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
        
        return redirect(url_for('login')) 

    return render_template('cadastro.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    global logado

    if request.method == 'POST':
        nome = request.form.get('nome')
        email= request.form.get('email')
        senha = request.form.get('senha')

        if nome and email and senha:
            logado = True
            return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if not logado:
        return redirect(url_for('login'))

    return render_template('area_livros.html')



@app.route('/logout')
def logout():
    global logado
    logado = False
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








if __name__ == "__main__":
    app.run(debug=True)

