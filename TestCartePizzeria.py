import unittest
from unittest.mock import Mock
from unittest.mock import patch

from Pizza import Pizza
from CartePizzeriaException import CartePizzeriaException

from CartePizzeria import CartePizzeria

class TestCartePizzeria(unittest.TestCase):
    
    def setUp(self):
        pizzas = []
        pizzas2 = []
        self.cartePizzeriaEmpty = CartePizzeria(pizzas)
        self.cartePizzeriaNotEmpty = CartePizzeria(pizzas2)

        nom = "4 fromages"
        ingredients = ["lait","fromage"]
        prix = 10

        pizza_4fromage = Pizza(nom, ingredients, prix)
        self.cartePizzeriaNotEmpty.add_pizza(pizza_4fromage)


    def test_is_empty(self):
        """Test that pizzas is empty"""
        self.assertTrue(self.cartePizzeriaEmpty.is_empty())
        self.assertFalse(self.cartePizzeriaNotEmpty.is_empty())

    def test_nb_pizzas(self):
        print("test :", self.cartePizzeriaEmpty.nb_pizzas)
        # self.assertTrue(self.cartePizzeriaNotEmpty.nb_pizzas == 1)
        self.assertTrue(self.cartePizzeriaEmpty.nb_pizzas() == 0)
        self.assertTrue(self.cartePizzeriaNotEmpty.nb_pizzas() == 1)
    
    @patch("CartePizzeria.nb_pizzas")
    def test_nb_pizzas2(self, mock_nb_pizzas):
        mock_nb_pizzas.return_value = 1
        self.assertEqual(self.cartePizzeriaNotEmpty.nb_pizzas(), 1)


    def test_add_pizza(self):
        # pizza = Pizza("4 fromages", ["fromage", "mozzarella"], 10)
        pizza = Mock()
        self.cartePizzeriaNotEmpty.add_pizza(pizza)
        self.assertIn(pizza, self.cartePizzeriaNotEmpty.pizzas)

    def test_remove_existing_pizza(self):
        pizza = Pizza("2 fromages", ["cheese", "mozzarella"], 10)
        self.cartePizzeriaNotEmpty.add_pizza(pizza)
        self.cartePizzeriaNotEmpty.remove_pizza("2 fromages")
        self.assertNotIn(pizza, self.cartePizzeriaNotEmpty.pizzas)
    
    def test_remove_non_existing_pizza(self):
        with self.assertRaises(CartePizzeriaException):
            self.cartePizzeriaNotEmpty.remove_pizza("Margherita")

    @patch.object(CartePizzeria, 'remove_pizza')
    def test_remove_non_existing_pizza2(self, mock_remove_pizza):
        mock_remove_pizza.side_effect = CartePizzeriaException("Pizza not found")
        with self.assertRaises(CartePizzeriaException):
            self.cartePizzeriaNotEmpty.remove_pizza("Margherita")

if __name__ == "__main__":
  unittest.main()