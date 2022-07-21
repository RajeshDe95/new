import  logging
logging.basicConfig(filename="Multiple_Inheritence.log",level=logging.INFO)
class ineuron:

    def no_students(self):
        logging.info("No of students enrolled")

    def student_details(self):
        logging.info("print the profile status of the students")

class hackathon:

    def participated(self):
        logging.info("no of students participated in hacathon")

    def winner(self):
        logging.info("print the winner of hackathon")

class prize(ineuron,hackathon):

    def prize(self):
        logging.info("print the prize money of hackathon")



p = prize()
p.student_details()
p.winner()
p.prize()