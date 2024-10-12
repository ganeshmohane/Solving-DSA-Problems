# Reduce the fraction to its lowest form - Zeus Learning (20 Sep 2024 APT test)

def reduce_fraction():
    numerator = int(input("Enter the numerator:\n"))
    denominator = int(input("Enter the denominator: \n"))

    # Find the greatest common divisor (GCD) of numerator and denominator
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    hcf = gcd(numerator, denominator)

    # Reduce the fraction by dividing both numerator and denominator by GCD
    reduced_numerator = numerator // hcf
    reduced_denominator = denominator // hcf

    print(f"Reduced fraction is {reduced_numerator}/{reduced_denominator}")

reduce_fraction()