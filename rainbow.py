import hashlib
from itertools import combinations_with_replacement
import itertools
import argparse
import string

def main(hash_obj, max_length):
    
    key_space = string.ascii_lowercase

    with open('rainbow_table.txt', 'w') as f:
        for key in map(''.join, itertools.product(key_space, repeat=max_length)):
            hash_obj.update(''.join(key).encode('utf-8'))
            hashed_key = hash_obj.hexdigest()
            f.write(key)
            f.write("\t")
            f.write(hashed_key)
            f.write("\n")
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Produce a rainbow table for a specific hash')
    parser.add_argument('--hash', action='store',help='the hash to be tabled')
    parser.add_argument('--passwordmaxlength', type=int, action='store',help='the hash to be tabled')

    hash_type = parser.parse_args().hash
    max_length = parser.parse_args().passwordmaxlength
    
    hash_obj = None

    if hash_type == "md5":
        hash_obj = hashlib.md5()
    elif hash_type == "sha256":
        hash_obj = hashlib.sha256()
    else:
        print("Hash must be specified as either md5 or sha256")
        exit()
    main(hash_obj, max_length)
