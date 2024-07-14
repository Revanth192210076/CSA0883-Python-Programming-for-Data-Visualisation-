age = int(input("Enter Age : "))

age1=18-age;



if age >= 18:
    status = "Eligible"
else:
    status = "Not Eligible, You are eligible after ",age1,"Years"

print("You are ", status, " for Vote.")
