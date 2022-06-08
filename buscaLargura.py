from math import dist
import time

import time

def buscaLargura(self,s,d,q,G):
    Q = []   
    desc = []               
    R = []               
    
    print("\n\n  /////////////// INICIANDO BUSCA EM LARGURA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n\n")
    inicio=time.time()
    for v in range(q):
        desc.append(0)            # Vertices descobertos
    
    Q.append(s)
    R.append(s)
    desc[s] = 1
    if (d == s):         # Verificar se o vertice de origem é igual ao de destino para evitar calculos desnecessarios
        fim = time.time()   # Calcular tempo
        tempo = fim - inicio

    else:
        while len(Q) != 0:
            u = Q.pop(0)

            for (v,w,x) in range(len(G)):
                if(v==u):
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1
                        
                    if (R[d]!= 0):
                        break

        fim = time.time()                                     # Calcular tempo 
        print(R)
        caminho = []
        caminho.append(d)
        custo = dist[d]
        if R[d] != 0:
            while d != s:
                caminho.append(R[d])
                d = R[d]
        else:
            print("Não existe caminho para o vertice escolhido!")
            pass

        
        print("Caminho: ",caminho[::-1])
        print("Custo: ", custo)
        print("Tempo", fim - inicio, "segundos")
        