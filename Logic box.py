print("="*50)
print("Welcome to the Number Analyzer!")
print("="*50)

print("Select an option")
print("1. Analyze a Range of Numbers")
print("2. Exit")

choice = int(input("Enter your choice: "))

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total = 0

for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total += num

print()
print(f"""sum of all numbers from
      {start} to {end} is: {total}""")

print("="*50)
print("Exiting the program. good bye!")    
print("="*50)    

    




        


