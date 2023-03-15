#!/usr/bin/env python3

class Book:
     
    def __init__(self, title = "sample", page_count = 0):
        self.title = title
        self.page_count = page_count

    def get_page(self):
        return self._page_count
    
    def set_page(self,page_count):
        if(type(page_count) == int):
            self._page_count = page_count    
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
                

    page_count = property(get_page, set_page)

sample_book = Book("And Then There Were None")
print(sample_book.title)

