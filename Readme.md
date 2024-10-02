# Previsão de reclamação negativa no [Consumidor.gov](https://www.consumidor.gov.br)

<center>

<img  src='utilities/img/consumidor-gov.jpg' alt='Banner com o logo  do  Consumidor.Gov'>

  
</center>

##  Visão Geral

Este desenvolve um modelo preditivo que ajuda empresas a identificar potenciais avaliações negativas de consumidores em relação a reclamações registradas no site [Consumidor.gov](https://www.consumidor.gov.br). 

A partir dessa identificação, a empresa pode tomar medidas preventivas para mitigar a insatisfação.

O foco está nas reclamações do segmento de fabricantes de produtos eletrônicos, e os dados abrangem um período de 12 meses, de **julho de 2023 a junho de 2024**.


## Descrição das variáveis

- **Região**: Região geográfica do Brasil.
- **UF**: Estado da federação.
- **Cidade**: Nome da cidade do consumidor.
- **Sexo**: Gênero do consumidor.
- **Faixa Etária**: Faixa etária do consumidor.
- **Data Finalização**: Data em que a reclamação foi finalizada.
- **Tempo Resposta**: Tempo em dias para resposta da empresa.
- **Nome Fantasia**: Nome comercial da empresa.
- **Segmento de Mercado**: Setor de atuação da empresa.
- **Como Comprou/Contratou**: Meio de aquisição do produto ou serviço.
- **Procurou Empresa**: Indica se o consumidor tentou resolver o problema diretamente com a empresa.
- **Respondida**: Se a empresa respondeu à reclamação.
- **Situação**: Status atual da reclamação (resolvida, não resolvida).
- **Avaliação Reclamação**: Avaliação do consumidor sobre a resolução da reclamação.
- **Nota do Consumidor**: Nota dada pelo consumidor (1 a 5).

## Modelos utilizaados

Os seguintes modelos foram utilizados para resolução desse problema:

- **Random Forest**
- **XGBoost**
- **SGD Classifier**
- **LightGBM**
- **Naive Bayes**
- **SVM**
- **KNN**

Os modelos com melhores resultados em termos de precisão e recall para identificar potenciais avaliações negativas foram:

- **Naive Bayes**
- **LightGBM**
- **XGBoost**

## Limitações

* **Dados:** Os dados utilizados nesta análise são referentes ao primeiro semestre de 2024 e podem não ser representativos de outros períodos.
* **Causalidade:** O modelo pode identificar correlações, mas não estabelece relações de causa e efeito. 


## Conclusões

O projeto fornece uma ferramenta poderosa para empresas que desejam monitorar e agir sobre reclamações de clientes, especialmente no contexto de avaliações negativas. 

O próximo passo é a integração desse modelo com um sistema de alerta que ajude as empresas a identificar reclamações com alto risco de insatisfação.
