class Hotel:
    def __init__(self, name, place, room_lux, room_lux_price, room_mid, room_mid_price):
        self.name = name
        self.place = place
        self.room_lux = room_lux
        self.room_lux_price = room_lux_price
        self.room_mid = room_mid
        self.room_mid_price = room_mid_price

    def booking(self):
        y= {}

        for key,value in self.room_mid:
            if value != "bussy":
                value = "bussy"
                return value
        print(self.room_mid)


ho1 = Hotel("Jake", "Marriot", {"Lux" : "fre"}, 100000 , {"mid" : "fre"},2000 )
print (ho1.booking())


