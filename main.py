from flask import Flask, jsonify, request, Response
from data import Funcionario

app = Flask(__name__)
funcionario = Funcionario()



@app.route('/empregados')
def get_empregados():
    return jsonify({'empregados': funcionario.empregados})

@app.route('/empregados/<id>')
def get_empregados_by_id(id):
    out_empregados = []
    for empregado in funcionario.empregados:
        if id == empregado['_id']:
            out_empregados.append(empregado)
            return jsonify(out_empregados)

@app.route('/empregados/cargo/<cargo>')
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in funcionario.empregados:
        if cargo == empregado['cargo']:
            out_empregados.append(empregado)
    return jsonify(out_empregados)


@app.route('/empregados/<info>/<value>')
def get_empregado_info(info, value):
    out_empregados = []
    for empregado in funcionario.empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)

            if type(value_empregado == int):
                if int(value) == value_empregado:
                    out_empregados.append(empregado)

    return jsonify({'empregados': out_empregados})


@app.route('/informations', methods=['POST'])
def get_empregado_post():

    username = request.form['username']
    secret = request.form['secret']

    if not check_user(username, secret):
        return Response('Unauthorized', status=401)

    info = request.form['info']
    value = request.form['value']

    out_empregados = []
    for empregado in funcionario.empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)

            if type(value_empregado == int):
                if int(value) == value_empregado:
                    out_empregados.append(empregado)

    return jsonify({'empregados': out_empregados})


def check_user(username, secret):
    for user in funcionario.users:
        if user['username'] == username and user['secret'] == secret:
            return True
        return False



if(__name__ == '__main__'):
    app.run(debug=True)