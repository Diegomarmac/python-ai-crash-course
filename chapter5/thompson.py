# dados cierto numero de slot machines, vamos abuscar la maquina con el mejor ratio de victoria
import numpy as np

conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05] # Definimos los ratio de conversion, cada valor es la probabilidad de ganar de cada slot machine 
N = 10000 # numero de muestras
d = len(conversionRates) # numero de slot machines

# vamos a crear un dataset simulando el jugar en cada slot machine N veces
X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

# Ahora vamos a crear arrreglos para cada psoible "reward"
nPosReward= np.zeros(d)
nNegReward = np.zeros(d)

# taking our best slot machine through beta distribution and updatong its losses and wins
for i in range(N):
    selected  = 0
    maxRandom = 0
    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j
    if X[i][selected] == 1:
        nPosReward[selected] += 1 # actualizamos el indice de reward positivos
    else:
        nNegReward[selected] += 1 # actualizamos el indice de recompensas negativas

# ahora vamos a mostrar que slot machine es considerada la mejor
nSelected = nPosReward + nNegReward
for i in range(d):
    print("Maquina numero " + str(i + 1) + " fue seleccionada " + str(nSelected[i]) + " veces")
print("Por lo tanto, tenemos que la mejor maquina es: " + str(np.argmax(nSelected) +1))

