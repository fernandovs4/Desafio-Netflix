import numpy as np
from scipy.linalg import diagsvd
import pandas as pd
def calculaAuto(B): #função utilizada para calcular os autovetores e autovalores
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
    valor_minimo = min(min(linha) for linha in A)
    valor_maximo = max(max(linha) for linha in A)
    numero_ruido = np.random.randint(valor_minimo, valor_maximo + 1)
   # funcao principal
    numero = A[linha][coluna]
    B = A.copy()
    B[linha][coluna] = numero_ruido


    return B, numero, linha, coluna


def svd(A):
    # funcao que realiza a descomposicao SVD
    B, numero, linha, coluna = escolheAleatorio(A)

    sigma, U, V_transposto = calculaAuto(B)

    maximo = len(B)
    while abs(numero-B[linha][coluna] > 1):
        B[maximo][maximo] = 0
        B = U@sigma@V_transposto
        maximo -= 1
  
    return B
 
    



def main():
    df = pd.read_csv('ratings_small.csv', sep=',')

    movieId = df['movieId'].unique()
    rating = df['rating']
 

        # Criar a tabela pivô
    pivot_table = pd.pivot_table(df, values='rating', index=['userId'], columns=['movieId'], aggfunc='mean')

    # Preencher as células vazias com a média da linha
    pivot_table = pivot_table.apply(lambda row: row.fillna(2.5), axis=1)

    # Exibir a tabela pivô resultante
    print(pivot_table)
    
    
    
if __name__ == '__main__':
    main()