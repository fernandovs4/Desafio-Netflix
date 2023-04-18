import numpy as np
from scipy.linalg import diagsvd
import pandas as pd
import time
import random

def calculaAuto(B): #função utilizada para calcular os autovetores e autovalores
    

    U, s, Vt = np.linalg.svd(B)

    # Matriz Sigma
    Sigma = np.zeros(B.shape)
    Sigma[:len(s), :len(s)] = np.diag(s)
    return sigma, U, V_transposto


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
    
    print("Elemento aleatório não-NaN:", elemento)
    print("Posição do elemento:", linha, coluna)
    df = df.fillna(2.5)

    df = df.to_numpy()
    B = df.copy()
    B[linha,coluna] = random.randrange(1, 6)
    print(B[linha][coluna], "aaaaaaaaaaaaa")
   # funcao principal
    numero = elemento
   
    return B, numero, linha, coluna


def svd(A):
    B, numero, linha, coluna = escolheAleatorio(A)


    sigma, U, V_transposto = calculaAuto(B)
   

    maximo = len(sigma)  - 1
 
    print(numero)
    print(B[linha][coluna], "bbbbbb")
    while sigma[maximo][maximo] < 11:
            sigma[maximo][maximo] = 0
            maximo -= 1
    print(U@sigma@V_transposto)
    v = U@sigma@V_transposto
    v = v[linha][coluna]
    while abs(numero- v) > 0.5:
        sigma[maximo][maximo] = 0
        print(sigma)
        print(abs(numero- v) )
        v = U@sigma@V_transposto
        v = v[linha][coluna]
        maximo -= 1
  
    return sigma
 
    



def main():
    df = pd.read_csv('ratings_small.csv', sep=',')

   
    df = df.pivot(index='userId', columns='movieId', values='rating')
    print(df)
   
    sigma = svd(df)
    #transformar pra csv
    df = pd.DataFrame(sigma)
    df.to_csv('sigma.csv', index=False, header=False)
    
   


    
if __name__ == '__main__':
    main()


df = pd.read_csv('ratings_small.csv', sep=',')
df = df.pivot(index='userId', columns='movieId', values='rating')
df = df.fillna(2.5)
df = df.to_numpy()
B = df.copy()
B[670][0] = 2

sigma, U, V_transposto = calculaAuto(B)
df1 = pd.read_csv('sigma.csv', sep=',')
df1 = df1.to_numpy()
print(U.shape, V_transposto.shape, df1.shape)
print(df1)
U = np.delete(U, 670, axis=1)
b = U@df1@V_transposto
print(b[670][0])