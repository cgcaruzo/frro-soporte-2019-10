import random
import math
import simpy
'''
Producto
- Codigo
- Utilidad
- Stock
- Stock de seguridad
- Lead Time
- Tiempo Promedio de Venta
'''
SEMILLA = 350
NUM_CLIENTES = 1
T_VENTA = 5
STOCK = 50



def venta (env, name, cliente ):
  global te
  global fin
  llega = env.now # Guarda el minuto de llegada del cliente
  #print ("---> %s llego a cliente en minuto %.2f" % (name, llega))
  with cliente.request() as request: # Espera su turno
    yield request # Obtiene turno
    pasa = env.now # Guarda el minuto cuado comienza a ser atendido
    #espera = pasa - llega # Calcula el tiempo que espero
    #te = te + espera # Acumula los tiempos de espera
    #print ("**** %s pasa con peluquero en minuto %.2f" % (name, pasa))
    '''
    yield env.process(cortar(name)) # Invoca al proceso cortar
    deja = env.now #Guarda el minuto en que termina el proceso cortar 
    print ("<--- %s deja peluqueria en minuto %.2f" % (name, deja))
    '''
    fin = pasa # Conserva globalmente el ultimo minuto de la simulacion
  

def principal (env, cliente, tventa, stock):
  llegada = 0
  i = 0
  for i in range(stock): # Para n clientes
    R = random.random()
    llegada = -tventa * math.log(R) # Distribucion exponencial
    yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
    i += 1
    env.process(venta(env, 'Producto %d' % i, cliente)) 

def obtenerTiempoAgotado(stock, tventa):
  #random.seed (SEMILLA)  # Cualquier valor
  env = simpy.Environment() # Crea el objeto entorno de simulacion
  cliente = simpy.Resource(env, NUM_CLIENTES) #Crea los recursos (peluqueros)
  env.process(principal(env, cliente, tventa, stock)) #Invoca el proceso princial
  env.run() #Inicia la simulacion
  return fin
'''
  print ("\n---------------------------------------------------------------------")
  print ("\nIndicadores obtenidos: ")

  #lpc = te / fin
  #print ("\nLongitud promedio de la cola: %.2f" % lpc)
  #tep = te / STOCK
  #print ("Tiempo de espera promedio = %.2f" % tep)
  print ("Tiempo de finalizacion = %.2f" % fin)
  #upi = (dt / fin) / NUM_CLIENTES
  #print ("Uso promedio de la instalacion = %.2f" % upi)
  print ("\n---------------------------------------------------------------------")'''
  

'''
  te  = 0.0 # tiempo de espera total
  dt  = 0.0 # duracion de servicio total
  fin = 0.0 # minuto en el que finaliza
  '''