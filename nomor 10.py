x1 = float(input("enter x1: "))
y1 = float(input("enter y1: "))
x2 = float(input("enter x2: "))
y2 = float(input("enter y2: "))

m = (y2 - y1) / (x2 - x1)

x_mid = (x1 + x2) / 2
y_mid = (y1 + y2) / 2

m_perp = -1 / m

b = y_mid - m_perp * x_mid

print(f"Persamaan bisektor tegak lurus adalah: y = {m_perp}x + {b}")