country_name = input("Enter country name: ")

def my_function(country=None):
    if country is None:
        country = country_name
    print("I am from " + country)

my_function("Sweden")
my_function()
