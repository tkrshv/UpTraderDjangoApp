from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name="Menu Title", unique=True)
    slug = models.SlugField(max_length=255, verbose_name="Menu Slug")

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name="Item Title")
    slug = models.SlugField(max_length=255, verbose_name="Item Slug")
    menu = models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.title