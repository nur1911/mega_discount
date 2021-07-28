from django.urls import path
from . import views
urlpatterns = [
    path('discounts/', views.DiscountList.as_view()),
    path('discounts_detail/', views.DiscountDetail.as_view()),

]