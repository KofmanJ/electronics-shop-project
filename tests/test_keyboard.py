from src.keyboard import Keyboard


def test_1():
    new_test = Keyboard('Keyboard', 13000, 33)
    assert str(new_test) == 'Keyboard'
    assert str(new_test.language) == "EN"
    new_test.change_lang()
    assert str(new_test.language) == "RU"
