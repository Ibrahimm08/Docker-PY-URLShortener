# Helper functions

import string, random


# Generates a 6 character string with numbers and letters
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
