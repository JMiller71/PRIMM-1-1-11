"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
  # prompts two inputs from user and adds them together to get the total 
    num1: int = input("Enter a number: ")
    num1 = float(num1) # changes string to an integer
    num2: int = input("Enter another number: ")
    num2 = float(num2) # changes string to an integer
    total: int = num1+num2
#prints string saying num1 + num2 = total
    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
