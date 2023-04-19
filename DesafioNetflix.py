import numpy as np
from scipy.linalg import diagsvd
import pandas as pd
import random

def calculaAuto(B): #função utilizada para calcular os autovetores e autovalores
    U, S, VT = np.linalg.svd(B)
    compressão = 190 # quantidade de autovalores e autovetores que serão utilizados
    return np.diag(S[:compressão]),  U[:, :compressão],VT[:compressão, :] # retorna os autovalores, autovetores e a matriz transposta dos autovetores

def escolheAleatorio(A):
    # funcao que escolhe um numero aleatorio de um array
    df = A
    # Obtenha uma lista dos índices de linhas e colunas que não são NaN
    indices_validos = np.argwhere(~np.isnan(df.values))
    # Escolha um índice aleatório que não seja NaN
    indice_aleatorio = np.random.choice(len(indices_validos))
    # Obtenha a linha e a coluna correspondente ao índice selecionado aleatoriamente
    linha, coluna = indices_validos[indice_aleatorio]
    # Obtenha o elemento e a posição correspondente no dataframe
    elemento = df.iloc[linha, coluna]
    # # calcular a média de cada coluna
    df = df.fillna(df.mean())
    df = df.to_numpy()
    B = df.copy()
    B[linha,coluna] = random.randrange(1, 6)
   # funcao principal
    numero = elemento
    return B, numero, linha, coluna

# def calculaK(A):
    # B, numero, linha, coluna = escolheAleatorio(A)
    # sigma, U, V_transposto = calculaAuto(B)
    # v = U@sigma@V_transposto
    # v = v[linha][coluna]
    # maximo = 670
    # while abs(numero- v) > 0.2:
    #     sigma[maximo][maximo] = 0
    #     v = U@sigma@V_transposto
    #     v = v[linha][coluna]
    #     maximo -= 1
    # k = 480
    # return k



    
