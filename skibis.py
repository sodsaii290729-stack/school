# ==========================================
# Utmaning 1 – Bok i ett bibliotek
# ==========================================

# A class is a blueprint (template) for creating objects.
class Book:

    # __init__ runs automatically when you create a new book.
    # It receives the three values: title, author and pages.
    def __init__(self, title, author, pages):
        # self means "this specific book".
        # We save each value inside the object so we can use it later.
        self.title = title
        self.author = author
        self.pages = pages

    # A method is a function that belongs to the class.
    # show_info() prints the information about the book.
    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)
        print()  # Empty line between books


# Create two different book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)

# Call the method to print the information for each book
book1.show_info()
book2.show_info()


# ==========================================
# Utmaning 2 – Temperaturmätare
# ==========================================

# A blueprint for a temperature sensor
class TemperatureSensor:

    # Runs when a new sensor is created.
    # location = where the sensor is (for example Kitchen)
    # temperature = the starting temperature
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    # Increases the temperature by 1 degree each time it is called
    def increase_temperature(self):
        self.temperature = self.temperature + 1

    # Decreases the temperature by 1 degree each time it is called
    def decrease_temperature(self):
        self.temperature = self.temperature - 1

    # Prints the location and the current temperature
    # Example: Kitchen: 22 degrees
    def show_temperature(self):
        print(self.location + ":", self.temperature, "degrees")


# Create two different sensors with their own starting temperatures
sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Outside", 5)

# Show the starting temperatures
print("Start temperatures:")
sensor1.show_temperature()
sensor2.show_temperature()

# Increase the kitchen temperature twice (20 -> 22)
sensor1.increase_temperature()
sensor1.increase_temperature()

# Decrease the outside temperature once (5 -> 4)
sensor2.decrease_temperature()

# Show the new temperatures
print()
print("After changes:")
sensor1.show_temperature()
sensor2.show_temperature()


# ==========================================
# Utmaning 3 – Produktlager
# ==========================================

# A blueprint for a product in a simple stock system
class Product:

    # Runs when a new product is created.
    # name = the product's name
    # price = the price in kr
    # stock = how many are in stock
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Sells one product.
    # The if-statement checks that there is something left to sell.
    def sell(self):
        if self.stock > 0:
            self.stock = self.stock - 1
            print("Sold one", self.name)
        else:
            print("Product is out of stock!")

    # Adds more products to the stock.
    # amount = how many new products arrive
    def restock(self, amount):
        self.stock = self.stock + amount
        print("Restocked", amount, self.name)

    # Prints the product information
    def show_info(self):
        print("Product:", self.name)
        print("Price:", self.price, "kr")
        print("Stock:", self.stock)
        print()  # Empty line


# Create two products
product1 = Product("Keyboard", 399, 10)
product2 = Product("Mouse", 199, 1)

# Show the starting information
product1.show_info()
product2.show_info()

# Sell one keyboard (10 -> 9)
product1.sell()
product1.show_info()

# Restock 5 keyboards (9 -> 14)
product1.restock(5)
product1.show_info()

# Sell the mouse twice.
# The first time works (1 -> 0), the second time it is out of stock.
product2.sell()
product2.sell()
product2.show_info()