import  logging
logging.basicConfig(filename="Inheritence.log",level=logging.INFO)

class hall_of_fame:

    def __init__(self,name,emailid,domain):
        self.name=name
        self.emailid=emailid
        self.domain=domain

class ineuron(hall_of_fame):
    pass


i = ineuron("abhi","abhi@gmail.com","data science")
j = ineuron("raj","raj@gmail.com","data analyst")

logging.info(i.name)
logging.info(i.emailid)
logging.info(i.domain)
logging.info(j.name)
logging.info(j.emailid)
logging.info(j.domain)






