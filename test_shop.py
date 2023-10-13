"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_cart(self, cart,  product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 10)
        assert cart.products[product] == 11


    def test_del_card(self, cart , product):
        cart.add_product(product, 10)
        cart.remove_product(product, 9)
        assert cart.products[product] == 1
        cart.remove_product(product, 2)
        assert product not in cart.products.keys()
        cart.add_product(product, 10)
        cart.remove_product(product, 10)
        assert product not in cart.products
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products



    def test_clear_card(self, cart , product):
        cart.add_product(product, 10)
        cart.clear()
        assert product not in cart.products.keys()


    def test_total_price(self, cart, product):
        cart.add_product(product, 7)
        assert cart.get_total_price() == 100 * 7


    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        old_quantity = product.quantity
        cart.buy()
        assert old_quantity == product.quantity + 10
        cart.add_product(product, 1000)
        with pytest.raises(ValueError) as excinfo:
            cart.buy()
        assert excinfo.typename == 'ValueError'