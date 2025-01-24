import threading
import time

class SistemaDeReservas:
    def __init__(self, quantidade_recursos):
        # Inicializa com a quantidade de recursos (datashows) disponíveis
        self.recursos = [True] * quantidade_recursos  # True significa disponível
        self.mutex = threading.Lock()  # Lock para garantir que uma reserva seja feita de cada vez

    def reservar_recurso(self, id_usuario):
        # Tenta reservar um recurso (datashow)
        with self.mutex:  # Usando o lock para garantir acesso único à função
            for indice in range(len(self.recursos)):
                if self.recursos[indice]:  # Se o recurso estiver disponível
                    self.recursos[indice] = False  # Marca o recurso como reservado
                    print(f"Usuário {id_usuario} reservou o recurso {indice + 1}")
                    time.sleep(2)  # Simula o tempo de uso do recurso
                    self.recursos[indice] = True  # Libera o recurso após o uso
                    print(f"Usuário {id_usuario} liberou o recurso {indice + 1}")
                    return
            print(f"Usuário {id_usuario} não conseguiu reservar um recurso, todos estão ocupados.")

# Função que simula múltiplos usuários tentando fazer reservas
def simular_reservas(sistema, id_usuario):
    sistema.reservar_recurso(id_usuario)

# Cria o sistema com 3 recursos
sistema = SistemaDeReservas(3)

# Cria várias threads simulando usuários tentando reservar os recursos
threads = []
for usuario in range(10):  # Simula 10 usuários
    thread = threading.Thread(target=simular_reservas, args=(sistema, usuario + 1))
    threads.append(thread)
    thread.start()

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

print("Finalizado.")
