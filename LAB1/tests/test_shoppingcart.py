import unittest
from src.shoppingcart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add("Kebab", 2.69, 4)
        self.assertEqual(self.cart.items["Kebab"], {"price": 2.69, "qty": 4})

    def test_remove_item(self):
        self.cart.add("Energol", 3.11, 4)
        self.cart.remove("Energol", 2)
        self.assertEqual(self.cart.items["Energol"], {"price": 3.11, "qty": 2})

        self.cart.remove("Energol", 2)
        self.assertNotIn("Energol", self.cart.items)

    def test_get_total(self):
        self.cart.add("Woda", 1.50, 10)
        self.cart.add("Sterydy", 100.00, 12)
        self.assertEqual(self.cart.total(), 1215.0)

    def test_clear(self):
        self.cart.add("Kebab", 1.25, 6)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)


if __name__ == "__main__":
    unittest.main()
