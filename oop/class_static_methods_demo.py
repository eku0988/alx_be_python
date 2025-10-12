class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that prints the class attribute 'calculation_type'
        and returns the product of two numbers.
        Uses 'cls' to access class-level data.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
