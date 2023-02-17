from rest_framework.views import exception_handler
from datetime import datetime

def shop_exception(exc, context):
    response = exception_handler(exc, context)
    response.data['time'] = datetime.now()
    return response
