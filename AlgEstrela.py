import numpy as np
#CRIANDO A CLASSE NÓ COM OS MÉTODOS CONSTRUTOR, ADICIONAR ADJACENTES E MOSTRAR ADJACENTES

class Nó:

    def __init__(self, cidade, linha_reta):
        self.cidade = cidade
        self.visitado = False
        self.linha_reta = linha_reta #heurística da distância para o objetivo
        self.adjacentes = []

    def insere_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.nó.cidade, i.custo)

#CRIANDO A CLASSE ADJACENTE COM O MÉTODO CONSTRUTOR 

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo #Atributo da distância de nó a nó pela estrada

        #Atributo que representa a soma das distâncias da estrada(nó a nó) e a distância em linha reta de um nó ao objetivo.
        self.distancia_aestrela = vertice.linha_reta + self.custo

#CRIANDO A CLASSE GRAFO O QUAL FAZ A JUNÇÃO DO NÓ COM OS DETERMINADOS ADJACENTES

class Grafo:
    Porto_União = Nó('Porto União', 203)
    Paulo_Frontin = Nó('Paulo Frontin', 172)
    Canoinhas = Nó('Canoinhas', 141)
    Três_Barras = Nó('Três Barras', 131)
    São_Mateus = Nó('São Mateus', 123)
    Irati = Nó('Irati', 139)
    Curitiba = Nó('Curitiba', 0)
    Palmeira = Nó('Palmeira', 59)
    Mafra = Nó('Mafra', 94)
    Campo_Largo = Nó('Campo Largo', 27)
    Balsa_Nova = Nó('Balsa Nova', 41)
    Lapa = Nó('Lapa', 74)
    Tijucas_do_Sul = Nó('Tijucas do Sul', 56)
    Araucária = Nó('Araucária', 23)
    São_José_dos_Pinhais = Nó('São José dos Pinhais', 13)
    Contenda = Nó('Contenda', 39)

#Adjacentes com as distâncias de estrada correspondentes de nó a nó 

    Porto_União.insere_adjacentes(Adjacente(Paulo_Frontin, 46))
    Porto_União.insere_adjacentes(Adjacente(São_Mateus, 87))
    Porto_União.insere_adjacentes(Adjacente(Canoinhas, 78))

    Paulo_Frontin.insere_adjacentes(Adjacente(Irati, 75))
    Paulo_Frontin.insere_adjacentes(Adjacente(Porto_União, 46))

    Canoinhas.insere_adjacentes(Adjacente(Três_Barras, 12))
    Canoinhas.insere_adjacentes(Adjacente(Mafra, 66))
    Canoinhas.insere_adjacentes(Adjacente(Porto_União, 78))

    Três_Barras.insere_adjacentes(Adjacente(Canoinhas, 12))
    Três_Barras.insere_adjacentes(Adjacente(São_Mateus, 43))
    
    São_Mateus.insere_adjacentes(Adjacente(Três_Barras, 43))
    São_Mateus.insere_adjacentes(Adjacente(Lapa, 60))
    São_Mateus.insere_adjacentes(Adjacente(Irati, 57))
    São_Mateus.insere_adjacentes(Adjacente(Palmeira, 77))
    São_Mateus.insere_adjacentes(Adjacente(Porto_União, 87))

    Irati.insere_adjacentes(Adjacente(Paulo_Frontin, 75))
    Irati.insere_adjacentes(Adjacente(São_Mateus, 57))
    Irati.insere_adjacentes(Adjacente(Palmeira, 75))

    Curitiba.insere_adjacentes(Adjacente(São_José_dos_Pinhais, 15))
    Curitiba.insere_adjacentes(Adjacente(Araucária, 37))
    Curitiba.insere_adjacentes(Adjacente(Balsa_Nova, 51))
    Curitiba.insere_adjacentes(Adjacente(Campo_Largo, 29))

    Palmeira.insere_adjacentes(Adjacente(Irati, 75))
    Palmeira.insere_adjacentes(Adjacente(São_Mateus, 77))
    Palmeira.insere_adjacentes(Adjacente(Campo_Largo, 55))

    Mafra.insere_adjacentes(Adjacente(Canoinhas, 66))
    Mafra.insere_adjacentes(Adjacente(Lapa, 57))
    Mafra.insere_adjacentes(Adjacente(Tijucas_do_Sul, 99))

    Campo_Largo.insere_adjacentes(Adjacente(Palmeira, 55))
    Campo_Largo.insere_adjacentes(Adjacente(Balsa_Nova, 22))
    Campo_Largo.insere_adjacentes(Adjacente(Curitiba, 29))

    Balsa_Nova.insere_adjacentes(Adjacente(Campo_Largo, 22))
    Balsa_Nova.insere_adjacentes(Adjacente(Curitiba, 51))
    Balsa_Nova.insere_adjacentes(Adjacente(Contenda, 19))

    Lapa.insere_adjacentes(Adjacente(São_Mateus, 60))
    Lapa.insere_adjacentes(Adjacente(Contenda, 26))
    Lapa.insere_adjacentes(Adjacente(Mafra, 57))

    Tijucas_do_Sul.insere_adjacentes(Adjacente(São_José_dos_Pinhais, 49))
    Tijucas_do_Sul.insere_adjacentes(Adjacente(Mafra, 99))

    Araucária.insere_adjacentes(Adjacente(Contenda, 18))
    Araucária.insere_adjacentes(Adjacente(Curitiba, 37))

    São_José_dos_Pinhais.insere_adjacentes(Adjacente(Tijucas_do_Sul, 49))
    São_José_dos_Pinhais.insere_adjacentes(Adjacente(Curitiba, 15))

    Contenda.insere_adjacentes(Adjacente(Lapa, 26))
    Contenda.insere_adjacentes(Adjacente(Araucária, 18))
    Contenda.insere_adjacentes(Adjacente(Balsa_Nova, 19))

grafo = Grafo()

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

        #Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0 
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente #Incluindo o adjacente que vai receber como parametro para o objeto dessa classe
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i,' - ', self.valores[i].vertice.cidade, ' - ',
                        self.valores[i].custo, ' - ',
                        self.valores[i].vertice.linha_reta, ' - ',
                        self.valores[i].distancia_aestrela)
                    
#grafo.Araucária.adjacentes[0].vertice.linha_reta #Mostra a distância do nó para o objetivo do adjacente [0] 
#grafo.Araucária.adjacentes[0].distancia_aestrela #Mostra a somatória das distâncias
#grafo.Araucária.adjacentes[0].custo #Mostra o custo de nó a nó 
#grafo.Araucária.adjacentes[0].vertice.cidade #Mostra o nome da cidade adjacente no índice 0


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual): #Construtor que recebe o vertice, que corresponde ao caminho a ser percorrido
        print('-----------------')
        print('Atual: {}'.format(atual.cidade)) #Mostra o elemento atual
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None: #Se existir um valor  na posição 0 executa a função recursiva
                self.buscar(vetor_ordenado.valores[0].vertice) #Recebe um vertice como parametro para depois buscar os adjacentes

buscaAestrela = AEstrela(grafo.Curitiba)
buscaAestrela.buscar(grafo.Porto_União)