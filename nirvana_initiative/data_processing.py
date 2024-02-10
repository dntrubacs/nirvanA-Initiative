import os
import pandas
import api_networking

class DP:
    """Data Processing"""
    def init(self):
        self.folder
        self.filename
        self.file
        self.data
    
    def start(self, filename, cwd=""):
        self.filename = filename
        # Need to get cwd
        if cwd == "":
            # Directory is empty
            self.folder = os.getcwd()
        else:
            self.folder = cwd
        self.file = self.folder + "/" + self.filename
        self.runner()

    def csv_reader(self):
        self.data = pandas.read_csv(self.file)
        print(self.data)
        return self.data

    def txt_reader(self, file):
        dat = []
        with open(file, 'r') as f:
            while line := f.readline():
                dat.append(line.rstrip())
                #print(line.rstrip(), '/line')
        f.close()
        return dat

    def questions(self):
        data = self.csv_reader()
        # Questions are kept in [2]
        return [data[col].tolist() for col in data.columns][1]
    
    def runner(self):
        #dat = self.questions()
        dat = self.txt_reader("../data/CFR-2023-title14-vol1.txt")
        #print(dat)
        messages = []
        n = 0
        for d in dat:
            if d=="":
                continue
            n += 1
            if n%1000==0:
                print(n)
            #print(d)
            try:
                messages.append(api_networking.llm_qa(llm_server_url='http://localhost:1234/v1',
                              message=d, max_tokens=1))
            except:
                #print("Failed, your mum")
                pass
        
        print(messages)
        

DP = DP()


def csv_reader(file):
    data = pandas.read_csv(file)
    print(data)
    return data
def find():

    Question = ""
    Question = input("Stuff to find: ")

    data = []
    for i in ["../data/CFR-2023-title14-vol1.txt","../data/CFR-2023-title14-vol2.txt","../data/CFR-2023-title14-vol3.txt","../data/CFR-2023-title14-vol4.txt","../data/CFR-2023-title14-vol5.txt"]:
        data.append(csv_reader(i))

    print(data)
#DP.start("Aviation Quiz.csv")
find()
