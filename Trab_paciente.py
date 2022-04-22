import time
import os
class Paciente:
    def __init__(self, nome, tipoSanguineo, dataNascimento):
        self.nome = nome
        self.tipoSanguineo = tipoSanguineo
        self.dataNascimento = dataNascimento
    
    def __repr__(self):
        return ', Nome: '+ self.nome + ', Tipo Sanguíneo: ' + self.tipoSanguineo + ', Data Nascimento: ' + self.dataNascimento

class MaxHeap:

    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if len(self.heap) != 1:
            return self.heap[1]
        else:
            return str("Não há próximo paciente")
            
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)


def escolha(opcao):
        if numero == 1:
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            nome = input(str("Informe o Nome do Paciente: "))
            tipoSanguineo = input(str("Informe o Tipo Sanguineo do Paciente: "))
            dataNascimento = input("Informe a Data de Nascimento do Paciente: ")
            paciente = Paciente(nome, tipoSanguineo, dataNascimento)
            prioridade = 0
            while(prioridade < 1 or prioridade > 10):
                prioridade = int(input("Informe entre (1-10) Qual a prioridade: "))
            global ordem
            global contagem
            item = (prioridade, ordem, paciente)
            h.put(item)
            ordem += 1
            contagem -= 1
            print("Contagem atual: ", contagem)
        elif numero == 2:
            if(h.peek()):
                chamados.append(h.peek())
            print(h.get())
        elif numero == 3:
            print(h.peek())
        elif numero == 4:
            if(len(chamados)<=4):
                for i in range(len(chamados)):
                    print(chamados[i])
            else:
                for i in range(1,6):
                    print(chamados[len(chamados) - i])
        else:
            print("Ops Opção inválida")
    
## Sistema ##
contagem = 999
ordem = 0
h = MaxHeap()
chamados = list()
while(True):
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("(1) Adicionar novo paciente\n(2) Chamar próximo paciente\n(3) Mostrar próximo paciente\n(4) Listar últimos 5 chamados")
    numero = 0
    while(numero < 1 or numero > 4):
        numero = int(input("Digite qual opção deseja: "))
        escolha(numero)
        
