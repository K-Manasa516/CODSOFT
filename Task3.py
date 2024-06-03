import random
import string

def generate_secure_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    try:
        pwd_length = int(input("Enter the length of your desired password: "))
        if pwd_length <= 0:
            print("Invalid input. Length must be a positive integer.")
            return
        generated_password = generate_secure_password(pwd_length)
        print("Your generated password is:", generated_password)
    except ValueError:
        print("Invalid input. Length must be a positive integer.")

if __name__ == "__main__":
    main()
