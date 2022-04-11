#require Libraries
import random
import string

# Get Length
print('Please Input Your Password Length : ')
length = int(input())

#Set Parts of a Hard Password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lowercase + uppercase + digits + symbols

#Generate Password
temp = random.sample(all,length)

password = ''.join(temp)
#Show Password
print(password)

#---------------------------------- Coded By Benyamin vala -------------------------------------#