takeoff_speed = int(input("enter take off speed: "))
jarak = int(input("enter distance: "))
takeoff_speed = takeoff_speed * (1000 / 3600)

acc = float("{:.2f}".format ((takeoff_speed ** 2) / (2 * jarak)))

waktu = ("{:.2f}".format (takeoff_speed / acc))

print (f"the jets acceleration is {acc} m/s^2 with a time of {waktu} seconds")