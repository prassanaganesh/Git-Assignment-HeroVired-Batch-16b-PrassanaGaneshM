import math
class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    def calculate_rectangle_area(self, length, width):
        return length * width
    
    def calculate_area(length, width):
    """Calculate and return the area of a rectangle."""
    return length * width

def main():
    try:
        # Take user input
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        # Validate inputs
        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
            return

        # Calculate area
        area = calculate_area(length, width)

        # Display result
        print(f"The area of the rectangle is: {area:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
