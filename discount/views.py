# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from discount.models import Company
# from discount.serializers import CompanyListSerializer2


from discount.operations import get_company_dto
from discount.serializers import CompanyDtoSerializer
from rest_framework.generics import ListAPIView


class DiscountList(ListAPIView):
    queryset = get_company_dto()
    print(queryset)
    serializer_class = CompanyDtoSerializer

class DiscountDetail(ListAPIView):
    pass
