import random # Adjust characters in random sequence .
import string # uses Alphabets, numbers and special characters.

def password_generator(length: int = 10): # Define the legnth: int= "".
    alphabet = string.ascii_letters + string.digits + string.punctuation # Defines all things used from the string module. 
    password = "".join(random.choice(alphabet) for i in range(length) ) # Use random.choice(alphabet) to create a random sequnce. 
    return password

password = password_generator() # call the fucntion  
print(f"generated password: {password}") # this will give your password, for example: PIZlT?Tr][
