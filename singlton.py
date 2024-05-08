class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, data):
        self.data = data

if __name__ == "__main__":
    # Creating instances of Singleton
    s1 = Singleton("Data for Singleton 1")
    s2 = Singleton("Data for Singleton 2")

    # Printing the data attribute of both instances
    print("Data for Singleton 1:", s1.data)
    print("Data for Singleton 2:", s2.data)

    # Modifying the data attribute of s1
    s1.data = "Modified data for Singleton 1"

    # Checking if the data attribute of s2 is also modified
    print("Data for Singleton 2 after modification:", s2.data)
