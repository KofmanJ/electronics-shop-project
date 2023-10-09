"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest


@pytest.fixture
def item_test():
    return Item("Телефон", 40000, 3)


def test_calculate_total_price(item_test):
    """
    Возвращает общую стоимость товара в магазине
    """
    assert item_test.calculate_total_price() == 120000


def test_apply_discount(item_test):
    """
    Возвращает стоимость товара в магазине с применением установленной скидки
    """
    Item.pay_rate = 0.8
    assert item_test.apply_discount() == 32000

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('1.0') == 1
    assert Item.string_to_number('6.5') == 6


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'
    assert item.name != 'СуперСмар'