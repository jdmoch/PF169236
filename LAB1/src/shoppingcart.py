class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name: str, price: float, qty: int = 1):
        if name in self.items:
            self.items[name]['qty'] += qty
        else:
            self.items[name] = {'price': price, 'qty': qty}

    def remove(self, name: str, qty: int = None):
        if name in self.items:
            if qty is None or qty >= self.items[name]['qty']:
                del self.items[name]
            else:
                self.items[name]['qty'] -= qty

    def total(self) -> float:
        return round(sum(item['price'] * item['qty'] for item in self.items.values()), 2)

    def clear(self):
        self.items.clear()

    def show(self):
        if not self.items:
            print("Koszyk jest pusty.")
        else:
            for name, details in self.items.items():
                print(f"- {name}: {details['qty']} szt. x {details['price']} zł")
            print(f"Łączna wartość: {self.total()} zł")