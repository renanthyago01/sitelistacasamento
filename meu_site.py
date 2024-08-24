from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Lista de produtos com imagens
produtos = [
    {"id": 1, "nome": "Geladeira", "disponivel": True, "imagem": "https://electrolux.vtexassets.com/arquivos/ids/202734/Refrigerator_TF56_Electrolux_Detalhe2.jpg?v=637379383634970000"},
    {"id": 2, "nome": "Mangueira", "disponivel": True, "imagem": "https://atacadodolojista.vtexassets.com/arquivos/ids/188937/Mangueira-de-Jardim-10m-Quality-Verde.jpg?v=638393655956270000"},
    {"id": 3, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 4, "nome": "Jogo de cama", "disponivel": True, "imagem": "https://3a36cfaa62ac8ba9.cdn.gocache.net/images/produtos/mix_grafite_jogo_2021_1_20210331__g.jpg"},
    {"id": 5, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 6, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 7, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 8, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 9, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 10, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 11, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 12, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 13, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 14, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 15, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 16, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 17, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 18, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 19, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 20, "nome": "Panela de arroz", "disponivel": True, "imagem": "https://t62533.vteximg.com.br/arquivos/ids/942876-1000-1000/PE42.jpg?v=638265785854000000"},
    {"id": 21, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 22, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 23, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 24, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 25, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 26, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 27, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},
    {"id": 28, "nome": "Panela de arroz", "disponivel": True, "imagem": ""},

]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/selecionar_produto', methods=['POST'])
def selecionar_produto():
    produto_id = request.json.get('id')
    for produto in produtos:
        if produto['id'] == produto_id:
            produto['disponivel'] = False
            break
    return jsonify({"status": "success", "produto_id": produto_id})

#if __name__ == '__main__':
 #   app.run(debug=True)