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
