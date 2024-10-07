def gallons_to_liters(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter quantity of gasoline in gallons (negative to quit): "))
        if gallons < 0:
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")

main()
