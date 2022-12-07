class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'Person("{self.name}", {self.age})\nADDRESS:{self.address}'


class Address:

    def __init__(self, house_number, street, town, county, eircode, country="Ireland"):
        self.house_number = house_number
        self.street = street
        self.town = town
        self.county = county
        self.eircode = eircode
        self.country = country

    def __repr__(self):
        string = "\n"
        string += f'{self.house_number} {self.street},\n{self.town}, \n{self.county}, \n{self.eircode}, \n{self.country}'
        return string


def addNewAddress(person, address):
    person.append(address)


def main():
    address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
    p1 = Person("John", 36, address1)
    print(p1)
    address2 = Address("95", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
    addNewAddress(p1, address2, address1)


if __name__ == "__main__":
    main()
