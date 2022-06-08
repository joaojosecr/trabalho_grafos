import time

def dijkstra(G, s, dest,q):

    inicio = time.time()    # Calcular tempo
    print("\n\n  /////////////// INICIANDO DIJKSTRA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n\n")
    Q = []   
    dist = []               # Vetor que armazena a distância de s a cada vértice
    pred = []               # Vetor que armazena o predecessor cada vértice
    
    if (dest == s):         # Verificar se o vertice de origem é igual ao de destino para evitar calculos desnecessarios
        fim = time.time()   # Calcular tempo
        tempo = fim - inicio
        print("Caminho: [",s,',', dest,']')
        print("Custo: 0")
        print("Tempo", tempo, "segundos")
        return dist, pred, fim - inicio
        
    else:
        for v in range(q):
            Q.append(v)               # Q: lista dos vértices a serem processados
            dist.append(float("inf")) # Distancia de s a cada vertice
            pred.append(None)         # Predecessor de cada vertice

        dist[s]=0
        while (len(Q)!=0):            # Verificar se  lista Q não for vazia (há vertices para processar)
            min = float("inf")
            u = Q[0]

            for i in Q:
                if (dist[i] < min):
                    min = dist[i] # Atualiza valor de distancia minima
                    u = i         # u: Vértice de menor distancia em Q
            Q.remove(u)           #Remover u de Q
            
            for v in range(len(G)):
                    
                if G[v][0] == u :
                    if  dist[G[v][1]] > (dist[u] + G[v][2]):  # Verificando se o novo caminho é menor que 
                        dist[G[v][1]] = dist[u] + G[v][2]     # O antigo para substituir na lista de distancia  
                        pred[G[v][1]] = u
        
        fim = time.time()                                     # Calcular tempo 
     
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
        print("Tempo", fim - inicio, "segundos")
        return dist, pred, fim - inicio
    