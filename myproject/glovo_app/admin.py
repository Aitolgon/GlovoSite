from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

@admin.register(Product, Category,)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class AddressInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Address
    extra = 1

class ContactInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Contact
    extra = 1

class StoreMenuInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = StoreMenu
    extra = 1


@admin.register(Store)
class StoreAdmin(TranslationAdmin, NestedModelAdmin):
    inlines = [AddressInline, ContactInline, StoreMenuInline]
    class Media:
                js = (
                    'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                    'modeltranslation/js/tabbed_translation_fields.js',
                )
                css = {
                    'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
                }


admin.site.register(UserProfile)
admin.site.register(CourierProduct)
admin.site.register(Order)
admin.site.register(Review)

