import hashlib
from itertools import combinations_with_replacement
import itertools

def main():
    
    key_space = ['a','i','l','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','H','A']

    for key in map(''.join, itertools.product('AHialn ', repeat=7)):
        md5_obj = hashlib.md5()
        md5_obj.update(''.join(key).encode('utf-8'))
        hashed_key = md5_obj.hexdigest()
        if key == "Hi Alan":
            print(hashed_key)

        if hashed_key == "4471c23e354c63c4d0dc3d69c1162317":
            print(key)



if __name__ == "__main__":
    main()
