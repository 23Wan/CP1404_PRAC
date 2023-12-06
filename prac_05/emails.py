
def giveName(email):
    separateName = email.split("@")
    if "_" in separateName[0]:
        fullName = separateName[0].split("_")
        fullNameJoin = " ".join(fullName)
        returName = fullNameJoin.title()
        return returName
    else:
        returName = separateName[0].title()
        return returName
userData = {}
while True:
    email = input("Email: ")
    if(email == ''):
        break
    nameGuessed = giveName(email)
    print("Is your name", nameGuessed, "? (y/n)", end=" ")
    reCheckName = input()[0]
    if reCheckName == 'y' or reCheckName == 'Y':
        userData[nameGuessed] = email ;
    else:
        nameTyped = input("Name: ")
        if nameTyped in userData:
            print("Name already exists is the database. Re-enter Name: ", end="")
            nameTyped = input()
            userData[nameTyped] = email ;
        else:
            userData[nameTyped] = email ;

print("\n")
for key, value in userData.items():
    print(key, "(", value, ")")