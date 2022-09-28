
class Person:

    def __init__(self, name: str, age: int, size: int, hair_color: str):
      self.name: name
      self.age: age
      self.size: size
      self.hair_color: hair_color

    def Walk(self, distance: int) -> str :
      str(distance)
      return "la distancia a la que esta es " + str(distance)

    def Eat(self,Food:str) -> str:
      return "la comida que le gusta " + Food

    def Speak(self,Language:str) -> str:
        return "su lenguaje es  " + Language


class Student(Person):

  def __init__(self, name: str, age: int, size: int, hair_color: str):
    Person.__init__(self, name, age, size, hair_color)
    print("Creating Student")

  def Study(self):
      print("you are STUDING")



class Teacher(Person):

  def __init__(self, name: str, age: int, size: int, hair_color: str):
    Person.__init__(self, name, age, size, hair_color)
    print("Creating Teacher")

  def Teach(self):
    print("you are TEACHING")


b = Teacher("marcelo", 45, 12, "rojo")
print(b.Walk(4))
print(b.Eat("perro caliente"))
print(b.Speak("español"))
b.Teach()


a = Student("mari", 45, 12, "azul")
print(a.Walk(42))
print(a.Eat("hamburguesa"))
print(a.Speak("catalan"))
a.Study()

