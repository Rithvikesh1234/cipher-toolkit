"""Cipher Toolkit - Classic encryption algorithms."""
import string

def caesar(text, shift, decrypt=False):
    shift = -shift if decrypt else shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

def vigenere(text, key, decrypt=False):
    key = key.lower()
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - ord("a")
            result.append(caesar(ch, shift, decrypt))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

def rot13(text):
    return caesar(text, 13)

def atbash(text):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr(base + 25 - (ord(ch) - base)))
        else:
            result.append(ch)
    return "".join(result)

if __name__ == "__main__":
    msg = "Hello, World!"
    print(f"Original : {msg}")
    print(f"Caesar+3 : {caesar(msg, 3)}")
    print(f"Vigenere : {vigenere(msg, 'secret')}")
    print(f"ROT13    : {rot13(msg)}")
    print(f"Atbash   : {atbash(msg)}")
