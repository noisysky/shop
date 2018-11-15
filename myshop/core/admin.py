from django.contrib import admin
from core.models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'type')#, 'get_total')
    search_fields = ('name', 'trade_mark__name')

#    def get_total(self, obj):
#        return obj.price * obj.count
#    get_total.short_description = 'Total'

admin.site.register(Products, ProductAdmin)