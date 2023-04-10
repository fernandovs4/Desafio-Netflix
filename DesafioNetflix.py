import numpy as np
import pandas as pd





def escolheAleatorio(A):
    # funcao que escolhe um numero aleatorio de um array
    linha = np.random.randint(0, len(A))
    coluna = np.random.randint(0, len(A[0]))
    numero = A[linha][coluna]


    return (linha, coluna, numero)



def svd(A):
    # funcao que realiza a descomposicao SVD
    ruido = escolheAleatorio(A)

   
    
