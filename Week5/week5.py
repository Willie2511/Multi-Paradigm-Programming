

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = [address]

    def __repr__(self):
        return f'Person("{self.name}", {self.age})\nADDRESS:{self.address}'

    def addNewAddress(self, newAddress):
        self.address.append(newAddress)

    def getAllAddresses(self):
        return self.address


class Student(Person):
    def __init__(self, name, age, address):
        Person.__init__(self, name, age, address)
        self.college_programme = None

    def __repr__(self):
        string = f'Student({self.name}, {self.age})'
        if(self.college_programme != None):
            string += f'{self.college_programme}'
        return string

    def homeAddress(self):
        return self.address[0]

    def collegeAddress(self):
        if (len(self.address) == 1):
            return self.homeAddress()
        else:
            return self.address[1]


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


class CollegeProgramme:

    def __init__(self, name, level, university, limit=1):
        self.name = name
        self.level = level
        self.university = university
        self.limit = 1
        self.modules = []
        self.students = []

    def addModule(self, new_module):
        self.modules.append(new_module)

    def getAllModules(self):
        return self.modules

    def isModuleOnProgramme(self, module_name):
        for module in self.modules:
            if (module.name == module_name):
                return True
        return False

    def enrollStudent(self, newStudent):
        if(newStudent.age < 18):
            print("Too young to enroll in programme")
        elif (len(self.students) == self.limit):
            print("The programme is full")
        else:
            self.students.append(newStudent)
            newStudent.college_programme = self

    def __repr__(self):
        return f'College Programme: {self.name}, {self.level}, {self.university}'


class CollegeModules:

    def __init__(self, name, level, credits):
        self.name = name
        self.level = level
        self.credits = credits

    def __repr__(self):
        return f'College Module: {self.name}, {self.level}, {self.credits}'


def main():
    # address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
    address2 = Address("99", "Frenchcourt", "Orandale", "Mayo", "H91K7P1")

    # # p1 = Person("John", 36, address1)
    p1 = Student("John", 23, address2)
    p2 = Student("Jacl", 34, address2)
    print(p1)
    # p1.addNewAddress(address1)
    # print(p1.homeAddress())

    masters = CollegeProgramme("Software Engineering", 9, "NUIG")
    module1 = CollegeModules("Python", 8, 5)
    masters.addModule(module1)
    module2 = CollegeModules("Networking", 8, 5)
    masters.addModule(module2)

    print(masters.isModuleOnProgramme("Python"))

    masters.enrollStudent(p1)
    masters.enrollStudent(p2)
    print(p1)


if __name__ == "__main__":
    main()
