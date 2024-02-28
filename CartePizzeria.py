from CartePizzeriaException import CartePizzeriaException

class CartePizzeria:

    def __init__(self, pizzas):
        pizzas = []
        self.pizzas = pizzas

    def is_empty(self):
        if (len(self.pizzas) == 0) :
            return True

    def nb_pizzas(self):
        print("len is:", len(self.pizzas))
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.nom == name :
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException("Pizza not found") 



