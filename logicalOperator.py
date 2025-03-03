f_name = input("Enter First Name: ")
l_name = input("Enter Last  Name: ")
age = int(input("Enter Age: "))

if age <= 17:
    print(f"Welcome {f_name} {l_name}, Hello young star")
    
elif age >=100:
    print(f"Hello {f_name} {l_name},too old")
    
else:
      print(f"Hello {f_name} {l_name},You Are welcome")