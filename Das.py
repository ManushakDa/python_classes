class Human:
    def __init__(self, name, surname, age, height, weight, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def person_will_be_100_years_old(self):

        if self.age < 100:
            years_100 = 100 - self.age
            print("Human will be 100 years old after", years_100)
        elif self.age > 100:
            print("Human age is greater than 100")
        elif self.age == 100:
            print("Human is 100 years old")

    def human_optimal_weight(self):
        optimal_weight = 50 + 0.75 * (self.height - 150) + (self.weight - 20) / 4
        print("Your optimal weight will be", optimal_weight)

    def present(name, surname, age, height, weight, gender):
        return "sad"


class Student(Human):
    def __init__(self, marks,name, surname,age, height, weight, gender):

        super().__init__(name, surname,age, height, weight, gender)
        self.marks = marks




    def add_marks(self, new_mark):
        self.new_mark = new_mark
        self.marks = []
        a = self.marks.append(new_mark)
        print(a)

    def avg(self):
        print(sum(self.marks) / len(self.marks))

    def present(self):
        print()


# human1 = Human("man", "Xalatyan", 100, 155, 159, "mail")
# human1.person_will_be_100_years_old()
# human1.human_optimal_weight()
st1 = Student([15, 15, 25, 36, 96],"man", "Xalatyan", 100, 155, 159, "mail",)
st1.avg()
st1.present()

