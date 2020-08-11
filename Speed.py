Driving_speed = int(input("What was your driving speed?\n"))
Allowed_speed = int(input("What is the allowed speed on the road?\n"))


def roundThis():
    return 5 * round((Driving_speed / 5))


Driving_speed = roundThis()

if Driving_speed < Allowed_speed:
    print("OK")
else:
    demerits = ((Driving_speed - Allowed_speed) // 5)
    print("Your demerits are", demerits)
if demerits >= 12:
    print("Time to go to jail!")

input("Press any key to exit...")
