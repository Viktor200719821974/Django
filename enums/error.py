from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ('Token expired or invalid', status.HTTP_403_FORBIDDEN)
    VLE1 = 'The email must be set'
    VLE2 = 'Superuser must have is_staff=True'
    VLE3 = 'Superuser must have is_superuser=True'
    BOOLE = 'Value must be 0 and 1'

    def __init__(self, msg, code=status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.code = code
