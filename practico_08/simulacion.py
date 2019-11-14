import random
import math
import simpy


SEMILLA = 42
T_ENTREGAS = 30  # Number of machines in the carwash
WASHTIME = 5      # Minutes it takes to clean a car
T_INTER = 7       # Create a car every ~7 minutes
SIM_TIME = 20     # Simulation time in minutes

class Simulacion(object):
	def __init__(self, pedidos, vehiculos):
		# print("SIMULANDO")
		random.seed(random.random())
		self.env = simpy.Environment()
		self.pedidos = pedidos
		self.cant_pedidos = len(pedidos)
		self.vehiculos = vehiculos
		self.te  = 0.0 # tiempo de espera total
		self.dt  = 0.0 # duracion de servicio total
		self.fin = 0.0 # minuto en el que finaliza
		self.upi = 0.0 # minuto en el que finaliza
		self.vehiculos = simpy.Resource(self.env, len(vehiculos)) #Crea los recursos (vehiculos)
		self.cant_vehiculos = len(vehiculos)
		self.env.process(self.iniciar())
		self.env.run()
		#self.capacidad = simpy.Container(env, GAS_STATION_SIZE, init=GAS_STATION_SIZE)

	def iniciar(self):
		llegada = 0
		i = 0
		# print("COMIENZA SIMULACION")
		for i in range(self.cant_pedidos):
			# R = random.random()
			# tiempo_entrega = -T_ENTREGAS * math.log(R)
			# yield self.env.timeout(tiempo_entrega)
			i += 1
			yield self.env.process(self.entrega())
		print(self.dt, self.fin, self.cant_vehiculos)
		self.upi = round((self.dt / self.fin) / self.cant_vehiculos,2)

	def entrega(self):
		# print("ENTREGA")
		llega = self.env.now
		# print(llega)
		with self.vehiculos.request() as request:
			yield request
			R = random.random()
			tiempo_entrega = -T_ENTREGAS * math.log(R)
			self.dt = self.dt + llega + tiempo_entrega # Acumula los tiempos de uso de la i
			# print(tiempo_entrega)
			yield self.env.timeout(tiempo_entrega)
			# self.vehiculos.release()
			# pasa = self.env.now # Guarda el minuto cuado comienza a ser atendido
			espera = tiempo_entrega + llega
			self.te = self.te + espera
			deja = self.env.now
			self.fin = deja # Conserva globalmente el ultimo minuto de la simulacion
			# print(self.fin)