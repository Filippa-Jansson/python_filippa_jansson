
#Använder denna kod till execise 6, för att visa att man kan importera kod
from numbers import Number

def validate_positive_number(value) -> bool:

    if not isinstance(value, Number):
        raise TypeError(f"the value must be a Number not a {type(value)}")
    
    if value < 0:
        raise ValueError(f"Value must be larger than 0 not {value}")