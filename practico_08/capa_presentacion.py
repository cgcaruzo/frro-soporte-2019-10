from flask import render_template, request, url_for, Flask
from practico_08.negocio.pedido_negocio import NegocioPedido
from practico_08.negocio.data.models.pedido import Pedido

app = Flask(__name__)

with app.app_context(), app.test_request_context():
	url_for('static', filename='jquery-3.3.1.slim.min.js')
	url_for('static', filename='popper.min.js')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/pedido/new')
def pedido_new():
	return render_template('pedido_new.html')

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
	msg = None
	np = NegocioPedido()

	if request.method == 'POST':
		pedido = Pedido(direccion=request.form['direccion'], fecha_carga=request.form['fecha_carga'], fecha_entrega=request.form['fecha_entrega'])
		np.alta(pedido)
		msg = 'Pedido creado'

	pedidos = np.todos()
	return render_template('pedido_list.html', pedidos=pedidos, msg=msg)

@app.route('/pedido/baja', methods=['GET', 'POST'])
def pedido_baja():
	if request.method == 'POST':
		np = NegocioPedido()
		lista= request.form.getlist('borrar')
		for i in lista:
			np.baja(i)
	return render_template('pedido_baja.html')

