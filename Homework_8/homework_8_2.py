"""
Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country(country_name, capital):
    country_dict = {'name': country_name, 'capital': capital}
    return country_dict


country_name = input("Enter the country's name: ")
capital = input("Enter the capital: ")

country_info = make_country(country_name, capital)
print(country_info)

