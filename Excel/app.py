from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db.init_app(app)


class Responsavel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    matricula = db.Column(db.String(10))
    cpf = db.Column(db.String(11))

    def __init__(self, nome, email, telefone, matricula, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.matricula = matricula
        self.cpf = cpf


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    matricula = db.Column(db.String(10))
    cpf_r = db.Column(db.String(11))

    def __init__(self, nome, email, telefone, matricula, cpf_r):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.matricula = matricula
        self.cpf_r = cpf_r


class Boletim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_Aluno = db.Column(db.String(200))
    nome_Responsavel = db.Column(db.String(200))
    matricula = db.Column(db.String(10))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # renders an html file
    return render_template('index.html')


@app.route('/form/responsavel', methods=['POST', 'GET'])
def form_responsavel():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('tel')
        matricula = request.form.get('matr')
        cpf = request.form.get('cpf')

        bot = Responsavel(nome, email, telefone, matricula, cpf)
        db.session.add(bot)
        db.session.commit()

    return render_template('formsR.html')


@app.route('/form/aluno', methods=['POST', 'GET'])
def form_aluno():
    if request.method == 'POST':
        nome = request.form.get('noA')
        email = request.form.get('emailA')
        telefone = request.form.get('telA')
        matricula = request.form.get('matrA')
        cpf_r = request.form.get('cpf_r')

        bot = Aluno(nome, email, telefone, matricula, cpf_r)
        db.session.add(bot)
        db.session.commit()

    return render_template('formsA.html')


@app.route('/boletim')
def bolet():

    # return render_template('boletim.html', blet=Responsavel.query.first())
    return render_template('boletim.html')


# runs the file
if __name__ == "__main__":
    app.run(debug=True)
