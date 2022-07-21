import  logging
logging.basicConfig(filename="Overriding.log",level=logging.INFO)
class ineuron:

    def no_students(self):
        logging.info("No of students enrolled")

    def student_details(self):
        logging.info("print the profile status of the students")

class hackathon(ineuron):

    def no_students(self):
        logging.info("no of students enrolled in hacathon")

    def winner(self):
        logging.info("print the winner of hackathon")

h = hackathon()

h.no_students()