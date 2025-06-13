import random
import string

def generate_unique_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_unique_codes_for_user(user, total_codes=10):
    codes = set()
    
    # Garante que sejam únicos mesmo antes de salvar
    while len(codes) < total_codes:
        codes.add(generate_unique_code())

    print(codes)

create_unique_codes_for_user('')
