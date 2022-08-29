name = input("Enter Name : ").strip().title()

print(f"Name :{name}")

# only first last name alllowed. no middle name
first, last = name.split(" ")

print(f"First name: {first}\nLast name: {last}")
