# Introduction 
Ao fazer a análise exploratória foi percebida a existência de pequenas inconsistências que foram efetivamente ajustadas para melhorar a interpretação dos dados.

O primeiro step consistiu em avaliar as variáveis que estavam dentro do dataset para verificar seu formato, critério, distribuição e a existência de dados faltantes. Comprovamos que algumas colunas não adicionavam informação, pelo que foram removidas. Seguidamente, foi feito um tratamento sobre os outliers, onde foi aplicada a regra dos 3 desvios para eliminá-los. 

Procedimentos de feature engineering foram feitos para discretizar alguns campos, além disso, fizemos o procedimento de One Hot Enconding e O balanceamento do dataset com a técnica Random Under Sampler

Os dados foram separados entre treino e teste, onde 80% dos dados foram selecionados para treinar o modelo. Assim, foi escolhido o XGBoost como modelo a ser utilizado para treinar e fazer as predições. Dentre os motivos para sua escolha encontram-se a rapidez do treino, a facilidade de usar em conjunto com outras libraries como sklearn, sua boa documentação. Em adição, este algoritmo permite definir uma métrica de avaliação a ser aprimorada após cada iteração; no caso foi escolhido o ROC.

A seleção dos hiperparâmetros foi feita em conjunto com GridCV, componente baseado em força bruta para escolher os melhores hipeparâmetros com base nas escolhas prévias.

Após o treino encontramos que as métricas reportadas em termos de F1-score, precision, recall, acurácia e AUC foram favoráveis, olhando para o precision e recall por grupo para achar o melhor threshold de separação entre as classes. Assim, decidiu-se que o melhor ponto de corte em 45%.

Finalizada a modelage, encontramos o maior preditor utilizando feature importance, a variável faixa_etaria. Porém é importante citar a presença das varíaveis black list e segment market.

Dentro das cinco principais preditoras, uma sobre a qual poderia se trabalhar é origem do canal de comunicação utilizaod pelo cliente. Essa variável, pode ser enriquecida por bases externas, além disso, é interessante associar o engajamento do usuário, histórico, LTV, base de créditos e dessa forma aumentar a possibilidade de conversão de venda.


* [Fluxograma do projeto Orçamento de exames](https://miro.com/app/board/uXjVOtcTIbY=/)


# Getting Started

* pip install requirements.txt 



# Build and Test
 
# Build and deploy

Acessar o projeto e rodar a aplicação atráves do comando
```
python run.py
```


