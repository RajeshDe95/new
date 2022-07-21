
import  logging
logging.basicConfig(filename="Encapsulation.log",level=logging.INFO)
class ineuron:
    def __init__(self):
        self.participant = "no of people participated"

    def hackathon(self):
        logging.info(self.participant)

i = ineuron()

i.hackathon()
i.participant="no of people participated in hackathon"
i.hackathon()



class ineuron1:
    def __init__(self):
        self.__participant = "no of people participated"

    def hackathon(self):
        logging.info(self.__participant)

    def hackathon_details_updated(self,new_value):
        self.__participant=new_value

i1 = ineuron1()

i1.hackathon_details_updated("no of people participated in hackathon")
#i1.__participant("no of people participated in hackathon")
i1.hackathon()



