from flask import Flask, request, jsonify, abort
from models import Pessoa, Veiculo, session

app = Flask(__name__)

@app.route('/pessoa/<string:nome>', methods=['GET'])
def get_idade_pessoa(idade):
    '''
     Recebe o nome da Pessoa e retorna a idade da mesma.
    '''
    nome = nome.title()
    pessoa = session.query(Pessoa).filter_by(idade=idade).first()
    if pessoa:
        return jsonify({
            'idade': pessoa.idade
        })
    else:
        abort(404, description= 'Pessoa não encontrada!')



app.run(debug=True)