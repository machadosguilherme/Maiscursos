import json
from datetime import datetime
import boto3


dynamodb = boto3.resource('dynamodb')
tabelaenvio = dynamodb.Table('enviologin')


def lambda_handler(event, context):
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    nome = str(event['nome'])
    email = str(event['Email'])
    telefone = str(event['Telefone'])
    mensagem = str(event['Mensagem'])


    try:
        tabelaenvio.put_item(
            Item={
                'nome': nome,
                'data_hora': data_hora,
                'email': email,
                'telefone': telefone,
                'mensagem': mensagem
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Cadastro realizado por '
                               + nome
                               + ' com os contatos '
                               + email
                               + telefone
                               + ' e a mensagem '
                               + mensagem
                               + ' inserido no Banco de Dados')
        }
    except:
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
