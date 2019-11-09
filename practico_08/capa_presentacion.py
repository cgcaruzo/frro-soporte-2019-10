from flask import render_template, request, url_for, Flask
from practico_08.negocio.pedido_negocio import NegocioPedido
from practico_08.negocio.data.models.models import Pedido,Producto,Vehiculo,PedidoDetalle
from practico_08.negocio.producto_negocio import NegocioProducto
from practico_08.negocio.vehiculo_negocio import NegocioVehiculo
from practico_08.negocio.pedido_detalle_negocio import NegocioPedidoDetalle

app = Flask(__name__)

with app.app_context(), app.test_request_context():
	url_for('static', filename='jquery-3.3.1.slim.min.js')
	url_for('static', filename='popper.min.js')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/pedido/nuevo')
def pedido_nuevo():
	nprod = NegocioProducto()
	productos = nprod.todos()
	return render_template('pedido_nuevo.html', productos=productos)

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
	msg = None
	np = NegocioPedido()
	npd = NegocioPedidoDetalle()

	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				np.baja(i)
			msg = 'Pedido/s eliminado/s exitosamente'
		else:
			pedido = Pedido(direccion=request.form['direccion'], fecha_carga=request.form['fecha_carga'], fecha_entrega=request.form['fecha_entrega'])
			exito = np.alta(pedido)
			if exito is True:
				lista_product_id = request.form.getlist('producto_id')
				lista_cantidad = request.form.getlist('cantidad')
				for i in range(5):
					if lista_cantidad[i] != '':
						det = PedidoDetalle(pedido_id=pedido.id, producto_id=lista_product_id[i], cantidad=lista_cantidad[i])
						npd.alta(det)
				msg = 'Pedido creado exitosamente'
			elif exito is False:
				msg = 'No se pudo crear el pedido'
			else:
				msg = exito[0]

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
		elif 'id' in request.form:
			producto = Producto(id=request.form['id'], nombre=request.form['nombre'], marca=request.form['marca'], costo_kilo=request.form['costo_kilo'])
			nprod.modificacion(producto)
			msg = 'Producto actualizado exitosamente'
		else:
			producto = Producto(nombre=request.form['nombre'], marca=request.form['marca'], costo_kilo=request.form['costo_kilo'])
			nprod.alta(producto)
			msg = 'Producto creado exitosamente'

	productos = nprod.todos()
	return render_template('producto_list.html', productos=productos, msg=msg)

@app.route('/producto/nuevo')
def producto_nuevo():
	return render_template('producto_form.html')

@app.route('/producto/<int:id_producto>/editar')
def producto_editar(id_producto):
	nprod = NegocioProducto()
	producto = nprod.buscar(id_producto)
	return render_template('producto_form.html', producto=producto)

@app.route('/vehiculo', methods=['GET', 'POST'])
def vehiculo():
	msg = None
	nv = NegocioVehiculo()
	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				nv.baja(i)
				msg = 'Vehículo/s eliminado/s exitosamente'
		elif 'id' in request.form:
			vehiculo = Vehiculo(id=request.form['id'], nombre=request.form['nombre'], patente=request.form['patente'], capacidad=request.form['capacidad'])
			exito=nv.modificacion(vehiculo)
			if exito is True:
				msg = 'Vehiculo modificado exitosamente'
			elif exito is False:
				msg = 'No se pudo modificar el vehiculo'
			else:
				msg = exito[0]
		else:
			vehiculo = Vehiculo(nombre=request.form['nombre'], patente=request.form['patente'], capacidad=request.form['capacidad'])
			exito=nv.alta(vehiculo)
			if exito is True:
				msg = 'Vehiculo creado exitosamente'
			elif exito is False:
				msg = 'No se pudo crear el vehiculo'
			else:
				msg = exito[0]

	vehiculos = nv.todos()
	return render_template('vehiculo_list.html', vehiculos=vehiculos, msg=msg)

@app.route('/vehiculo/nuevo')
def vehiculo_nuevo():
	return render_template('vehiculo_form.html')

@app.route('/vehiculo/<int:id_vehiculo>/editar')
def vehiculo_editar(id_vehiculo):
	nv = NegocioVehiculo()
	vehiculo = nv.buscar(id_vehiculo)
	return render_template('vehiculo_form.html', vehiculo=vehiculo)
