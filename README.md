 O objetivo do projeto era desenvolver um algoritmo capaz de prever a nota que um usuário daria para um filme sem que ele o tivesse assistido, ou então que já tivesse assistido mas que a nota foi perdida/modificada, o que chamamos dentro do nosso contexto de "ruído".
 
 ## Instalação
Para utilizar o programa basta clonar esse repositório em algum local de sua máquina. Para fazer isso, clique no botão verde **"Code"** logo acima, escolha um modo de baixar o repositório, podendo ser baixando o zip e descompactando ou clonando através de https ou ssh. Após seguir essas etapas, será preciso instalar as bibliotecas necessárias. Isso pode ser feito, estando na raiz do projeto, rodando no terminal o seguinte comando:  `pip install -r requirements.txt `, com isso, as bibliotecas necessárias serão instaladas. Com o ambiente preparado, o usuário estará apto a executar o arquivo demo.py e livre para alterar os valores das variáveis i e j para escolher especificamente o elemento em que deseja aplicar o ruído.
 
## Teoria/Modelo matemático
A técnica SVD, ou Decomposição em Valores Singulares, é uma técnica matemática amplamente utilizada para decompor uma matriz em três componentes principais, a saber: matriz U, matriz Sigma e matriz V^T (a transposta da matriz V). Essa técnica é usada para analisar e compreender as propriedades dos dados, descobrir padrões ocultos e reduzir a dimensionalidade dos dados.

A matriz Sigma obtida na decomposição SVD é uma matriz diagonal contendo os autovalores em relação à matriz original, e esses autovalores são ordenados em ordem decrescente. Os autovalores são medidas da variabilidade dos dados em cada direção da matriz original, e os maiores valores de autovalor correspondem às direções mais importantes para a construção da matriz original.

As colunas da matriz U correspondem aos autovetores à esquerda, enquanto as linhas da matriz V^T correspondem aos autovetores à direita. Esses autovetores representam as direções principais dos dados e são usados para encontrar a estrutura oculta nos dados.

A decomposição SVD pode ser escrita na forma matricial A = UΣV^T.\
A = matriz original\
U = autovetores à esquerda\
Σ = sigma\
V^T = autovetores à direita


\
Para construir o algoritmo nós partimos da tese de que um usuário pode ser representado partindo do padrão geral dos demais usuários que temos acesso aos dados, ou seja, cada usuário possui um pouco de cada perfil e juntando cada uma dessas partes nós chegamos em um que melhor o representa. Sendo assim, nós temos que comprimir a nossa matriz Sigma de tal forma que ela possua apenas aqueles valores mais essenciais para a construção dos perfis em geral, ou seja mantemos os maiores valores e excluímos os menores, haja vista que esses menores seriam os mais afetados pelo ruído aplicado, afetando nossas previsões.

## Por dentro do código
Para que o nosso algoritmo funcione da maneira que gostaríamos nós precisávamos primeiro definir o tamanho da compressão que faríamos, ou seja, quais autovalores manteríamos na nossa análise a fim de considerar apenas aqueles mais influentes na construção dos perfis em geral. Calculamos, então, o K, variável essa responsável por definir até qual autovalor nós mantériamos (Ex: para um K=10, nós manteríamos apenas os 10 maiores autovalores da matriz Sigma), ele foi calculado unindo dois métodos:\
\
1 - Criamos um gráfico contendo os valores da matriz sigma e vimos a partir de qual momento os valores passam a ser tornar pequenos, fazendo com que quando aplicado o ruído os autovalores seriam fortemente impactados e consequentemente o novo valor calculado para a posição do ruído também seria. Seguindo esse método, concordamos que com o K=100 era um valor interessante para capturar os autovalores por conta da forma que eles estavam se comportando a partir disso (cada vez reduzindo menor em relação ao anterior)\
<img src= "https://github.com/fernandovs4/Desafio-Netflix/blob/main/graf_sigma.png">\
2 - Além disso, nós utilizamos alguns valores da matriz, aplicamos o ruído e tentamos recalcular partindo do K=100, e vimos que para grande parte dos elementos selecionados o palpite era próximo do número esperado, por isso, prosseguimos com o K=100.

## Resultados
Fizemos dois testes com o nosso algoritmo:\
1 - O primeiro visava testá-lo para diferentes elementos da matriz original e observar se o valor calculado foi próximo ao esperado (valor original antes do ruído). Com esse teste foi possível analisar que o nosso modelo funcionava para uma parte razoável dos elementos, por isso prosseguimos com o K=100.\
<img src= "https://github.com/fernandovs4/Desafio-Netflix/blob/main/histograma_diferencas.jpg">\

\
2 - Ademais, realizamos um teste de stress que consistia em aumentar cada vez mais a quantidade de ruídos na nossa matriz original para ver como seria o desempenho do nosso algoritmo em relação aos seus palpites. Realizamos esses testes para 1000, 10000, 10000 mil ruídos. Com isso percebemos que, assim como o esperado, quanto maior a quantidade de dados "estragados" pior seria a previsão.
As imagens abaixo mostra os resultados obtidos:


## Concluindo
Tendo em vista os resultados obtidos, notamos que apesar do nosso sistema em alguns momentos prever notas que se afastam bastante do que era esperado, grande parte das vezes ele retorna um valor interessante e que se aproxima do original. Dessa forma, acreditamos que seja possível alguns  testes e ajustes em relação à matriz sigma e na variável K para melhorar o nosso algoritmo e suas previsões, mas no geral o nosso sistema prevê de forma razoável a nota que o usuário daria para determinado filme, sendo então possível utilizá-lo como ferramenta auxiliar para recomendar filmes à um usuário.
