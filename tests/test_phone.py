from src.phone import Phone

def test_str():
    phone1 = Phone("iPhone 15", 150_000, 10, 2)
    assert str(phone1) == 'iPhone 15'

def test_repr():
    phone1 = Phone("iPhone 15", 150_000, 10, 2)
    assert repr(phone1) == "Phone('iPhone 15', 150000, 10, 2)"

def test_number_of_sim():
    phone1 = Phone("iPhone 15", 150_000, 10, 2)
    assert phone1.number_of_sim == 2
