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
        #self.runner()

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
DP.start("Aviation Quiz.csv")

def txt_reader(file):
    dat = ""
    with open(file, 'r') as f:
        dat = f.read()
    f.close()
    return dat
def find(word, amount):

    data = ""
    for num, i in enumerate(["data/CFR-2023-title14-vol1.txt","data/CFR-2023-title14-vol2.txt","data/CFR-2023-title14-vol3.txt","data/CFR-2023-title14-vol4.txt","data/CFR-2023-title14-vol5.txt"]):
        info = txt_reader(i)
        x = 0
        s = 0
        while x != -1:
            x = info.find(word,s)
            #print("Paper "+str(num)+":"+ str(info[x:x+amount]))
            data = data + str(info[x:x+amount])
            s = x+amount+1
            if len(data) > 4000:
                break

    data = data[0:100]

    return data

def q_interpreter(q):
    ignoreList = ["for",
                  "and",
                  "what",
                  "a",
                  "but",
                  "in",
                  "such",
                  "by",
                  "the",
                  "that",
                  "there",
                  "at",
                  "their",
                  "of",
                  "within",
                  "an",
                  "be",
                  "to",
                  "is",
                  "a.",
                  "b.",
                  "c."]
    askList = []
    #for q in questions:
    words = q.split(" ")
    for w in words:
        if w.lower() in ignoreList:
            pass
        else:
            askList.append(w)

    return askList

def runner(question: str, llm_server_url: str = 'http://localhost:1234/v1', max_tokens: int = -1,
           temperature:float = 0.0)-> str:
    # interpet the question
    interpreted_q = q_interpreter(q=question)

    # figo through each word in interpreted_q
    n = 0
    for word in interpreted_q[0:1]:
        n += 1
        # find similar statements
        similar_statements = find(word=word, amount=100)

        # tell chatbot to rember the cfr code
        llm_qa(llm_server_url=llm_server_url, message='Remember this: '+similar_statements,
               max_tokens = 1, temperature = 0)

    # ask the question
    answer = llm_isolate_answer(llm_server_url='http://localhost:1234/v1', aviation_question=question,
                                max_tokens=-1, temperature=temperature)
    return answer



if __name__ == '__main__':
    import json
    import os
    from data_cleaning import return_question
    from api_networking import llm_isolate_answer, llm_qa
    os.chdir('/home/jordan/github/nirvanA-Initiative')
    all_answers = []

    # go through each question
    n_none = 0
    n_errors = 0
    for i in range(100):
        try:
            # get the question
            question = return_question(data_path='Aviation Quiz.csv', index=i)

            test_answer = runner(question=question)
            if test_answer is not None:
                pass
            else:
                test_answer = 'C'
                n_none += 1
        except:
            test_answer = 'A'
            n_errors += 1
        all_answers.append(test_answer)
        print(i,'/',99, test_answer, 'errors: ', n_errors, 'D answers: ', n_none)

    with open("Answers.csv","w") as f:
        index = 0
        for j in all_answers:
            f.write(str(index)+ ", "+ j+ "\n")
            index+=1

    f.close()

