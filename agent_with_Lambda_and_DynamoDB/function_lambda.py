#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    try:
        agent = event["agent"]
        actionGroup = event["actionGroup"]
        function = event["function"]
        parameters = event.get("parameters", {})

        table_name = "agenda_contatos"
        table = dynamodb.Table(table_name)

        nome_contato = next(
            (param["value"] for param in parameters if param["name"] == "nome_contato"),
            None,
        )

        if not nome_contato:
            responseBody = {"TEXT": {"body": "Por favor, forneça o nome do contato."}}
        else:
            try:
                # Tente obter o item usando scan em vez de get_item:
                print(f"Buscando contato: {nome_contato.lower()}")

                scan_response = table.scan(
                    FilterExpression=boto3.dynamodb.conditions.Attr("id").eq(
                        nome_contato.lower()
                    )
                )

                items = scan_response.get("Items", [])

                if items:
                    # Item encontrado:
                    responseBody = {"TEXT": {"body": items[0]["telefone"]}}
                else:
                    # Item não encontrado
                    responseBody = {
                        "TEXT": {
                            "body": f"Desculpe, não consegui encontrar o número de telefone de {nome_contato}. O cliente não foi encontrado no banco de dados."
                        }
                    }
            except Exception as e:
                print(f"Erro ao buscar contato: {str(e)}")
                responseBody = {
                    "TEXT": {"body": f"Ocorreu um erro ao buscar o contato: {str(e)}"}
                }

        action_response = {
            "actionGroup": actionGroup,
            "function": function,
            "functionResponse": {"responseBody": responseBody},
        }

        dummy_function_response = {
            "response": action_response,
            "messageVersion": event["messageVersion"],
        }
        print("Response: {}".format(dummy_function_response))

        return dummy_function_response

    except Exception as e:
        print(f"Erro geral na função: {str(e)}")
        return {
            "response": {
                "actionGroup": event.get("actionGroup", ""),
                "function": event.get("function", ""),
                "functionResponse": {
                    "responseBody": {
                        "TEXT": {"body": f"Ocorreu um erro no processamento: {str(e)}"}
                    }
                },
            },
            "messageVersion": event.get("messageVersion", "1.0"),
        }
