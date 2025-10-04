import sys
from robust_division_calculator import safe_divide


def main():
    # Check if exactly 2 arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function
    result = safe_divide(numerator, denominator)
    print(result)


if __name__ == "__main__":
    main()
