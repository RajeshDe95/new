import  logging
logging.basicConfig(filename="Multilevel_inheritence.log",level=logging.INFO)
class ineuron:

    def no_students(self):
        logging.info("No of students enrolled")

    def student_details(self):
        logging.info("print the profile status of the students")

class hackathon(ineuron):

    def participated(self):
        logging.info("no of students participated in hacathon")

    def winner(self):
        logging.info("print the winner of hackathon")

class prize(hackathon):

    def prize(self):
        logging.info("print the prize money of hackathon")

p = prize()

p.no_students()
p.participated()
p.prize()


