from rest_framework import status
from rest_framework.exceptions import APIException

class ShopBaseException(APIException):
    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.default_detail = detail
        self.status_code = code
