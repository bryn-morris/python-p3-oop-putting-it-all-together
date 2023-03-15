#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand="sample", color = "blank", size = 0):
        self.brand = brand
        self.color = color
        self.size = size

    def size_getter(self):
        return self._size

    def size_setter(self,size):
        print(size)
        if(type(size) != int):
            print("size must be an integer")
        else:
            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(size_getter,size_setter)

stan_smith = Shoe("Adidas")
stan_smith.size = "not an integer"

