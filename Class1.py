class Country:
    def __init__(self, name, continent, *args, **kwargs):
        self.name = name
        self.continent = continent
        print("args", args, "kwargs", kwargs)
        super().__init__(*args, **kwargs)

    def subject_of_class(self):

        return (f"{self.name ,self.continent}")

    def presentation(self):
        print(f"{super().presentation()}"
              f"my experience at {self.name} is {self.continent}")


class Brand:
    def __init__(self,brand_name ,business_start_date, *args, **kwargs):
        self.brand_name = brand_name
        self.business_start_date = business_start_date
        print("args", args, "kwargs", kwargs)
        super().__init__(*args, **kwargs)

    def presentation(self):
        print(f"{super().presentation()}"
              f"my experience at {self.brand_name} is {self.business_start_date}")

class Season:
    def __init__(self, season_name, avg_temperature, *args, **kwargs):
        self.season_name = season_name
        self.avg_temperature = avg_temperature
        print("args", args, "kwargs", kwargs)
        super().__init__(*args, **kwargs)

    def presentation(self):
        print(f"{super().presentation()}"
              f"my experience at {self.season_name} is {self.avg_temperature}")


class Product(Country, Brand, Season):
    def __init__(self, name, product_type, price, quantity, *args, **kwargs):
        self.name = name
        self.type = product_type
        self.price = price
        self.quantity = quantity
        print("args", args, "kwargs", kwargs)
        super().__init__(*args, **kwargs)

    def product_price(self, precent):
        self.price = precent
        total_price = self.price - self.price * precent/100
        return total_price


product1 = Product("Geox", "dress", 150000, 1, " Yerevan", "Asia", "Br", "01/12/2017", "Autumn", 25 )

