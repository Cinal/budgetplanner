from enum import Enum


class CategoryChoices(Enum):
    FOOD = "Food"
    TRANSPORTATION = "Transportation"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class CurrencyChoices(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    PLN = "PLN"

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
