import requests
from requests import codes
from parser import parse_user_input


def do_http_request(make_request, on_success, on_failure):
    try:
        request = make_request()
        if request.status_code == codes.ok:
            data = request.json()
            on_success(data)
        else:
            on_failure()
    except Exception:
        on_failure()


def default_failure_handler():
    print('Unexpected error while performing the operation. Please, try again later.')

class CalculadoraClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def _get_request_url(self, route):
        return f'{self.server_url}{route}'

    def list_active_api_endpoints(self):
        def on_success(response_json):
            for endpoint in response_json:
                print(f'Endpoint: {endpoint["endpoint"]}')

        def make_request(): return requests.get(self._get_request_url('/operacoes'))

        do_http_request(make_request, on_success, default_failure_handler)

    def sum(self, a, b):
        def make_request(): return requests.post(self._get_request_url(f'/operacoes/soma/{a}/{b}'))

        def on_success(response_json):
            error, value = response_json['error'], response_json['value']
            is_success = not error
            if is_success: 
                print(f'{a} + {b} = {value}')
            else:
                print('Unexpected error on the server performing the operation. Please, try again later')

        do_http_request(make_request, on_success, default_failure_handler)

    def subtract(self, a, b):
        def make_request(): return requests.post(self._get_request_url(f'/operacoes/subtrai/{a}/{b}'))

        def on_success(response_json):
            error, value = response_json['error'], response_json['value']
            is_success = not error
            if is_success: 
                print(f'{a} - {b} = {value}')
            else:
                print('Unexpected error on the server performing the operation. Please, try again later')

        do_http_request(make_request, on_success, default_failure_handler)

    def multiply(self, a, b):
        def make_request(): return requests.post(self._get_request_url(f'/operacoes/multiplica/{a}/{b}'))

        def on_success(response_json):
            error, value = response_json['error'], response_json['value']
            is_success = not error
            if is_success: 
                print(f'{a} * {b} = {value}')
            else:
                print('Unexpected error on the server performing the operation. Please, try again later')

        do_http_request(make_request, on_success, default_failure_handler)

    def divide(self, a, b):
        def make_request(): return requests.post(self._get_request_url(f'/operacoes/divide/{a}/{b}'))

        def on_success(response_json):
            error, value = response_json['error'], response_json['value']
            is_success = not error
            if is_success: 
                print(f'{a} / {b} = {value}')
            else:
                print('Unexpected error on the server performing the operation. Please, try again later')

        do_http_request(make_request, on_success, default_failure_handler)
