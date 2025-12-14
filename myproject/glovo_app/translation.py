from .models import (Product, Category, Contact, Address, Store, StoreMenu,)
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_description',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('contact_name',)

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address_name',)

@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description',)

@register(StoreMenu)
class StoreMenuTranslationOptions(TranslationOptions):
    fields = ('menu_name',)