from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomException(APIException):
    status_code = 400
    default_detail = {'response': 'Something went wrong'}


success = Response(data={'response': "Success"}, status=200)
error = CustomException({'response': "Xatolik yuz berdi"})
none = CustomException({'response': "Kiritilganlar bo'yicha malumot topilmadi"})
value_e = CustomException({'response': "Malumotlarni to'g'ri shakilda jo'nating"})
restricted = CustomException({'response': "Bu amaliyot uchun sizda ruhsat mavjud emas"})
