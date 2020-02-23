class Cashier(object):
    n = 0
    now_n = 0
    discount = 0
    products = None
    prices = None

    def __init__(self, n, discount, products, prices):
        self.n = n
        self.prices = prices
        self.discount = discount
        self.products = products

    def getBill(self, product, amount):
        self.now_n += 1
        price = 0

        for i in range(len(product)):
            for item_index in range(len(self.products)):
                if product[i] == self.products[item_index]:
                    price += (self.prices[item_index] * amount[i])
                    break

        if self.now_n == self.n:
            price = price - (self.discount * price) / 100
            self.now_n = 0
        return round(price, 2)

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)


if __name__ == '__main__':
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    print(cashier.getBill([1, 2], [1, 2]))
    print(cashier.getBill([3, 7], [10, 10]))
    print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
    print(cashier.getBill([4], [10]))
    print(cashier.getBill([7, 3], [10, 10]))
    print(cashier.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
    print(cashier.getBill([2, 3, 5], [5, 3, 2]))
