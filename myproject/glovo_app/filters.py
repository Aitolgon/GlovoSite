from django_filters import FilterSet
from .models import Product, Store



class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = {
             'category': ['exact'],
             'created_date': ['gt', 'lt',],
        }

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt'],

        }