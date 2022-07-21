import  logging
logging.basicConfig(filename="Polymorphism.log",level=logging.INFO)
class ineuron_students:

    def students(self):
        logging.info("total no of students")

class hackathon_students:

    def students(self):
        logging.info("no of students present in hackathon")

def ineuron_students_desc(a):
    a.students()

i = ineuron_students()
j = hackathon_students()

ineuron_students_desc(i)
ineuron_students_desc(j)

#logging.shutdown()