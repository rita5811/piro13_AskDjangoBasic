from django.db import models
from django.views.generic import ListView
from askcompany.shop.models import Item

class ItemListView(ListView):
    model = Item
    item_list = ItemListView.as_view()
# Create your models here.
