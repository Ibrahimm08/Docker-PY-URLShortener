# Helper functions
from datetime import datetime
from dateutil.relativedelta import relativedelta
import string, random


# Generates a 6 character string with numbers and letters
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


# Splits lifetime to check if its days or months to add, then adds days/months to get expiry_date
def add_time(lifetime: str):
    unit, value = lifetime.split()
    value = int(value)

    # Turn into object to easily enter as argument rather than using if else statements
    args = {unit: value}  # example {"days": 5}

    return (datetime.now() + relativedelta(**args))