def say_hello():
    return "Hello Visitor"


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_basic_info(self):
        print(
            "Employee named {}, age {}, salary {}".format(
                self.name, self.age, self.salary
            )
        )
