# <h1 align="center"><font color="gree">A Guide to Building ChatGPT on AWS</font></h1>

<font color="pink">Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>


## <font color="red">Introduction</font>
Aqui vamos criar um serviço similar ao ChatGPT, onde você pode fazer queries e receber respostas.
Basicamente, usaremos o PROMPT para chamar o modelo de AI em segundo plano, gerar uma resposta e retornar para o usuário/cliente.
Temos, uma API Gateway que recebe a sua requisição, depois chama à função lambda, depois a função lambda chama ao bedrock (em segundo plano) e depois retorna a resposta para o usuário/cliente. O seguinte gráfico ilustra o processo:


![](./Building_a_chatGPT_on_AWS.drawio.png)


## <font color="red">Criando nosso ``IAM Role``</font>

Vamos criar uma função IAM para que a nossa Função Lambda possa acessar o Bedrock e CloudWatchLogs.



























Thank God!