import hashlib
from itertools import permutations

def main():
    
    key_space = ['a','b','c','d','e']

    for key in permutations(key_space):
        print(key)
        md5_obj = hashlib.md5()
        md5_obj.update(''.join(key).encode('utf-8'))
        hashed_key = md5_obj.hexdigest()
        print(hashed_key)
    


if __name__ == "__main__":
    main()
