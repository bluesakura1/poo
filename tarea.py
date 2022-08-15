r = 0
numberprinter =0

class Teacher:
  def __init__(self,id,name):
    self.id = id
    self.name = name
    self.enrolled_course = []


class Student:
  def __init__(self, id, name, cur):
    self.id = id
    self.name = name
    self.enrolled_course = [cur]

    


class Course:
  def __init__(self,id,name,teacher):
    self.id = id
    self.name = name
    self.enrolled_students = []
    self.teacher = teacher
    self.cuestionario = []

  def remove_student(self):
    aux = int(input("""dijite que materia desea cancelar 1 (Matematicas). 3 (derecho). 6 (ingles). 8 (tenis). 
        5 (geometria). 2 (lengua). 7 (contaduria). 4 (natacion)."""))

    if aux == 1:
      curss = c1
    if aux == 2:
      curss = c2
    if aux == 3:
      curss = c3
    if aux == 4:
      curss = c4
    if aux == 5:
      curss = c5
    if aux == 6:
      curss = c6
    if aux == 7:
      curss = c7
    if aux == 8:
      curss = c8

    if E in curss.enrolled_students:
      estud = curss.enrolled_students
      estud = estud.remove(E)
      curso = E.enrolled_course
      curso = curso.remove(curss)
      print("el estudiante a sido removido")
    else:
      print("el estudiante no pertenece al curso")

  def get_studentlist(self):
    aux2 = len(self.enrolled_students)
    tim = 0

    aux = int(input("""dijite que materia desea obtener sus nombres 1 (Matematicas). 3 (derecho). 6 (ingles). 8 (tenis). 
            5 (geometria). 2 (lengua). 7 (contaduria). 4 (natacion)."""))

    if aux == 1:
      curss = c1
    if aux == 2:
      curss = c2
    if aux == 3:
      curss = c3
    if aux == 4:
      curss = c4
    if aux == 5:
      curss = c5
    if aux == 6:
      curss = c6
    if aux == 7:
      curss = c7
    if aux == 8:
      curss = c8

    while tim <= aux2-1:
      getn = curss.enrolled_students[tim]
      print(getn.name)
      tim =tim+1
    if curss.enrolled_students ==[]:
      print("no hay estudiantes")



class parcial:

  def __init__(self,nombre,porciento):
    self.nombre = nombre
    self.porcentaje = porciento
    self.cuestionario = []

  def preguntas(self):
    tp =1
    aux = int(input("""dijite que materia desea crear un parcial 1 (Matematicas). 3 (derecho). 6 (ingles). 8 (tenis). 
            5 (geometria). 2 (lengua). 7 (contaduria). 4 (natacion)."""))

    if aux == 1:
      curss = c1
    if aux == 2:
      curss = c2
    if aux == 3:
      curss = c3
    if aux == 4:
      curss = c4
    if aux == 5:
      curss = c5
    if aux == 6:
      curss = c6
    if aux == 7:
      curss = c7
    if aux == 8:
      curss = c8

    while tp == 1:
      pr=input("ingrese su pregunta de parcial")
      aux3 = pa1.cuestionario
      aux3 =aux3.append(pr)
      aux4=curss.cuestionario
      aux4=aux4.append(pr)

      tp=int(input("desea añadir mas preguntas escriba 1 si no quiere añadir mas 0"))
      if tp != 1:
        print(pa1.cuestionario)
        print(curss.cuestionario, curss.name)






#----------------- Instanciacion -----------------

p1 = Teacher(1,"carlos")
p2 = Teacher(2,"juan")
p3 = Teacher(3,"camila")
p4 = Teacher(4,"alex")
c1 = Course(1,"matematicas",p1)
c2 = Course(2,"lengua",p2)
c3 = Course(3,"derecho",p3)
c4 = Course(4,"natacion",p4)
c5 = Course(1,"geometria",p1)
c6 = Course(2,"ingles",p2)
c7 = Course(3,"contaduria",p3)
c8 = Course(4,"tenis",p4)
E = Student(1, "saony",c1)
E = Student(4, "alex",c5)
E = Student(2, "clara",c4)
E = Student(3, "mateo",c3)
pa1 = parcial("calculo", 32)

#----------------- Instanciacion -----------------
def enroll_course(r):
  while r == 0:
    print("Buenos dias por favor precione el numero corerespondiente para la materia a matricular una a la vez")
    aux = int(input(""" 1 (Matematicas). 3 (derecho). 6 (ingles). 8 (tenis). 
    5 (geometria). 2 (lengua). 7 (contaduria). 4 (natacion). """))

    curso = E.enrolled_course



    if aux == 1:
      if c1 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c1.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c1)
        print("Matriculaccion exitosa")

    if aux == 2:
      if c2 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c2.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c2)
        print("Matriculaccion exitosa")

    if aux == 3:
      if c3 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c3.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c3)
        print("Matriculaccion exitosa")

    if aux == 4:
      if c4 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c4.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c4)
        print("Matriculaccion exitosa")

    if aux == 5:
      if c5 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c5.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c5)
        print("Matriculaccion exitosa")

    if aux == 6:
      if c6 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c6.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c6)
        print("Matriculaccion exitosa")

    if aux == 7:
      if c7 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c7.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c7)
        print("Matriculaccion exitosa")

    if aux == 8:
      if c8 in curso:
        print("ya matriculaste esta materia")
      else:
        estud = c8.enrolled_students
        estud = estud.append(E)
        curso = curso.append(c8)
        print("Matriculaccion exitosa")

    r = int(input("quieres matricular mas materias escribe 0 para si o 1 para no?"))
def cancel_course(r):
  while r == 0:
    print("Buenos dias por favor precione el numero corerespondiente para la materia a matricular una a la vez")
    aux = int(input("""dijite que materia desea cancelar 1 (Matematicas). 3 (derecho). 6 (ingles). 8 (tenis). 
    5 (geometria). 2 (lengua). 7 (contaduria). 4 (natacion)."""))

    curso = E.enrolled_course

    if aux == 1:
      if not (c1 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c1.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c1)
        print("cancelacion exitosa")

    if aux == 2:
      if not (c2 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c2.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c2)
        print("cancelacion exitosa")

    if aux == 3:
      if not (c3 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c3.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c3)
        print("cancelacion exitosa")

    if aux == 4:
      if not (c4 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c4.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c4)
        print("cancelacion exitosa")

    if aux == 5:
      if not (c5 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c5.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c5)
        print("cancelacion exitosa")

    if aux == 6:
      if not (c6 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c6.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c6)
        print("cancelacion exitosa")

    if aux == 7:
      if not (c7 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c7.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c7)
        print("cancelacion exitosa")

    if aux == 8:
      if not (c8 in E.enrolled_course):
        print("no estas matriculado en esta materia")
      else:
        estud = c8.enrolled_students
        estud = estud.remove(E)
        curso = curso.remove(c8)
        print("cancelacion exitosa")

    r = int(input("quieres cancelar mas materias escribe 0 para si o 1 para no?"))


enroll_course(0)
print(E.enrolled_course)
cancel_course(0)
print(E.enrolled_course)
c2.get_studentlist()
print(E.enrolled_course)
c2.remove_student()
print(parcial.preguntas(0))
