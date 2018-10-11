import pandas as pd
class ServiceAnalysis():
    def __init__(self,datapath):
        self.datapath=datapath
        self.data=pd.read_table(self.datapath, delimiter='|', encoding='utf-8',
                           na_values='null', low_memory=False)
        self.data.columns=['mobile','service']
    def get_service(self):
        data_service_names=self.data.service.value_counts()
        counts=data_service_names.sum()
        result={}
        result['MainClass']={'增值业务_MainClass_Equal': {'ClassifyValue': dict(data_service_names)}}
        result['MainClassTotal'] = {'增值业务汇总': counts}
        return result

