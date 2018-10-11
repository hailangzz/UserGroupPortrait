import pandas as pd
import AppInfo
data=pd.read_table(AppInfo.data_path, delimiter='|', encoding='utf-8',
                   na_values='null', low_memory=False)
columns=['mobile','appname','classifyname']
def get_appname():
    data_appname=data.appname.value_counts()
    counts=data_appname.sum()
    result={}
    result['MainClass'] = {'APP名称_MainClass_Equal': {'ClassifyValue': dict(data_appname)}}
    result['MainClassTotal'] = {'APP名称汇总': counts}
    return result
def get_classifyname():
    data_classifyname=data[data.classifyname.notnull()]
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

