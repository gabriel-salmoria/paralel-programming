from time import sleep
from random import randint
from threading import Thread, Lock, Condition


def produtor(parity):
    global buffer
    for i in range(parity, 20, 2):
        sleep(randint(0, 2))           # fica um tempo produzindo...
        item = 'item ' + str(i)
        with lock:
            if len(buffer) == tam_buffer:
                print('>>> Buffer cheio. Produtor ira aguardar.')
                lugar_no_buffer.wait()    # aguarda que haja lugar no buffer
            buffer.append(item)
            print('Produzido %s (ha %i itens no buffer)' % (item, len(buffer)))
            item_no_buffer.notify()


def consumidor(parity):
    global buffer
    for i in range(parity, 20, 2):
        with lock:
            if len(buffer) == 0:
                print('>>> Buffer vazio. Consumidor ira aguardar.')
                item_no_buffer.wait()   # aguarda que haja um item para consumir
            item = buffer.pop(0)
            print('Consumido %s (ha %i itens no buffer)' % (item, len(buffer)))
            lugar_no_buffer.notify()
        sleep(randint(0, 2))         # fica um tempo consumindo...


buffer = []
tam_buffer = 5
lock = Lock()
lugar_no_buffer = Condition(lock)
item_no_buffer = Condition(lock)

# criando e produtores e consumidores
produtores = []
for i in range(2):
    produtores.append(Thread(target=produtor, args=(i,)))

consumidores = []
for i in range(2):
    consumidores.append(Thread(target=consumidor, args=(i,)))

# iniciando os produtores e consumidores
for produtor in produtores:
    produtor.start()

for consumidor in consumidores:
    consumidor.start()

# esperando os produtores e consumidores terminarem
for produtor in produtores:
    produtor.join()

for consumidor in consumidores:
    consumidor.join()
