from string import ascii_letters
p_symbols = "#!\{}/+&@._§%?<>£;,:"
import random

def password_generator(length,symbols):
    if symbols:
        characters = ascii_letters + p_symbols
        password = "".join([random.choice(characters) for _ in range(length)])
        return password
    else:
        password = "".join([random.choice(ascii_letters) for _ in range(length)])
        return password