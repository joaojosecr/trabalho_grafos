import os
from dijkstra import dijkstra
from bellmanFord import bellmanFord
from buscaLargura import buscaLargura
import PySimpleGUI as sg 

# PARA INSTALAR PySimpleGUI utilize:  pip install pysimplegui 


class TelaSG:
    def __init__(self):
        layout=[
            
            [sg.Text('Selecione o grafo no diretório:')],
            [sg.InputText(key="grafo",size=(80,1)),
            sg.FileBrowse(initial_folder=caminho+"\\Datasets",file_types=(("Text files", ".txt"),))],
            [sg.Text('Nó de origem: '),sg.Input(key='origem',size=(5,1))],
            [sg.Text('Nó de destino:'),sg.Input(key='destino',size=(5,1))],
            [sg.Button('Calcular',key='calc'),sg.Button('Sair',key='exit')],
            [sg.Output(size=(80,7))],
            [sg.Text('João José Cardoso Ribeiro  18.1.8160')]
            
        ]

        self.janela = sg.Window("Analise de grafo").layout(layout)
        
    def Iniciar(self):

        # Extrair dados     
        self.button, self.values = self.janela.read()

        try:   
            if(self.button == 'calc'):
                #self.m1=self.values['m1']
                #self.m2=self.values['m2']
                #self.m3=self.values['m3']
                self.grafoName=self.values['grafo']
                
                try:
                    G, q,e= lerGrafo(self.grafoName)
                except:
                    print("Eror ao ler grafo. Selecione outro grafo.")
                #print(G)

                try:
                    s=int(self.values['origem'])
                except:
                    print("Selecione uma origem.")
        
                try:
                    d=int(self.values['destino'])
                except:
                    print("Selecione um destino.")
                

                str=list(self.grafoName)
                name=[]
                nome=[]
                while (len(str)>0):
                    
                    l=str[len(str)-1]
                    if(l=='/'):
                        while (len(nome)>0):
                            aux=nome[len(nome)-1]
                            nome.pop()
                            name.append(aux)
                        grafoName=''.join(name)   
                        break
                    else:
                        nome.append(l)
                        str.pop()
                
                
                metodo=1


                match grafoName:
                    case "facebook_combined.txt":
                        metodo=2
                    case "rome99c.txt":
                        metodo=1
                    case "rg300_4730.txt":
                        metodo=2
                    case "toy.txt":
                        metodo=1
                    case "USA-road-dt.DC.txt":
                        metodo=2
                    case "USA-road-dt.NY.txt":
                        metodo=2
                    case "web-Google.txt":
                        metodo=1
                

                if(-1<s & s<q):
                    if(-1<d & d<q):
                        Calcular(G,q,e,s,d,self,metodo)
                    else:
                        print("\nEscolha um valor de destino entre 0 e",q-1)    
                else:
                    print("\nEscolha um valor de origem entre 0 e",q-1)
                    

        except Exception as e:
            print("Selecione um grafo, uma origem e um destino!\n",e)
            
        return self.button

def Calcular(G,q,e,s,d,self,metodo):


    if(metodo==1):
        dijkstra(G,s,d,q)
    elif(metodo==2):
        bellmanFord(G,s,d,q,e)
    elif(metodo==3):
        buscaLargura(self,s,d,q,G)
    
def imprimirGrafo(G):
    print("\nV = vertice de saida da aresta\nE = vertice de chegada da aresta\nw = peso da aresta\n\n(V, E, w)")
    for i in range(len(G)):
        print(G[i])

def lerGrafo(file):
    
    arquivo = []
    try:
        with open(file, 'r', encoding='utf-8') as grafo:
            for linha in grafo:
                stripped_line = linha.strip()       # Separa as linhas do arquivo, cada linha em uma posição da lista
                linha_list = stripped_line.split()
                arquivo.append(linha_list)          # Salvando na lista
    except:
        return 0
    numVertices=int(arquivo[0][0])  # Salvando número de vertices      
    numArestas=int(arquivo[0][1])   # Salvando número de arestas
    arquivo.pop(0)                  # Eliminando a primeira linha que contem vertices e arestas

    G = []  # grafo final

    for i in range(numArestas):     # Para cada aresta, adiciona uma posição no grafo
        G.append([])
        vertice, fim, peso = arquivo[i] # Salva cada número em uma variavel auxiliar
        G[i].append(int(vertice))       # Retira o primeiro vertice da aresta e sala na posição G[i][0]
        G[i].append(int(fim))           # Retira o segundo vertice da aresta e sala na posição G[i][1]
        G[i].append(int(peso))          # Retira o peso da aresta e sala na posição G[i][2]
        
    for i in range(len(G)):             # percorre o grafo
        if len(G[i]) > 0:               # se existe arestas para o vertice 'i'
            G[i] = tuple(G[i])          # tupla que representa as arestas
            G[i] = tuple(G[i])
            G[i] = tuple(G[i])
    
    return G, numVertices, numArestas
         
caminho = os.path.dirname(os.path.abspath(__file__))

janela = TelaSG()

print("\n\tJoão José Cardoso Ribeiro\t18.1.8160\n\t")

while True:
    event = janela.Iniciar()
    if event == sg.WIN_CLOSED or event == 'exit':
        break