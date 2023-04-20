import pandas as pd
from DesafioNetflix import calculaAuto

df = pd.read_csv('ratings_small_formated.csv', sep=',', index_col=0)
#Substitui os valores NaN por 2.5
df = df.fillna(2.5)
df = df.to_numpy()
B = df.copy()
i = 300 # Altere aqui
j = 100 # E aqui
numero_esperado = B[i][j]
B[i][j] = 1
sigma, U, V_transposto = calculaAuto(B)
B = U@sigma@V_transposto
diferenca = abs(B[i][j] - numero_esperado)
print(f"Numero esperado: {numero_esperado}\nNumero achado: {B[i][j]}\nDiferença: {diferenca}")
