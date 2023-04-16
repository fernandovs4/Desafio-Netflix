import numpy as np
from scipy.linalg import diagsvd
import pandas as pd
import random

def calculaAuto(B): #função utilizada para calcular os autovetores e autovalores
    U, S, Vt = np.linalg.svd(B)
    sigma = np.zeros(B.shape)
    sigma[:len(S), :len(S)] = np.diag(S)
    return sigma, U, Vt


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
    # col_mean = np.nanmean(df, axis=0)

    # # substituir os NaNs pela média da coluna correspondente
    # mask = np.isnan(df)
    # df[mask] = np.take(col_mean, np.where(mask)[1])
    df = df.fillna(2.5)

    df = df.to_numpy()
    B = df.copy()
    B[linha,coluna] = random.randrange(1, 6)
   # funcao principal
    numero = elemento
   
    return B, numero, linha, coluna


def svd(A):
    B, numero, linha, coluna = escolheAleatorio(A)
    sigma, U, V_transposto = calculaAuto(B)
    maximo = 670
    v = U@sigma@V_transposto
    v = v[linha][coluna]
    while abs(numero- v) > 0.2:
        sigma[maximo][maximo] = 0
        v = U@sigma@V_transposto
        v = v[linha][coluna]
        maximo -= 1
        
  
    return sigma
 
    



def main():
    df = pd.read_csv('ratings_small.csv', sep=',')
    df_ratings = df.pivot_table(index='userId', columns='movieId', values='rating')

    # Substitui os valores NaN pela média de cada coluna
    df = df_ratings.fillna(df_ratings.mean())
    print(df)
   
    sigma = svd(df)
    #transformar pra csv
    df = pd.DataFrame(sigma)
    df.to_csv('sigma2.csv', index=False, header=False)
    
   

if __name__ == "__main__":
     main()
