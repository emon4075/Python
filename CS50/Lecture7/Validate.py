# Checking Email Validity

Email = input("Enter Your Email Address: ")

if "@" in Email:
    user_name, domain_name = Email.split("@")
    if user_name and domain_name.endswith(".com"):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
