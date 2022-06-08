import time

def bellmanFord(G, s, dest,q,e):
    inicio = time.time()                # Calcular tempo
    print("\n\n  /////////////// INICIANDO BELLMAN FORD \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n\n")
    dist = []
    pred = []

    if (dest == s):                     # Verificar se o vertice de origem é igual ao de destino para evitar calculos desnecessarios
        fim = time.time()               # Calcular tempo
        tempo = fim - inicio
        print("Caminho: ",s, dest)
        print("Custo: 0")
        print("Tempo", tempo, "segundos")
        return dist, pred, tempo
    else:

        for v in range(q):
            dist.append(float("inf"))   # Vetor que armazena a distancia de s a cada vertice
            pred.append(None)           # Vetor que armazena o predecessor de cada vertice
        dist[s] = 0

        for i in range(q):
            trocou = False
            
            for (u,v,w) in G:

                if  dist[v] > dist[u] + w:  # Verificando se o novo caminho é menor que 
                    dist[v] = dist[u] + w   # o antigo para substituir na lista de distancia  
                    pred[v] = u
                    trocou = True
            if trocou == False:         # A execução pode ser encerrada prematuramente
                break
        
        fim = time.time()                    # Calcular tempo

        caminho = []
        caminho.append(dest)
        custo = dist[dest]
        if pred[dest] != None:
            while dest != s:
                caminho.append(pred[dest])
                dest = pred[dest]
        else:
            print("Não existe caminho para o vertice escolhido!")
            pass

       
        print("Caminho: ",caminho[::-1])
        print("Custo: ", custo)
        print("Tempo", fim - inicio, "s")

        tempo = fim - inicio
        return dist, pred, tempo