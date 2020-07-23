from django.urls import path
from askcompany.shop import views

app_name = 'shop'

urlpatterns=[
    path('items/', item_list, name='item_list'),
]