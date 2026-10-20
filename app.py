#  postman - teste http --> verificar respostas da API
# 1. OBJETIVO
# 2. URLBASE
# 3. ENDPOINTS
# 4. RECURSOS DISPONIBILIZADOS

# VAMOS CRIAR UMA API:
"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "O Senhor dos aneis", "autor": "J.R.R.TOLKIEN"},
    {"id": 2, "titulo": "A revolução dos bichos", "autor": "George Orwell"},
    {"id": 3, "titulo": "A hipotese do amor", "autor": "Ali Hazelwood"},
    {"id": 4, "titulo": "O Anticristo", "autor": "Friedrich Nietzsche"},
    {"id": 5, "titulo": "1984", "autor": "George Orwell"},
    {"id": 6, "titulo": "O Alquimista", "autor": "Paulo Coelho"},
    {"id": 7, "titulo": "Dom Casmurro", "autor":  "Machado de Assis"},
    {"id": 8, "titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez"},
    {"id": 9, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 10, "titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski"},
]

# 1. CONSULTAR TODOS OS LIVROS
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

# 2. CONSULTAR LIVRO POR ID
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"message": "LIVRO NÃO ENCONTRADO!"}), 404

#PUT --> primeiro, os dados enviados pelo cliente
#serão obtidos
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    #permite acessar os dados json enviados no corpo
    #da requisição
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])

@app.route("/livros", methods = ["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Delete - excluir um livro
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    # Como é necessário excluir um elemento da lista pelo seu indice, será utilizado novamente o enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)

# INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(host="localhost", port=6767, debug=True)