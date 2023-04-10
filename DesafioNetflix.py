import numpy as np
from scipy.linalg import diagsvd

def calculaAuto(B) #função utilizada para calcular os autovetores e autovalores
    autovalores, autovetores = np.linalg.eig(B.T@B) # captura os autovetores e autovalores de B transposto multiplicando B
    autovalores = diagsvd(autovalores, np.shape(B), np.shape(B)) # formata os autovalores
    U = autovetores
    sigma = autovalores
    V_transposto = U.T
    return sigma, U, V_transposto


def escolheAleatorio(A):
    # funcao que escolhe um numero aleatorio de um array
    linha = np.random.randint(0, len(A))
    coluna = np.random.randint(0, len(A[0]))
    numero = A[linha][coluna]


    return (linha, coluna, numero)



def remove_ruido(B, numero, linha, coluna):
    maximo = len(B)
    while abs(numero-B[linha][coluna] > 1):
        B[maximo][maximo] = 0
        maximo -= 1
    return B

   
    
