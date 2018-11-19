from django.contrib import admin
from core.models import Products, TelescopeType#, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'telescope_type')#, 'get_total')
    search_fields = ('name', 'telescope_type__name')

#    def get_total(self, obj):
#        return obj.price * obj.count
#    get_total.short_description = 'Total'

admin.site.register(Products, ProductAdmin)
admin.site.register(TelescopeType)
#admin.site.register(Tag)