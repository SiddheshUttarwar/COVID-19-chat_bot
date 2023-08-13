# reading state wise vaccination centers data
import json
from pprint import pprint
import sys
from os import path


def  Read_data():
        bundle_dir =getattr(sys,"_MEIPASS",path.abspath(path.dirname(__file__)))
        path_to_stateswise_vaccines =path.join(bundle_dir,"data","Statewise_vaccines.txt")
        m =open(path_to_stateswise_vaccines,"r")
        k =m.read()
        m.close()
        return json.loads(k)

