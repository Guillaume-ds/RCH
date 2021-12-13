import csv
import pandas as pd

def get_info_direct():
    infos_direct =pd.read_csv('Static/infos_directs.csv')  
    return infos_direct
    
infos_directs=get_info_direct()

hr = "<hr style=' text-align : center; border-color : grey; margin-top: 0px; margin-bottom: 0px;'>"