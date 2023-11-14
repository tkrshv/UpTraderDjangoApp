from django.contrib import admin

from base.models import Menu, Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Add new item', {
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
            )
