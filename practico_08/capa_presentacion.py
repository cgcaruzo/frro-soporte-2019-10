from flask import render_template, request, url_for, Flask
from practico_08.negocio.pedido_negocio import NegocioPedido
from practico_08.negocio.data.models.pedido import Pedido
from practico_08.negocio.producto_negocio import NegocioProducto
from practico_08.negocio.data.models.producto import Producto

app = Flask(__name__)

with app.app_context(), app.test_request_context():
	url_for('static', filename='jquery-3.3.1.slim.min.js')
	url_for('static', filename='popper.min.js')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/pedido/new')
def pedido_new():
	nprod = NegocioProducto()
	productos = nprod.todos()
	return render_template('pedido_new.html', productos=productos)

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
	msg = None
	np = NegocioPedido()

	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				np.baja(i)
				msg = 'Pedido/s eliminado/s exitosamente'
		else:
			pedido = Pedido(direccion=request.form['direccion'], fecha_carga=request.form['fecha_carga'], fecha_entrega=request.form['fecha_entrega'])
			np.alta(pedido)
			msg = 'Pedido creado exitosamente'

	pedidos = np.todos()
	return render_template('pedido_list.html', pedidos=pedidos, msg=msg)

@app.route('/producto', methods=['GET', 'POST'])
def producto():
	msg = None
	nprod = NegocioProducto()
	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				nprod.baja(i)
				msg = 'Producto/s eliminado/s exitosamente'
		else:
			producto = Producto(nombre=request.form['nombre'], marca=request.form['marca'], costo_kilo=request.form['costo_kilo'])
			nprod.alta(producto)
			msg = 'Producto creado exitosamente'
	productos = nprod.todos()
	return render_template('producto_list.html', productos=productos, msg=msg)

@app.route('/producto/new')
def producto_new():
	return render_template('producto_new.html')