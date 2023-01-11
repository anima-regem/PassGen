import random
import string

while True: 
 length = int(input('Enter Password Length : '))

 lower = string.ascii_lowercase
 upper = string.ascii_uppercase
 number = string.digits
 symbols = string.punctuation

 char = lower + upper + number + symbols

 t = random.sample(char,length)
 password ="".join(t)
 print(password)
