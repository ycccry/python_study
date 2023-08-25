import json

from Heima_python.P124_CombinedTrain.data_define import *


class FileReader:
    def read_date(self) -> list:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_date(self) -> list:
        f = open(self.path,"r",encoding="UTF-8")
        data_list = []
        for line in f.readlines():
            line = line.strip()
            data = line.split(",")
            record = Record(data[0],data[1],int(data[2]),data[3])
            data_list.append(record)
        f.close()
        return data_list

class JsonReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_date(self) -> list:
        f = open(self.path,"r",encoding="UTF-8")
        data_list = []
        for line in f.readlines():
            data = json.loads(line)
            record = Record(data["date"],data["order_id"],int(data["money"]),data["province"])
            data_list.append(record)
        f.close()
        return data_list




