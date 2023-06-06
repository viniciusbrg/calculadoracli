import os

from parser import parse_user_input
from client import CalculadoraClient
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get('API_URL')

operation, operands_list = parse_user_input()
calculadora = CalculadoraClient(API_URL)

choices = {
    'list-operations': calculadora.list_active_api_endpoints,
    'sum': lambda : calculadora.sum(operands_list[0], operands_list[1]),
    'subtract': lambda : calculadora.subtract(operands_list[0], operands_list[1]),
    'multiply': lambda : calculadora.multiply(operands_list[0], operands_list[1]),
    'divide': lambda : calculadora.divide(operands_list[0], operands_list[1])
}

choices[operation]()
