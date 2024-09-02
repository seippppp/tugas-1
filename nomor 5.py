volume = int(input("volume to be infused (ml): "))
minutes = int(input("minutes over which to infuse: "))

time_hours = minutes / 60

infusion_rate = volume / time_hours

print (f"VTBI: ,{volume}")
print(f"rate, {infusion_rate}")