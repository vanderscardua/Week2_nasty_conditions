place = input ("where should i look?")

if place == "in the bedroom":
        print("Where in the bedroom should i look?")
        specificlocation=input ()

        if specificlocation == "under the bed":
             print("found some shoes but no phone")

        else:
             print("Found some mess but no phone")

elif place == "in the bathroom":
    print("Where in the bathroom should i look?")
    specificlocation = input()
    if specificlocation == "in the bathtub":
        print("found a rubber duck but no phone")

    else:
        print("Found bathroom stuff but no phone")

elif place == "in the living room":
    print("Where in the living room should i look?")
    specificlocation = input()

    if specificlocation == "on the table":
        print("Yes! I found my phone.")

    else:
        print("Found some stuff but no phone")

else:
    print("i dont know where it is but i will keep looking. ")



