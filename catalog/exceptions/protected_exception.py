from rest_framework import status
from .base_exception import ShopBaseException

class ShopDeleteProtectedException(ShopBaseException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
