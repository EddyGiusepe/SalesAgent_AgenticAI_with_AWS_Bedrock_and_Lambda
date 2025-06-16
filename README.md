# <h1 align="center"><font color="gree">SalesAgent (Agentic AI) with AWS Bedrock and Lambda</font></h1>

<font color="pink">Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>

Neste tutorial, mostrei como criar um ``agente de IA`` com o ``AWS Bedrock`` e uma ``função Lambda`` passo a passo.


![](agent_sales_aws.drawio.png)

A seguir, você verá uma comparação entre a ``IA Agente`` e a ``IA Generativa``.

| IA Agente                                                                 | IA Generativa                                                  |
|---------------------------------------------------------------------------|----------------------------------------------------------------|
| Vai além da geração ao incluir autonomia, tomada de decisão e execução de tarefas | Foca na criação de novo conteúdo, como texto, imagens, música ou até código |
| Executa ações                                                            | Gera respostas                                                  |
| Salesforce Agentforce                                                    | ChatGPT, Gemini                                                |


## <font color="red">AWS CLI - Interface de Linha de Comando</font>

### <font color="blue">O que é o AWS CLI?</font>

O **AWS Command Line Interface (AWS CLI)** é uma ferramenta unificada de código aberto que permite gerenciar todos os seus serviços AWS através da linha de comando. Com ela, você pode:

- ✅ Controlar múltiplos serviços AWS com uma única ferramenta
- ✅ Automatizar tarefas usando scripts
- ✅ Ter funcionalidade equivalente ao Console Web da AWS
- ✅ Executar comandos diretamente do terminal

### <font color="blue">Principais Recursos</font>

- **Complementação com Tab**: Use a tecla Tab para autocompletar comandos
- **Prompts Automáticos**: Receba sugestões de comandos e parâmetros em tempo real
- **Histórico de Comandos**: Acesse comandos executados anteriormente com `aws history`

### <font color="blue">Como Usar o AWS CLI com o Cursor IDE</font>

Para integrar o AWS CLI com o Cursor IDE, siga estes passos:

1. **Instale o AWS CLI** no seu sistema:
   ```bash
   # No Linux/macOS
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

2. **Configure suas credenciais AWS**:
   ```bash
   aws configure
   ```
   Você precisará fornecer:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region (ex: us-east-1)
   - Default output format (ex: json)

3. **No Cursor IDE**, você pode:
   - Abrir o terminal integrado (`Ctrl+` `)
   - Executar comandos AWS diretamente
   - Criar scripts Python/JavaScript que usam o AWS SDK
   - Usar extensões como AWS Toolkit

### <font color="blue">Exemplos de Comandos Úteis</font>

```bash
# Listar buckets S3
aws s3 ls

# Listar funções Lambda
aws lambda list-functions

# Obter ajuda sobre um serviço
aws bedrock help

# Invocar uma função Lambda
aws lambda invoke --function-name MinhaFuncao output.json
```

### <font color="blue">Dicas para Desenvolvimento com Cursor + AWS</font>

1. **Use variáveis de ambiente** para suas credenciais em vez de hardcode
2. **Instale o AWS SDK** para sua linguagem preferida (boto3 para Python)
3. **Configure profiles** diferentes para ambientes dev/prod:
   ```bash
   aws configure --profile desenvolvimento
   aws configure --profile producao
   ```
4. **Use o terminal integrado do Cursor** para testar comandos rapidamente

### <font color="blue">🔍 Como Verificar se o AWS CLI já está Instalado</font>

Para verificar se você já tem o AWS CLI configurado, execute estes comandos:

1. **Verificar a versão instalada**:
   ```bash
   aws --version
   # Resultado esperado: aws-cli/2.x.x Python/3.x.x Linux/x.x.x
   ```

2. **Verificar suas credenciais configuradas**:
   ```bash
   aws configure list
   # Mostra as configurações atuais (access key, secret key, region, output)
   ```

3. **Testar a conexão com a AWS**:
   ```bash
   aws sts get-caller-identity
   # Retorna informações sobre sua identidade AWS (Account ID, User ID, ARN)
   ```

4. **Verificar os perfis configurados**:
   ```bash
   aws configure list-profiles
   # Lista todos os perfis AWS configurados
   ```

5. **Ver o conteúdo dos arquivos de configuração**:
   ```bash
   # No Linux/macOS
   cat ~/.aws/credentials
   cat ~/.aws/config
   
   # No Windows
   type %USERPROFILE%\.aws\credentials
   type %USERPROFILE%\.aws\config
   ```

6. **Verificar qual perfil está sendo usado**:
   ```bash
   echo $AWS_PROFILE
   # Se vazio, está usando o perfil default
   ```

**💡 Dica**: Se algum desses comandos retornar erro, significa que o AWS CLI não está instalado ou configurado corretamente.

### <font color="blue">🚨 Resolução de Problemas Comuns</font>  

#### Erro: `InvalidClientTokenId`

Se você receber este erro:
```
An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: 
The security token included in the request is invalid.
```

**Possíveis causas e soluções:**

1. **Credenciais expiradas ou inválidas**:
   ```bash
   # Reconfigure suas credenciais
   aws configure
   ```

2. **Verificar se as credenciais estão corretas**:
   ```bash
   # Ver as credenciais atuais (mascaradas)
   aws configure list
   
   # Editar manualmente as credenciais
   nano ~/.aws/credentials
   ```

3. **Usar um perfil específico**:
   ```bash
   # Listar perfis disponíveis
   cat ~/.aws/credentials | grep '\['
   
   # Usar um perfil específico
   export AWS_PROFILE=seu-perfil
   aws sts get-caller-identity
   ```

4. **Gerar novas credenciais no Console AWS**:
   - Acesse [Console AWS](https://console.aws.amazon.com/)
   - Vá em IAM → Users → Seu usuário
   - Security credentials → Create access key
   - Copie a nova Access Key ID e Secret Access Key
   - Execute `aws configure` novamente

5. **Verificar permissões do usuário IAM**:
   - Certifique-se que seu usuário tem as permissões necessárias
   - No mínimo, precisa da permissão `sts:GetCallerIdentity`

## <font color="red">📋 Guia Completo: Configurando AWS CLI do Zero</font>

### <font color="blue">Passo 1: Criar Conta AWS (se ainda não tiver)</font>

1. Acesse [aws.amazon.com](https://aws.amazon.com)
2. Clique em "Create an AWS Account"
3. Siga o processo de criação (precisará de cartão de crédito)

### <font color="blue">Passo 2: Obter suas Credenciais no Console AWS</font>

1. **Fazer Login no Console AWS**:
   - Acesse [console.aws.amazon.com](https://console.aws.amazon.com)
   - Entre com seu email e senha

2. **Acessar o IAM (Identity and Access Management)**:
   - No console AWS, procure por "IAM" na barra de busca
   - Ou acesse direto: [console.aws.amazon.com/iam](https://console.aws.amazon.com/iam)

3. **Criar um Usuário IAM** (recomendado - não use root):
   - No menu lateral, clique em **"Users"** → **"Add users"**
   - **User name**: Digite um nome (ex: `meu-usuario-cli`)
   - **Select AWS access type**: Marque ✅ **"Access key - Programmatic access"**
   - Clique em **"Next: Permissions"**

4. **Definir Permissões**:
   - Para desenvolvimento, você pode:
     - **Opção Rápida**: Clicar em **"Attach existing policies directly"** → Procurar e marcar **"AdministratorAccess"** (⚠️ use apenas para desenvolvimento)
     - **Opção Segura**: Criar políticas específicas para seu projeto
   - Clique em **"Next: Tags"** → **"Next: Review"** → **"Create user"**

5. **⚠️ IMPORTANTE - Salvar as Credenciais**:
   - Na tela de sucesso, você verá:
     - **Access key ID**: Algo como `AKIAIOSFODNN7EXAMPLE`
     - **Secret access key**: Clique em **"Show"** para revelar
   - **🔴 COPIE ESTAS CREDENCIAIS AGORA!** Você não poderá vê-las novamente
   - Opcionalmente, clique em **"Download .csv"** para salvar

### <font color="blue">Passo 3: Configurar o AWS CLI</font>

Agora no seu terminal, execute:

```bash
aws configure
```

Você será perguntado por 4 informações:

1. **AWS Access Key ID**: Cole o Access Key ID que você copiou
   ```
   AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
   ```

2. **AWS Secret Access Key**: Cole o Secret Access Key
   ```
   AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   ```

3. **Default region name**: Escolha a região mais próxima
   ```
   Default region name [None]: us-east-1
   ```
   
   **Regiões comuns**:
   - `us-east-1` - US East (N. Virginia) - Mais serviços disponíveis
   - `sa-east-1` - South America (São Paulo) - Mais próxima do Brasil
   - `us-west-2` - US West (Oregon)
   - `eu-west-1` - Europe (Ireland)

4. **Default output format**: Escolha o formato de saída
   ```
   Default output format [None]: json
   ```
   
   **Opções**: `json`, `yaml`, `text`, `table`

5. Testando o funcionamento do AWS CLI:
```bash
aws s3 ls
```


### <font color="blue">Passo 4: Testar a Configuração</font>

```bash
# Verificar se funcionou
aws sts get-caller-identity

# Resposta esperada:
{
    "UserId": "AIDACKCEVSQ6C2EXAMPLE",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/meu-usuario-cli"
}
```

### <font color="blue">Passo 5: Configurações Adicionais (Opcional)</font>

#### **Múltiplos Perfis**:
```bash
# Adicionar um novo perfil
aws configure --profile producao

# Usar um perfil específico
aws s3 ls --profile producao

# Ou definir como padrão temporariamente
export AWS_PROFILE=producao
```

#### **Verificar/Editar Configurações**:
```bash
# Ver configuração atual
aws configure list

# Editar diretamente os arquivos
nano ~/.aws/credentials
nano ~/.aws/config
```

### <font color="blue">🔒 Dicas de Segurança</font>

1. **Nunca compartilhe** suas credenciais AWS
2. **Não faça commit** dos arquivos `~/.aws/credentials` no Git
3. **Use políticas IAM** com permissões mínimas necessárias
4. **Rotacione suas chaves** regularmente
5. **Para produção**, use IAM Roles ao invés de Access Keys

### <font color="blue">🆘 Problemas Comuns</font>

- **"Unable to locate credentials"**: Execute `aws configure` novamente
- **"InvalidClientTokenId"**: Suas credenciais estão incorretas ou expiradas
- **"AccessDenied"**: Seu usuário não tem as permissões necessárias
- **Região incorreta**: Alguns serviços só funcionam em regiões específicas

### <font color="blue">🗑️ Como Deletar um Usuário IAM (Reverter Tudo)</font>

**Não tenha medo!** Você pode deletar usuários IAM a qualquer momento:

#### **Pelo Console AWS:**
1. Acesse [IAM Console](https://console.aws.amazon.com/iam)
2. Clique em **"Users"** no menu lateral
3. Selecione o usuário que quer deletar
4. Clique em **"Delete"** → Confirme digitando o nome do usuário

#### **Pelo AWS CLI:**
```bash
# Primeiro, delete as access keys do usuário
aws iam list-access-keys --user-name nome-do-usuario
aws iam delete-access-key --user-name nome-do-usuario --access-key-id AKIAIOSFODNN7EXAMPLE

# Depois, delete o usuário
aws iam delete-user --user-name nome-do-usuario
```

#### **Limpeza Completa (se quiser remover tudo):**
```bash
# Remover configurações locais do AWS CLI
rm -rf ~/.aws/credentials
rm -rf ~/.aws/config

# Ou remover apenas um perfil específico
aws configure --profile nome-do-perfil
# (deixe todos os campos em branco e pressione Enter)
```

### <font color="blue">💚 Por que é Seguro Testar:</font>

- ✅ **Gratuito**: IAM não tem custo
- ✅ **Reversível**: Delete quando quiser
- ✅ **Isolado**: Não afeta sua conta root AWS
- ✅ **Controlado**: Você define as permissões
- ✅ **Sem compromisso**: É só uma credencial de acesso

**Dica**: Comece com um usuário de teste com permissões mínimas. Quando se sentir confortável, crie um definitivo!






Thank God!