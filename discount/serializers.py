from rest_framework import serializers

from .models import Company, Discount, Adress, City, View


# class CompanySerializer(serializers.Serializer ):
#     name = serializers.CharField( max_length=30)
#     photo = serializers.URLField()
#     description = serializers.TextField()


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class ViewSerializer(serializers.Serializer):
    count = serializers.IntegerField()

class CompanyDtoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    photo = serializers.URLField()
    description = serializers.CharField(max_length=1000)
    discount_percent = serializers.IntegerField()
    city = serializers.CharField(max_length=10)
    view_count = serializers.IntegerField()










# class CompanyListSerializer2(serializers.ModelSerializer):
#
#     discount = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)
#     view = serializers.IntegerField()
#
#
#     class Meta:
#         model = Company
#         exclude = ("working_hours","phone","categori","pin","reviews","adress","id")





