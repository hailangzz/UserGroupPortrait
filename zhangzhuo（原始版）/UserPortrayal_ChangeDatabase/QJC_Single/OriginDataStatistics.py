import numpy as np
import pandas as pd
import operator
import copy

def get_sex(data):
    data_sex=data.sex.value_counts()
    result={}
    dict={}
    dict['男']=data_sex[1]
    dict['女'] = data_sex[0]
    result['MainClass'] ={'性别_MainClass_Equal': {'ClassifyValue':dict}}
    result['MainClassTotal']={'性别汇总': data.sex.count()}
    return result
def get_age(data):
    data_age=data.age.value_counts()
    result={}
    dict={}
    dict['0-15']=data_age[(data_age.index>=0)&(data_age.index<15)].sum()
    dict['15-20'] = data_age[(data_age.index >=15) & (data_age.index<20)].sum()
    dict['20-25'] = data_age[(data_age.index >=20) & (data_age.index<25)].sum()
    dict['25-30'] = data_age[(data_age.index >=25) & (data_age.index<30)].sum()
    dict['30-35'] = data_age[(data_age.index >=30) & (data_age.index<35)].sum()
    dict['35-40'] = data_age[(data_age.index >=35) & (data_age.index<40)].sum()
    dict['40-45'] = data_age[(data_age.index >=40) & (data_age.index<45)].sum()
    dict['45-50'] = data_age[(data_age.index >=45) & (data_age.index<50)].sum()
    dict['50-55'] = data_age[(data_age.index >=50) & (data_age.index<55)].sum()
    dict['55-60'] = data_age[(data_age.index >=55) & (data_age.index<60)].sum()
    dict['60以上'] = data_age[(data_age.index >=60)].sum()
    result['MainClass'] = {'年龄_MainClass_Range': {'ClassifyValue': dict}}
    result['MainClassTotal'] = {'年龄汇总': data.age.count()}
    return result
def get_brand_model(data):
    brands=['华为', '华为荣耀', '苹果', '小米', 'OPPO', 'vivo', '三星', '魅族', '360', '联想']
    data_brand_model=data[['brand','model']][data.brand.isin(brands)]
    dict_new={}
    for i in brands:
        data_model=data_brand_model[data_brand_model.brand==i].model.value_counts()
        data_model_dict=dict(data_model)
        dict_new[i]={'ClassifyValue':data_model_dict,'ChildClassTotal':len(data[data.brand==i])}
    dict_new.update(荣耀=dict_new.pop('华为荣耀'))
    dict_class={}
    dict_class['ChildClass']=dict_new
    dict_result={}
    dict_result['MainClass']={'手机品牌_MainClass_Equal':dict_class}
    dict_result['MainClassTotal']={'手机品牌汇总':len(data_brand_model)}
    return dict_result

def get_brand_model2(data):
    brands=[ '华为荣耀', '苹果', '小米', 'OPPO', 'vivo', '三星', '魅族', '360', '联想']
    data_brand_model=data[['brand','model']][data.brand.isin(brands)]
    dict_new={}
    for i in brands:
        data_model=data_brand_model[data_brand_model.brand==i].model.value_counts()
        data_model_dicts=dict(data_model)
        data_model_dict_new={}
        #print(data_model_dicts)
        for j in data_model_dicts.keys():
            if j.upper() not in list(map(lambda x:x.upper(),data_model_dict_new.keys())):
                #print(j)
                data_model_dict_new[j]=data_model_dicts[j]
            else:
                for keys_new in data_model_dict_new.keys():
                    if keys_new.upper()==j.upper():
                        data_model_dict_new[keys_new]+=data_model_dicts[j]
                    else:
                        pass
        dict_new[i]={'ClassifyValue':data_model_dict_new,'ChildClassTotal':len(data[data.brand==i])}
    dict_new.update(荣耀=dict_new.pop('华为荣耀'))
    dict_class={}
    dict_class['ChildClass']=dict_new
    dict_result={}
    dict_result['MainClass']={'手机品牌_MainClass_Equal':dict_class}
    dict_result['MainClassTotal']={'手机品牌汇总':len(data_brand_model)}
    return dict_result

def get_netlong(data):
    data_netlong=data.netlong.fillna(value=100)
    data_result=data_netlong.value_counts()
    dict={}
    dict['0-3'] = data_result[(data_result.index >= 0) & (data_result.index < 3)].sum()
    dict['3-6'] = data_result[(data_result.index >= 3) & (data_result.index < 6)].sum()
    dict['6-12'] = data_result[(data_result.index>= 6) & (data_result.index < 12)].sum()
    dict['12-24'] = data_result[(data_result.index>= 12) & (data_result.index < 24)].sum()
    dict['24-36'] = data_result[(data_result.index>= 24) & (data_result.index < 36)].sum()
    dict['36以上'] =data_result[data_result.index>=36].sum()
    result={}
    result['MainClass'] = {'在网时长_MainClass_Range': {'ClassifyValue': dict}}
    result['MainClassTotal'] = {'在网时长汇总': data.age.count()}
    return result
def get_mobilecard_brand(data):
    data_card_type=data[data.card_type.isin([1,2,3,4])].card_type
    data_result=data_card_type.value_counts()
    dict={}
    dict['全球通']=data_result[1]
    dict['动感地带']=data_result[2]
    dict['神州行']=data_result[3]
    dict['大众卡']=data_result[4]
    result={}
    result['MainClass'] = {'手机卡品牌_MainClass_Equal': {'ClassifyValue': dict}}
    result['MainClassTotal'] = {'手机卡品牌汇总': data.age.count()}
    return result

def get_city(data):
    owner_city=data.owner_city
    citys=dict(owner_city.value_counts())
    city_list=[]
    zhixiacity={}
    for (i,j) in citys.items():
        if i[0] in ['黑','内']:
            city_list.append([i[:3]+'省',i[3:]+'市',int(j)])
        elif i[:2] in ['北京','天津','重庆','上海']:
            city_=i[:2]+'市'
            if city_ not in zhixiacity.keys():
                zhixiacity[city_]=j
            else:
                zhixiacity[city_]+=j
        else:
            city_list.append([i[:2]+'省',i[2:]+'市',int(j)])
    city=pd.DataFrame(data=np.array(city_list),columns=['省','市','人数'])
    provinces=list(set(city['省']))
    results={}
    city_renshu_allprovince=pd.Series(data=city['人数'],dtype=np.int32)
    for i in ['北京市','天津市','重庆市','上海市']:
        results[i]={'ClassifyValue':{i:zhixiacity[i]},'ChildClassTotal':zhixiacity[i]}
    for provin in provinces:
        city_reshu_data=city[['人数']][city['省'] == provin]
        city_renshu = pd.Series(data=city_reshu_data['人数'], dtype=np.int32)
        data_result = city[['市', '人数']][city['省'] == provin]
        data_series=pd.Series(data=data_result['人数'].values,dtype=np.int32,index=data_result['市'].values)
        data_pro_city=dict(data_series)
        results[provin]={'ClassifyValue':data_pro_city,'ChildClassTotal':city_renshu.sum()}
    result_dict={}
    result_dict['MainClass']={'号码归属地_MainClass_Equal':{'ChildClass':results}}
    result_dict['MainClassTotal']={'号码归属地汇总':city_renshu_allprovince.sum()}
    return result_dict
def get_arpu(data):
    data_arpu = data.Arpu.value_counts()
    dicts={}
    dicts['0'] = data_arpu[(data_arpu.index == 0)].sum()
    dicts['0-10'] = data_arpu[(data_arpu.index > 0) & (data_arpu.index < 10)].sum()
    dicts['10-50'] = data_arpu[(data_arpu.index >= 10) & (data_arpu.index < 50)].sum()
    dicts['50-100'] = data_arpu[(data_arpu.index >= 50) & (data_arpu.index < 100)].sum()
    dicts['100-150'] = data_arpu[(data_arpu.index >= 100) & (data_arpu.index< 150)].sum()
    dicts['150-200'] = data_arpu[(data_arpu.index >= 150) & (data_arpu.index< 200)].sum()
    dicts['200-300'] = data_arpu[(data_arpu.index >= 200) & (data_arpu.index< 300)].sum()
    dicts['300以上'] = data_arpu[(data_arpu.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'本月费用总arpu_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'本月费用总arpu汇总': data.Arpu.count()}
    return result
def get_out_prdct_fee(data):
    data_out_prdct_fee=data.out_prdct_fee.value_counts()
    dicts={}
    dicts['0'] = data_out_prdct_fee[(data_out_prdct_fee.index == 0)].sum()
    dicts['0-10'] = data_out_prdct_fee[(data_out_prdct_fee.index > 0) & (data_out_prdct_fee.index < 10)].sum()
    dicts['10-50'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 10) & (data_out_prdct_fee.index < 50)].sum()
    dicts['50-100'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 50) & (data_out_prdct_fee.index < 100)].sum()
    dicts['100-150'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 100) & (data_out_prdct_fee.index < 150)].sum()
    dicts['150-200'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 150) & (data_out_prdct_fee.index < 200)].sum()
    dicts['200-300'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 200) & (data_out_prdct_fee.index < 300)].sum()
    dicts['300以上'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'本月套餐外总消费_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'本月套餐外总消费汇总': data.out_prdct_fee.count()}
    return result
def get_myfee(data):
    data_myth_fee=data.myth_fee.value_counts()
    dicts={}
    dicts['0'] = data_myth_fee[(data_myth_fee.index == 0)].sum()
    dicts['0-10'] = data_myth_fee[(data_myth_fee.index > 0) & (data_myth_fee.index < 10)].sum()
    dicts['10-50'] = data_myth_fee[(data_myth_fee.index >= 10) & (data_myth_fee.index < 50)].sum()
    dicts['50-100'] = data_myth_fee[(data_myth_fee.index >= 50) & (data_myth_fee.index < 100)].sum()
    dicts['100-150'] = data_myth_fee[(data_myth_fee.index >= 100) & (data_myth_fee.index < 150)].sum()
    dicts['150-200'] = data_myth_fee[(data_myth_fee.index >= 150) & (data_myth_fee.index < 200)].sum()
    dicts['200-300'] = data_myth_fee[(data_myth_fee.index >= 200) & (data_myth_fee.index < 300)].sum()
    dicts['300以上'] = data_myth_fee[(data_myth_fee.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'国际漫游总费用_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'国际漫游总费用汇总': data.myth_fee.count()}
    return result
def get_point_fee(data):
    data_point_fee = data.point_fee.value_counts()
    dicts={}
    dicts['0']=data_point_fee[(data_point_fee.index==0)].sum()
    dicts['0-2000'] = data_point_fee[(data_point_fee.index > 0)&(data_point_fee.index <2000)].sum()
    dicts['2000-5000'] = data_point_fee[(data_point_fee.index >=2000) & (data_point_fee.index < 5000)].sum()
    dicts['5000以上'] = data_point_fee[(data_point_fee.index >=5000)].sum()
    result = {}
    result['MainClass'] = {'积分余额_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'积分余额汇总': data.point_fee.count()}
    return result
def get_credit_limit(data):
    data_credit_limit=data.credit_limit.value_counts()
    dicts = {}
    dicts['0'] = data_credit_limit[(data_credit_limit.index == 0)].sum()
    dicts['0-10000'] = data_credit_limit[(data_credit_limit.index > 0) & (data_credit_limit.index < 10000)].sum()
    dicts['10000-30000'] = data_credit_limit[(data_credit_limit.index >=10000) & (data_credit_limit.index < 30000)].sum()
    dicts['30000-50000'] = data_credit_limit[(data_credit_limit.index >=30000) & (data_credit_limit.index < 50000)].sum()
    dicts['50000以上'] = data_credit_limit[(data_credit_limit.index >= 50000)].sum()
    result = {}
    result['MainClass'] = {'信用额度_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'信用额度汇总': data.credit_limit.count()}
    return result
def get_credit_payment_avg(data):
    data_credit_payment_avg = data.credit_payment_avg.value_counts()
    dicts = {}
    dicts['0'] = data_credit_payment_avg[(data_credit_payment_avg.index == 0)].sum()
    dicts['0-10000'] = data_credit_payment_avg[(data_credit_payment_avg.index > 0) & (data_credit_payment_avg.index < 10000)].sum()
    dicts['10000-30000'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 10000) & (data_credit_payment_avg.index < 30000)].sum()
    dicts['30000-50000'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 30000) & (data_credit_payment_avg.index < 50000)].sum()
    dicts['50000以上'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 50000)].sum()
    result = {}
    result['MainClass'] = {'信用卡年度支出_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'信用卡年度支出汇总': data.credit_payment_avg.count()}
    return result

def OriginDataStatistics(OriginDataPath):
    ReceiveStandardDataList=[]
    data = pd.read_table(OriginDataPath, delimiter='|', encoding='utf-8',
                         na_values='null', header=None, low_memory=False)
    data.columns = ['Userid', 'mobile', 'imsi', 'imei', 'name', 'age', 'sex', 'status', 'mobile_reg_time',
                    'mobile_cancel_time', 'netlong', 'yunys_type', 'card_brand', 'user_level', 'roster',
                    'owner_city', 'brand', 'model', 'mobile_system', 'user_hyyf_client', 'Location', 'Arpu',
                    'arpu_avg', 'prdct_fee', 'prdct_fee_avg', 'out_prdct_fee', 'out_prdct_fee_avg',
                    'myth_fee', 'myth_fee_avg', 'point_fee', 'credit_limit', 'credit_payment', 'credit_payment_avg',
                    'insur_type', 'insur_money', 'hotel_money_avg', 'hotel_type', 'traffic_type', 'traffic_money_avg',
                    'top100_appname', 'international', 'asia_roaming', 'au_roaming', 'na_roaming', 'sea_roaming',
                    'eu_roaming', 'hk_mc_tw_roaming', 'jap_kor_roaming', 'other_roaming', 'tx_member',
                    'tencent_kingcard', 'qq_member', 'qq_red', 'qq_yellow', 'qq_bule', 'qq_green',
                    'qq_magic', 'qq_ststion', 'sup_qq', 'qq_car', 'video_member', 'iqiyi', 'hbmg', 'mango_tv', 'youku',
                    'tencent_tv', 'migu_tv', 'leeco', 'cmcc', 'pptv', 'other_tv', 'realty', 'automobile',
                    'traffic_violation',
                    'car_maintenance', 'car_news', 'network_car', 'gps', 'carer_app', 'traffic_information', 'game',
                    'read',
                    'Ifeng_read', 'mobile_read', 'news_affairs', 'other_read', 'finance', 'financial_management',
                    'stock',
                    'Securities', 'bank', 'gold', 'music', 'migu_music', 'music_package', 'pop_music', 'crbt',
                    'music_activities',
                    'sports', 'cartoon', 'merchant_travel', 'education', 'parent_child_education', 'growth_plan',
                    'family_books',
                    'education_publicity', 'health_education', 'house', 'community', 'real_estate', 'cadres', 'police',
                    'civil_servant',
                    'group_client', 'family_client', 'campus_client', 'adis']

    # #print(get_credit_payment_avg())
    #print(get_sex(data))
    # print(get_age(data))
    #print(get_brand_model2(data))
    # #print(get_mobilecard_brand())
    # print(get_netlong(data))
    # print(get_city(data))
    ReceiveStandardDataList.append(copy.deepcopy(get_sex(data)))
    ReceiveStandardDataList.append(copy.deepcopy(get_age(data)))
    ReceiveStandardDataList.append(copy.deepcopy(get_brand_model2(data)))
    ReceiveStandardDataList.append(copy.deepcopy(get_netlong(data)))
    ReceiveStandardDataList.append(copy.deepcopy(get_city(data)))
    # print(ReceiveStandardDataList)
    return ReceiveStandardDataList














