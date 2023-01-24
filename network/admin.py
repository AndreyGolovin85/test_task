from django.contrib import admin

from network.models import Network, Products, Contacts


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'products',)
    actions = ['clear_arrears']


@admin.register(Contacts)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('country',)


@admin.register(Products)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('title',)


def clear_arrears(modeladmin, request, queryset):
    for network in queryset:
        network.debt = 0
        network.save()
