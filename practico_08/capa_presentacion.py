from flask import render_template, request, url_for, Flask
from datetime import datetime
from practico_08.negocio.pedido_negocio import NegocioPedido
from practico_08.negocio.data.models.models import Pedido,Producto,Vehiculo,PedidoDetalle
from practico_08.negocio.producto_negocio import NegocioProducto
from practico_08.negocio.vehiculo_negocio import NegocioVehiculo
from practico_08.negocio.pedido_detalle_negocio import NegocioPedidoDetalle
from practico_08.simulacion import Simulacion

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
	return render_template('pedido_form.html', productos=productos, datetime=datetime)

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
	msg = None
	alert = None
	np = NegocioPedido()
	npd = NegocioPedidoDetalle()

	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				np.baja(i)
			msg = 'Pedido/s eliminado/s exitosamente'
			alert = 'success'
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
				alert = 'success'
			elif exito is False:
				msg = 'No se pudo crear el pedido'
				alert = 'danger'
			else:
				msg = exito[0]
				alert = 'warning'

	pedidos = np.todos()
	return render_template('pedido_list.html', pedidos=pedidos, msg=msg, alert=alert)

@app.route('/pedido/<int:id_pedido>/ver')
def pedido_ver(id_pedido):
	np = NegocioPedido()
	pedido = np.buscar(id_pedido)
	print(pedido)
	npd = NegocioPedidoDetalle()
	detalles = npd.buscar_pedido(id_pedido)
	nprod = NegocioProducto()
	productos = nprod.todos()
	return render_template('pedido_form.html', pedido=pedido, detalles=detalles, productos=productos, datetime=datetime)

@app.route('/pedido/planificacion')
def pedido_planificacion():
	msg = None
	alert = None
	np = NegocioPedido()
	rows = np.group_fecha_entrega()
	pedidos = {}
	for row in rows:
		pedidos[row.fecha_entrega] = np.buscar_fecha_entrega(row.fecha_entrega)
	return render_template('pedido_planificacion.html', rows=rows, pedidos=pedidos, msg=msg, alert=alert, datetime=datetime)

@app.route('/producto', methods=['GET', 'POST'])
def producto():
	msg = None
	alert = None
	nprod = NegocioProducto()
	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				nprod.baja(i)
			msg = 'Producto/s eliminado/s exitosamente'
			alert = 'success'
		elif 'id' in request.form:
			producto = Producto(id=request.form['id'], nombre=request.form['nombre'], marca=request.form['marca'], costo_unitario=request.form['costo_unitario'])
			nprod.modificacion(producto)
			msg = 'Producto actualizado exitosamente'
			alert = 'success'
		else:
			producto = Producto(nombre=request.form['nombre'], marca=request.form['marca'], costo_unitario=request.form['costo_unitario'])
			nprod.alta(producto)
			msg = 'Producto creado exitosamente'
			alert = 'success'

	productos = nprod.todos()
	return render_template('producto_list.html', productos=productos, msg=msg, alert=alert)

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
	alert = None
	nv = NegocioVehiculo()
	if request.method == 'POST':
		if request.form.getlist('borrar'):
			lista= request.form.getlist('borrar')
			for i in lista:
				nv.baja(i)
				msg = 'Vehículo/s eliminado/s exitosamente'
				alert = 'success'
		elif 'id' in request.form:
			vehiculo = Vehiculo(id=request.form['id'], nombre=request.form['nombre'], patente=request.form['patente'], capacidad=request.form['capacidad'])
			exito=nv.modificacion(vehiculo)
			if exito is True:
				msg = 'Vehiculo modificado exitosamente'
				alert = 'success'
			elif exito is False:
				msg = 'No se pudo modificar el vehiculo'
				alert = 'danger'
			else:
				msg = exito[0]
				alert = 'warning'
		else:
			vehiculo = Vehiculo(nombre=request.form['nombre'], patente=request.form['patente'], capacidad=request.form['capacidad'])
			exito=nv.alta(vehiculo)
			if exito is True:
				msg = 'Vehiculo creado exitosamente'
				alert = 'danger'
			elif exito is False:
				msg = 'No se pudo crear el vehiculo'
				alert = 'success'
			else:
				msg = exito[0]
				alert = 'warning'

	vehiculos = nv.todos()
	return render_template('vehiculo_list.html', vehiculos=vehiculos, msg=msg, alert=alert)

@app.route('/vehiculo/nuevo')
def vehiculo_nuevo():
	return render_template('vehiculo_form.html')

@app.route('/vehiculo/<int:id_vehiculo>/editar')
def vehiculo_editar(id_vehiculo):
	nv = NegocioVehiculo()
	vehiculo = nv.buscar(id_vehiculo)
	return render_template('vehiculo_form.html', vehiculo=vehiculo)

@app.route('/simular/<string:fecha_entrega>')
def simular(fecha_entrega):
	nv = NegocioVehiculo()
	vehiculos = nv.todos()
	np = NegocioPedido()
	pedidos = np.buscar_fecha_entrega(fecha_entrega)
	simulacion = Simulacion(pedidos, vehiculos)
	return render_template('simulacion.html', simulacion=simulacion, vehiculos=vehiculos)
