import string
import random

def generate_password(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for i in range(length))


if __name__ =="__main__":
    print(generate_password(15))