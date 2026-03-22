
import random

random.seed(10) #aqui é para falar que são 10 numeros randomicos

class Tesouro: #construtor de tesouro
    def __init__(self, peso:float, valor:float, desc:str): #os parametros sao passado na ordem ao contrario, primerio o objeto dps a classe
        self.peso = peso
        self.valor = valor
        self.desc = desc


class Solucao:
    def __init__(self, qtd:int):
        self.fitness:int = -1
        self.selecionados:list[bool] = [] #criar vetor booleano
        for _ in range(qtd): # for até quantidade mandada
            self.selecionados.append(False) #deixa todo mundo falso no vetor
        
    def randomize(self):
        for i in range(len(self.selecionados)): # for para o tamanho do vetor
            self.selecionados[i] = random.random() > 0.5 # modo de aleatorizar um bool


class Modelo:
    def __init__(self, capacidade:float, filename:str):
        self.capacidade = capacidade
        self.tesouros:list[Tesouro] = [] #recebe uma lista de tesouros
        quantidade = 10
        with open(filename, "r", encoding="utf-8") as file:
            for line in file: #passar por todas as linhas do arquivo
                peso, valor, desc = line.split(";") # separa por ponto e virgula
                peso = float(peso)
                valor = float(valor)
                tesouro = Tesouro(peso, valor, desc) #pega todos as variaveis que foram add e coloca em tesouros
                self.tesouros.append(tesouro) #add ao tesouro da da classe
                quantidade -= 1 # mesma coisa de quantidade--;
                if quantidade <= 0:
                    break
    

    def quantidadeTesouros(self):
        return len(self.tesouros)


    def obterNomesTesourosSelecionados(self, solucao:Solucao) -> list[str]: # o -> nesse caso é para falar o tipo de retorno do metodo
        nomes:list[str] = []
        for i, ativo in enumerate(solucao.selecionados): #uma forma diferente de fazer: for i in range(len(solucao.selecionados))
            if ativo:
                nomes.append(self.tesouros[i].desc)
        return nomes

    
    def fitness(self, solucao:Solucao) -> int:
        peso_total = 0
        valor_total = 0
        for i in range(len(solucao.selecionados)):
            if solucao.selecionados[i]:
                tesouro = self.tesouros[i]
                peso_total += tesouro.peso
                valor_total += tesouro.valor
        if peso_total > self.capacidade:
            return 0
        solucao.fitness = valor_total
        return valor_total

    def cruzamento(self, p1:Solucao, p2:Solucao) -> tupla[Solucao,Solucao]:
        n:int = len(self.tesouros)
        index = random.randint(0, n-1)
        f1 = Solucao(n)
        f2 = Solucao(n)
        for i in range(0,index):
            f1.selecionados[i] = p1.selecionados[i]
            f2.selecionados[i] = p2.selecionados[i]
        for i in range(index,n):
            f1.selecionados[i] = p2.selecionados[i]
            f2.selecionados[i] = p1.selecionados[i]
        return (f1, f2)


if __name__ == "__main__":
    modelo = Modelo(200, "tesouros.csv")
    p1 = Solucao(modelo.quantidadeTesouros())
    p2 = Solucao(modelo.quantidadeTesouros())
    p1.randomize()
    p2.randomize()

    print(p1.selecionados)
    print(p2.selecionados)

    (f1,f2) = modelo.cruzamento(p1, p2)
    print(f1.selecionados)
    print(f2.selecionados)










