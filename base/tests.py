from django.test import TestCase

from base.models import Menu, Item


class MainMenuTestCase(TestCase):
    def setUp(self) -> None:
        menu = Menu.objects.create(title="main_menu", slug="main_menu")
        future_parent = Item.objects.create(title="item_1", slug="item1", menu=menu)
        Item.objects.create(title="item_2", slug="item2", menu=menu, parent=future_parent)

    def test_main_menu_exists(self):
        main_menu = Menu.objects.get(title="main_menu")

        self.assertIsNotNone(main_menu, "Menu not found")

    def test_main_menu_have_items(self):
        main_menu = Menu.objects.get(title="main_menu")

        self.assertIsNotNone(main_menu.items, "Menu doesn't have items")

    def test_item_have_parent(self):
        second_item = Item.objects.get(title="item_2")
        first_item = Item.objects.get(title="item_1")

        self.assertIsNotNone(second_item, "The second Item not found")
        self.assertIsNotNone(first_item, "The first item not found")
        self.assertIsNotNone(second_item.parent, "Not found second item parent")

        self.assertEqual(second_item.parent, first_item, "The first item not equals parent second item")
