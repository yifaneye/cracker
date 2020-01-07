import hashlib

DICTIONARY = "dictionary.txt"


def crack(hash_input):
    file = open(DICTIONARY, "r")
    for word in file:
        hash_computed = hashlib.md5(word[:-1].encode('utf-8')).hexdigest()
        if hash_computed == hash_input:
            return word
    file.close()
    return None
