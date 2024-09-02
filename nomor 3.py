hours = int(input("enter hours since the freezer failure: "))
minutes = int(input("enter minutes since the freezer failure: "))

t = hours * 60 + minutes
t = t /60

T = (4 * t ** 2 / t - 2) - 20
print(f"estimated freezer temperature is {T} celcius")