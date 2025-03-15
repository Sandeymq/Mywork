#class Cow:
    #def __init__(self, name = None, age = 15):
        #self.name = name
        #self.age = age
    #def GetInfo(self):
        #print(f"Name is {self.name}. Age is {self.age}.")
    #def Talk(self):
        #print("Moo moo!")

#obj = Cow("Cow", 15)
#obj.Talk()
#obj.GetInfo()
#objg = Cow()
#objg.GetInfo()

#class Triangle:
    #def __init__(self, width = 11, height = 10, dovzuna = 7):
        #self.width = width
        #self.height = height
        #self.dovzuna = dovzuna
    #def GetInfo(self):
        #print(f"width {self.width}. height {self.height}. dovzuna {self.dovzuna}")
    #def ploshca(self):
        #print(self.width*self.height *0.5)
    #def perimeter(self):
        #print("24cm")

#info = Triangle(11, 10, 7)
#info1 = Triangle(115, 10, 7)
#info.GetInfo()
#info.ploshca()
#infofo1.ploshca()
#print("test commit")

class Student():
    def __init__(self, name, age, grades = []):
        self.name = name
        self.age = age
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def get_avg(self):
        for i in self.grades:
            sum += self.grades[i]


student = Student("Олександр", 14)
student.add_grade(90)
student.add_grade(50)
student.add_grade(20)

