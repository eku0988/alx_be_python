class Book:
    def __init__(self, title, author, year):
        """
        Constructor that initializes the book attributes.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official representation of the Book object
        that can be used to recreate the instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
