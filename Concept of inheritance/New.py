class India():

    def capital(self):
        print("New delhi is the capital of India")

    def language(self):
        print("Hindi the primary language of India")

    def type(self):
        print("India is a developing country")

class USA():

    def capital(self):
        print("Washington D.C. is the capital of USA")

    def language(self):
        print("English the primary language of USA")

    def type(self):
        print("USA is a developed country")

IND = India()
USA = USA()

for country in (IND,USA):
    country.capital()
    country.language()
    country.type()
