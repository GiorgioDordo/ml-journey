class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"Car Information:") # la f serve per formattare la stringa. f = formatted string literal
    print(f"Brand: {self.brand}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")


Car1 = Car("Toyota", "Camry", 2020) 
Car2 = Car("Honda", "Civic", 2019)
Car1.display_info()