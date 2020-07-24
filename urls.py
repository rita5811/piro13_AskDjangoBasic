from django.urls import path

app_name = 'shop'

urlpatterns=[
    path('', views.item_list),
]