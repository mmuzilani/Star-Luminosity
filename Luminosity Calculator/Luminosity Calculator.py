# Star Luminosity Calculator
# Author: Md. Mahiuddin Zilani
# Description: Calculate luminosity of a star based on its mass

def calculate_luminosity(mass):
    """
    Calculate the luminosity of a star based on its mass.
    L/Lsun = (M/Msun)^3.5  for main-sequence stars
    """
    luminosity = mass ** 3.5
    return luminosity

def main():
    print("=== Star Luminosity Calculator ===")
    
    # Input: Mass of the star in solar masses
    mass = float(input("Enter the mass of the star (in solar masses): "))
    
    # Calculate luminosity
    luminosity = calculate_luminosity(mass)
    
    # Output: Luminosity in terms of Sun's luminosity
    print(f"The luminosity of the star is approximately {luminosity:.2f} times the Sun's luminosity.")

if __name__ == "__main__":
    main()
