class India():

    def capital(self):
        print("Delhi is capital of India")

    def language(self):
        print("Hindi")

    def type(self):
        print("Developing")

class USA():

    def capital(self):
        print("Washinngton is capital of USA")

    def language(self):
        print("English")

    def type(self):
        print("Developed")

IND = India()
USA = USA()
for country in (IND,USA):
    country.capital()
    country.language()
    country.type()