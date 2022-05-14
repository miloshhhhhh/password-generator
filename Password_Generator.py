# Master Strongbox & Password Generator 
import time
import random
import string
import sys
# import hashlib


def password_generator(length):

    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


# try to open file if exists and find match if exist skip password generation
def read_from_file(for_what):
    
    try:
        with open('password.txt', 'r') as f:
            for i in f:
                i = i.split(':')
                if i[0] == for_what:
                    print('Password already exists')
                    sys.exit()
    except FileNotFoundError:
        print('File not found but we will create one')


def save_to_file(password,pass_for):
    
    with open('password.txt', 'a') as f:
        f.write(pass_for+':'+password+'\n')
        print('Password saved to file')


def main():

    if len(sys.argv) == 2:
        for_what = str(input('For what do you want your password to be? ')).lower()
        length = int(sys.argv[1])
        print(length)
        password = password_generator(length)
        read_from_file(for_what) # break if it already exists
        save_to_file(password,for_what)
    
    else:
        print('Usage: python3 Password_Generator.py <length>')
        sys.exit()

if __name__ == '__main__':


    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
