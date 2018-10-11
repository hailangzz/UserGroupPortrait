import pandas as pd
import ServiceInfo
data=pd.read_table(ServiceInfo.data_path, delimiter='|', encoding='utf-8',
                   na_values='null', low_memory=False)
columns=['mobile','added_service']
def get_added_service():
    data_added_service_names=data.added_service.value_counts()
    counts=data_added_service_names.sum()
    result={}
    result['MainClass']={'增值业务名称_MainClass_Equal': {'ClassifyValue': dict(data_added_service_names)}}
    result['MainClassTotal'] = {'增值业务汇总': counts}
    return result
print(get_added_service())