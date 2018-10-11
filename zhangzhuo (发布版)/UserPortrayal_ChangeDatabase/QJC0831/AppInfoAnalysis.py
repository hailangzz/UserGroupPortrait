import pandas as pd
class AppAnalysis():
    def __init__(self,datapath):
        self.datapath=datapath
        self.data=pd.read_table(self.datapath, delimiter='|', encoding='utf-8',
                           na_values='null', low_memory=False)
        self.data.columns=['mobile','appname','classifyname']

    def get_appname(self):
        data_appname = self.data.appname.value_counts()
        counts = self.data['mobile'].drop_duplicates().count()
        result = {}
        result['MainClass'] = {'APP名称_MainClass_Equal': {'ClassifyValue': dict(data_appname)}}
        result['MainClassTotal'] = {'APP名称汇总': counts}
        return result

    def get_classifyname(self):
        data_classifyname=self.data[self.data.classifyname.notnull()]
        classifyname=list(set(list(data_classifyname.classifyname.values)))
        result={}
        dicts={}
        for names in  classifyname:
            data_classifyname_name=data_classifyname[['mobile','appname']][data_classifyname.classifyname==names]
            data_classifyname_name_counts=data_classifyname_name.appname.value_counts()
            dicts[names]={'ClassifyValue':dict(data_classifyname_name_counts),'ChildClassTotal':data_classifyname_name_counts.sum()}
        result['MainClass']={'APP所属分类_MainClass_Equal': {'ChildClass':dicts}}
        result['MainClassTotal']={'APP所属分类汇总': len(data_classifyname)}
        return result

