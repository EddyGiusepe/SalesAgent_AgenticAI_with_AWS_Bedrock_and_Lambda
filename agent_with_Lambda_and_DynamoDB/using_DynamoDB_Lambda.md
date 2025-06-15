# <h1 align="center"><font color="gree">Agente integrado com a função Lambda e consultando o DynamoDB</font></h1>

<font color="pink">Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>



## <font color="red">Índice</font>
- [Introdução](#introdução)
- [Criando IAM Role](#criando-iam-role)
- [Acessando o Bedrock](#acessando-o-bedrock)
- [Função Lambda](#função-lambda)
- [Criando uma Tabela no DynamoDB](#criando-uma-tabela-no-dynamodb)
- [Testando meu Agente na UI da AWS](#testando-meu-agente-na-ui-da-aws)


## <font color="red">Introdução</font>

Aqui vamos criar um `Agente` que vai consultar pelo telefone de um cliente em um banco de dados no `DynamoDB` e retornar uma resposta.


## <font color="red">Criando IAM Role</font>

Nesta sessão vamos criar uma `IAM Role` para que a nossa `Função Lambda` possa acessar ao `DynamoDB`.
Criamos o seguinte `IAM Role`: eddyDynamoLambda-Role, com as seguintes permissões: AmazonBedrockFullAccess, AmazonDynamoDBFullAccess, AmazonLambdaFullAccess e AmazonCloudWatchLogsFullAccess.


## <font color="red">Acessando o Bedrock</font>

Acessamos ao Bedrock e criamos nosso agente com o seguinte modelo e instruções:

![](./Agent_Lambda_Dynamo_Bedrock.jpeg)


## <font color="red">Função Lambda</font>

Aqui criamos nossa função Lambda para receber a consulta do agente e retornar uma resposta.
Ver em anexo o código: `function_lambda.py`


## <font color="red">Criando uma Tabela no DynamoDB</font>

Nos criamos uma tabela chamada: `agenda_contatos` e com três itens. Ver o gráfico a seguir:

![](./Table_DynamoDB.jpeg)


## <font color="red">Testando meu Agente na UI da AWS</font>

Eu testo meu Agente na UI da AWS com clientes que tem telefone registrado na minha tabela do `DynamoDB`.
O resultado é o seguinte:

![](./Testando_meu_Agente.jpeg)







Thank God!