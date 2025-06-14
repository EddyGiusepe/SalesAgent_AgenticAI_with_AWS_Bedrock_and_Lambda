#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

def lambda_handler(event, context):
        agent = event['agent']
        actionGroup = event['actionGroup']
        function = event['function']
        parameters = event.get('parameters', [])

        def process_return(orderNumber):
            # Call the return API
            message = "The item was returned successfully."
            print(message)

        responseBody = {}
        if function == "process_return":
            # Extract the orderNumber from the parameters
            orderN = "abc123"
            process_return(orderN)
            responseBody = {
                "TEXT": {
                    "body": "Process Return function was called successfully."
                }
            }
        
        else:
            responseBody = {
                "TEXT": {
                    "body": "The order function {} was called successfully!".format(function)
                }
            }