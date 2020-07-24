from django.urls import path
from . import views

app_name = 'shop'

urlpatterns=[
    path('arhives/<yyyy:year>/', views.archives_year, name='archive_year'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('', views.item_list, name='item_list'),
    path('new/', views.item_new, name='item_new'),
]