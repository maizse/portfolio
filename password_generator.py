import random
import string 
def password_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(chars) for x in range(0, size))

print("length of password: ")
size = int(input())

print(password_generator(size))
print(len(password_generator(size)))
