import os
import pandas


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

    def csv_reader(self):
        self.data = pandas.read_csv(self.file)
        print(self.data)
        return self.data

    def questions(self):
        data = self.csv_reader()
        # Questions are kept in [2]
        return data[2]


DP = DP()

DP.start("Aviation Quiz.csv")

DP.csv_reader()