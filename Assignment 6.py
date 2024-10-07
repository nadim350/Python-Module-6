import math


def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2) / 10000  # Convert area to square meters
    return price / area


def main():
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))
    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    price_per_sq_m1 = unit_price(diameter1, price1)
    price_per_sq_m2 = unit_price(diameter2, price2)

    print(f"First pizza's unit price: {price_per_sq_m1:.2f} €/m²")
    print(f"Second pizza's unit price: {price_per_sq_m2:.2f} €/m²")

    if price_per_sq_m1 < price_per_sq_m2:
        print("The first pizza offers better value for money.")
    else:
        print("The second pizza offers better value for money.")


main()
