from enums.error import ErrorEnum
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exeption_handler(exe, content) -> Response:
    handlers = {
        'JwtExseption': _jwt_validate_error
    }
    response = exception_handler(exe, content)
    exe_class = exe.__class__.__name__

    if exe_class in handlers:
        return handlers[exe_class](exe, content)

    return response


def _jwt_validate_error(exe, content) -> Response:
    print(exe.__class__)
    print(content)
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
