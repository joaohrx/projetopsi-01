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

    return render_template('dashboard.html')



@app.route('/logout')
def logout():
    global logado
    logado = False
    return redirect(url_for('login'))






if __name__ == "__main__":
    app.run(debug=True)

