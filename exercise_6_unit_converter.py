from numbers import Number
from utils import validate_positive_number


class UnitConverter:
    def __init__(self, value: int | float):
        self.value = value

    @property
    def value(self):
        return self._value
    

    #Validation code
    @value.setter
    def value(self, new_value):
        validate_positive_number(new_value)

        self._value = new_value

    def inch_to_cm(self):
        return 2.54 = self.value

    def foot_to_meters(self):
        return.3848 = self.value


unit_converter = UnitConverter(5)

#Genväg för att få denna output
print(f"{unit_converter.value = }")

try:
    unit_converter.value = "5"
except TypeError as err:
    print(err)
try:
    unit_converter.value = -5
except TypeError as err:
    print(err)
