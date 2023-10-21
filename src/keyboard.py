from src.item import Item


class MixinLog:
    """Класс для создания дополнительного функционала клавиатуры"""

    LANGUAGE = 'EN'

    def __init__(self):
        self.language = self.LANGUAGE


class Keyboard(Item, MixinLog):
    """Создание возможности по смене языка клавиатуры"""
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)
        self.language = language

    def change_lang(self):
        """Изменение языка клавиатуры"""
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self.language
