from flask import render_template, Flask
from negocio.pedido_negocio import NegocioPedido

app = Flask(__name__)

np = NegocioPedido()

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/pedido')
def pedido():
	pedidos = ns.todos()
	return render_template('pedido_list.html', data=pedidos)

@app.route('/pedido/new')
def pedido_new():
  return render_template('pedido_new.html')