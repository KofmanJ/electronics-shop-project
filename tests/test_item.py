"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError
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

def test_repr():
    item = Item("Телефон", 15000, 30)
    assert item.__repr__() == "Item('Телефон', 15000, 30)"

def test_str():
    item = Item("Телефон", 15000, 30)
    assert item.__str__() == "Телефон"

def test_add():
    item = Item("Телефон", 15000, 30)
    assert item + item == 60


def test_instantiate_from_csv_not_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/iteml.csv')


def test_instantiate_from_csv_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/item.csv')
