import string,random

n = int(input("How much passwords do you need ? "))
passwords_list = []

for _ in range(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(chars, 8))
    passwords_list.append(password)

print("Generated password:\n"+"\n".join(passwords_list))