import pandas as pd
from DesafioNetflix import calculaAuto

df = pd.read_csv('ratings_small_format.csv', sep=',',header=None)
df = df.to_numpy()
B = df.copy()
x = 464
numero_esperado = B[x-1][x-1]
B[x-1][x-1] = 1
sigma, U, V_transposto = calculaAuto(B)
B = U@sigma@V_transposto
print(f"Numero esperado: {numero_esperado}\nNumero achado: {B[x-1][x-1]}")
