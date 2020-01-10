from dictionary_attack import crack

import hashlib


def get_md5_hash(plaintext):
    return (hashlib.md5(plaintext.encode())).hexdigest()


def check_crack(hash_input, expectedRetVal):
    assert (crack(hash_input)).rstrip() == expectedRetVal


def test_crack_plaintext_of_123456():
    plaintext = "123456"
    hash_input = get_md5_hash(plaintext)
    check_crack(hash_input, plaintext)


def test_crack_plaintext_of_incorrect():
    plaintext = "incorrect"
    hash_input = get_md5_hash(plaintext)
    check_crack(hash_input, plaintext)


def test_crack_plaintext_of_password1():
    plaintext = "Password1"
    hash_input = get_md5_hash(plaintext)
    check_crack(hash_input, plaintext)


def test_crack_plaintext_of_pa55w0rd():
    plaintext = "pa55w0rd"
    hash_input = get_md5_hash(plaintext)
    check_crack(hash_input, plaintext)
