class Shoe:
    pass
    def _init_(self, brand, size: int):
        self.brand = brand
        assert isinstance(size, int), "Size must be an integer"
        self.size = size
        self.condition = 'New'  

    def repair(self):
        self.condition = 'Repaired'
        self.cobble = True


try:
    my_shoe = Shoe('adidas', '20') 
except AssertionError as e:
    print(e)

my_shoe = Shoe('nike', 10)
print(my_shoe.condition)  

my_shoe.repair()
print(my_shoe.condition)  
print(my_shoe.cobble)  