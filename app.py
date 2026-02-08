from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Apple DevSecOps Demo</h1><p>Sistema Operacional: Funcionando!</p>"

# Esta rota simula uma falha de segurança (XSS - Cross Site Scripting)
# Um scanner de segurança deve pegar isso depois.
@app.route('/echo')
def echo():
    user_input = request.args.get('msg', '')
    # ERRO DE SEGURANÇA: Retornando input do usuário sem filtrar!
    return f"Você disse: {user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)