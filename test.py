import pandas as pd

# Cria um DataFrame a partir dos dados fornecidos
data = {'userId': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        'movieId': [31, 1029, 1061, 1129, 1172, 62, 110, 144, 150, 153, 161, 165, 168, 296, 318, 355, 356, 377, 527, 588, 592, 593, 595, 736, 778, 866, 1197],
        'rating': [2.5, 3.0, 3.0, 2.0, 4.0, 3.0, 4.0, 3.0, 5.0, 4.0, 3.0, 3.0, 3.0, 4.5, 5.0, 2.5, 5.0, 2.5, 3.0, 3.0, 3.0, 3.0, 2.0, 3.5, 4.0, 3.0, 5.0],
        'timestamp': [1260759144, 1260759179, 1260759182, 1260759185, 1260759205, 835355749, 835355532, 835356016, 835355395, 835355441, 835355493, 835355441, 835355710, 1298862418, 1298862121, 1298861589, 1298862167, 1298923242, 1298862528, 1298922100, 1298923247, 1298921840, 1298923260, 1298932787, 1298863157, 1298861687, 1298932770]
        }
# Cria um novo DataFrame com as notas de cada usuário para cada filme

df = pd.DataFrame(data, columns = ['userId', 'movieId', 'rating', 'timestamp'])
df_ratings = df.pivot_table(index='userId', columns='movieId', values='rating')

# Substitui os valores NaN pela média de cada coluna
df_ratings_mean = df_ratings.fillna(df_ratings.mean())

print(df_ratings_mean)