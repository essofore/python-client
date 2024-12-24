from http import HTTPStatus
import locale

# Set the locale to the user's default
locale.setlocale(locale.LC_ALL, '')

def is_4xx(response):
    return response.status_code == HTTPStatus.BAD_REQUEST or response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

def handle_http_error(response):
    if is_4xx(response):
        x = response.parsed
        print(x.message)
        if hasattr(x, 'violations'):
            print(x.violations)
    else:
        print('Error:', response.status_code)

def format_int(x):
    return locale.format_string("%d", x, grouping=True)
