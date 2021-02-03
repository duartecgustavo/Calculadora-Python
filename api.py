from flask import Flask, render_template, request
# Flask me auxiilia acriar um servidor em Python
# O render_template irá renderizar uma pagina a parte para mim

app = Flask(__name__, template_folder='src/views')
# Aqui eu chamo minha api '__main__' e atribuo ela a variavel 'app' com auxilio do Flask
# template_folder indica o caminho que sera executado o server

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form['num1'] != "" and request.form['num2'] != ""):
            num1 = request.form['num1']
            num2 = request.form['num2']

            if(request.form["opc"] == "soma"):
                soma = int(request.form['num1']) + int(request.form['num2'])
                return {"Resultado": str(soma)}

            elif(request.form["opc"] == "subt"):
                subtrair = int(request.form['num1']) - int(request.form['num2'])
                return {"Resultado": str(subtrair)}

            elif(request.form["opc"] == "mult"):
                multi = int(request.form['num1']) * int(request.form['num2'])
                return {"Resultado": str(multi)}

            else:
                divid = int(request.form['num1']) // int(request.form['num2'])
                return {"Resultado": str(divid)}
        else:
            return 'Informe um valor valido!'
    #     int(num1) = request.form['num1']
    #     int(num2) = request.form['num2']
    #     return num1 + num2
# Acima eu peguei essa minha variavel e adicionei a função 'route' e indiquei a rota
# Com o '@' eu digo que assim que eu abrir essa rota irá executar alguma coisa no caso a função 'home'

@app.route("/<id>")
# @app.route("/<int:id>")
def home_id(id):
    return id
# Capturando parametro

# @app.route('/', methods=['POST'])
# def post():
#     return 'POST'


@app.route('/sobre')
def sobre():
    return 'Sobre'


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')


app.run(port=8080, debug=True)
# poderia adicionar uma porta com o comando 'port=8080'