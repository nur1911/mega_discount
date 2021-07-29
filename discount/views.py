# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from discount.models import Company
# from discount.serializers import CompanyListSerializer2


from discount.operations import get_company_dto, get_company_detail_dto
from discount.serializers import CompanyDtoSerializer, CompanyDetailSerializer
from rest_framework.generics import ListAPIView
from rest_framework import pagination


class DiscountList(ListAPIView):
    queryset = get_company_dto()
    serializer_class = CompanyDtoSerializer
    pagination_class = pagination.LimitOffsetPagination

class DiscountDetail(ListAPIView):
    queryset = get_company_detail_dto()
    serializer_class = CompanyDetailSerializer
    pagination_class = pagination.LimitOffsetPagination

