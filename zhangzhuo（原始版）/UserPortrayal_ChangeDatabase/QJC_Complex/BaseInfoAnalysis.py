import numpy as np
import pandas as pd
import BaseInfo
data=pd.read_table(BaseInfo.data_path, delimiter='|', encoding='utf-8',
                   na_values='null', low_memory=False)
data.columns=['mobile', 'sex', 'age', 'brand', 'model', 'listing_date',
       'listing_price', 'netlong', 'card_type', 'star_type', 'owner_city',
       'arpu', 'out_prdct_fee', 'myth_fee', 'point_fee', 'credit_limit',
       'credit_payment_avg','location']
#print(data.location)
def get_sex():
    data_sex=data.sex.value_counts()
    result={}
    dicts={}
    dicts['男']=data_sex[1]
    dicts['女'] = data_sex[0]
    result['MainClass'] ={'性别_MainClass_Equal': {'ClassifyValue':dicts}}
    result['MainClassTotal']={'性别汇总': data.sex.count()}
    return result
def get_age():
    data_age=data.age.value_counts()
    result={}
    dicts={}
    dicts['0-15岁']=data_age[(data_age.index>=0)&(data_age.index<15)].sum()
    dicts['15-20岁'] = data_age[(data_age.index >=15) & (data_age.index<20)].sum()
    dicts['20-25岁'] = data_age[(data_age.index >=20) & (data_age.index<25)].sum()
    dicts['25-30岁'] = data_age[(data_age.index >=25) & (data_age.index<30)].sum()
    dicts['30-35岁'] = data_age[(data_age.index >=30) & (data_age.index<35)].sum()
    dicts['35-40岁'] = data_age[(data_age.index >=35) & (data_age.index<40)].sum()
    dicts['40-45岁'] = data_age[(data_age.index >=40) & (data_age.index<45)].sum()
    dicts['45-50岁'] = data_age[(data_age.index >=45) & (data_age.index<50)].sum()
    dicts['50-55岁'] = data_age[(data_age.index >=50) & (data_age.index<55)].sum()
    dicts['55-60岁'] = data_age[(data_age.index >=55) & (data_age.index<60)].sum()
    dicts['60岁以上'] = data_age[(data_age.index >=60)].sum()
    result['MainClass'] = {'年龄_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'年龄汇总': data.age.count()}
    return result
def get_brand_model():
    brands=[ '华为荣耀', '苹果', '小米', 'OPPO', 'vivo', '三星', '魅族', '360', '联想']
    data_brand_model=data[['brand','model']][data.brand.isin(brands)]
    dict_new={}
    for i in brands:
        data_model=data_brand_model[data_brand_model.brand==i].model.value_counts()
        data_model_dicts=dict(data_model)
        data_model_dict_new={}
        for j in data_model_dicts.keys():
            if j.upper() not in list(map(lambda x:x.upper(),data_model_dict_new.keys())):
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
def get_listing_date():
    data_listing_date=data.listing_date.value_counts()
    dicts = {}
    for i in range(2000, 2019):
        for j in dict(data_listing_date).items():
            if j[0][:4] == str(i):
                if (str(i)+'年') not in dicts.keys():
                    dicts[str(i)+'年'] = int(j[1])
                else:
                    dicts[str(i)+'年'] += int(j[1])
    result = {}
    result['MainClass'] = {'上市时间_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'上市时间汇总': data.listing_date.count()}
    return result
def get_listing_price():
    data_new=data.listing_price.apply(pd.to_numeric,errors='coerce')
    data_listing_price =data_new.value_counts()
    dicts = {}
    dicts['500-1000元'] = data_listing_price[(data_listing_price.index >=500)&(data_listing_price.index <=1000)].sum()
    dicts['1500-2000元'] = data_listing_price[(data_listing_price.index >=1500) & (data_listing_price.index <= 2000)].sum()
    dicts['2500-3000元'] = data_listing_price[(data_listing_price.index >= 2500) & (data_listing_price.index <=3000)].sum()
    dicts['3500-4000元'] = data_listing_price[(data_listing_price.index >= 3500) & (data_listing_price.index <4000)].sum()
    dicts['4500-5000元'] = data_listing_price[(data_listing_price.index >=4500) & (data_listing_price.index <=5000)].sum()
    dicts['5500-6000元'] = data_listing_price[(data_listing_price.index >=5500) & (data_listing_price.index <=6000)].sum()
    dicts['6500-7000元'] = data_listing_price[(data_listing_price.index >=6500) & (data_listing_price.index <=7000)].sum()
    dicts['7500-8000元'] = data_listing_price[(data_listing_price.index >= 7500) & (data_listing_price.index <= 8000)].sum()
    dicts['8500-9000元'] = data_listing_price[(data_listing_price.index >= 8500) & (data_listing_price.index <= 9000)].sum()
    dicts['9500-10000元'] = data_listing_price[(data_listing_price.index >= 9500) & (data_listing_price.index <= 10000)].sum()
    dicts['10000元以上']=data_listing_price[(data_listing_price.index >10000)].sum()
    result = {}
    result['MainClass'] = {'上市价格总_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'上市价格汇总': data.listing_price.count()}
    return result
def get_netlong():
    data_netlong=data.netlong.fillna(value=100)
    data_result=data_netlong.value_counts()
    dicts={}
    dicts['0-3月'] = data_result[(data_result.index >= 0) & (data_result.index < 3)].sum()
    dicts['3-6月'] = data_result[(data_result.index >= 3) & (data_result.index < 6)].sum()
    dicts['6-12月'] = data_result[(data_result.index>= 6) & (data_result.index < 12)].sum()
    dicts['12-24月'] = data_result[(data_result.index>= 12) & (data_result.index < 24)].sum()
    dicts['24-36月'] = data_result[(data_result.index>= 24) & (data_result.index < 36)].sum()
    dicts['36月以上'] =data_result[data_result.index>=36].sum()
    result={}
    result['MainClass'] = {'在网时长_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'在网时长汇总': data.age.count()}
    return result
def get_card_type():
    data_card_type=data.card_type.value_counts()
    dicts={}
    dicts['全球通']=data_card_type[data_card_type.index==1].sum()
    dicts['动感地带']=data_card_type[data_card_type.index==2].sum()
    dicts['神州行']=data_card_type[data_card_type.index==3].sum()
    dicts['大众卡']=data_card_type[data_card_type.index==4].sum()
    result={}
    result['MainClass'] = {'手机卡品牌_MainClass_Equal': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'手机卡品牌汇总': data.age.count()}
    return result
def get_star_type():
    data_star_type = data.star_type.value_counts()
    dicts = {}
    dicts['0星用户'] = data_star_type[(data_star_type.index==0)|(data_star_type.index==-999)].sum()
    dicts['1星用户'] = data_star_type[(data_star_type.index==1)].sum()
    dicts['2星用户'] = data_star_type[(data_star_type.index==2)].sum()
    dicts['3星用户'] = data_star_type[(data_star_type.index==3)].sum()
    dicts['4星用户'] = data_star_type[(data_star_type.index==4)].sum()
    dicts['5星用户'] = data_star_type[(data_star_type.index==5)].sum()
    dicts['5星以上用户'] = data_star_type[(data_star_type.index>=6)].sum()
    result = {}
    result['MainClass'] = {'用户星级_MainClass_Equal': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'用户星级汇总': data.star_type.count()}
    return result
def get_city():
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
    try:
        for i in ['北京市','天津市','重庆市','上海市']:
            results[i]={'ClassifyValue':{i:zhixiacity[i]},'ChildClassTotal':zhixiacity[i]}
    except:
        pass
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
def get_arpu():
    data_arpu = data.arpu.value_counts()
    dicts={}
    dicts['0元'] = data_arpu[(data_arpu.index == 0)].sum()
    dicts['0-10元'] = data_arpu[(data_arpu.index > 0) & (data_arpu.index < 10)].sum()
    dicts['10-50元'] = data_arpu[(data_arpu.index >= 10) & (data_arpu.index < 50)].sum()
    dicts['50-100元'] = data_arpu[(data_arpu.index >= 50) & (data_arpu.index < 100)].sum()
    dicts['100-150元'] = data_arpu[(data_arpu.index >= 100) & (data_arpu.index< 150)].sum()
    dicts['150-200元'] = data_arpu[(data_arpu.index >= 150) & (data_arpu.index< 200)].sum()
    dicts['200-300元'] = data_arpu[(data_arpu.index >= 200) & (data_arpu.index< 300)].sum()
    dicts['300元以上'] = data_arpu[(data_arpu.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'本月费用总arpu_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'本月费用总arpu汇总': data.arpu.count()}
    return result
def get_out_prdct_fee():
    data_out_prdct_fee=data.out_prdct_fee.value_counts()
    dicts={}
    dicts['0元'] = data_out_prdct_fee[(data_out_prdct_fee.index == 0)].sum()
    dicts['0-10元'] = data_out_prdct_fee[(data_out_prdct_fee.index > 0) & (data_out_prdct_fee.index < 10)].sum()
    dicts['10-50元'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 10) & (data_out_prdct_fee.index < 50)].sum()
    dicts['50-100元'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 50) & (data_out_prdct_fee.index < 100)].sum()
    dicts['100-150元'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 100) & (data_out_prdct_fee.index < 150)].sum()
    dicts['150-200元'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 150) & (data_out_prdct_fee.index < 200)].sum()
    dicts['200-300元'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 200) & (data_out_prdct_fee.index < 300)].sum()
    dicts['300元以上'] = data_out_prdct_fee[(data_out_prdct_fee.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'本月套餐外总消费_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'本月套餐外总消费汇总': data.out_prdct_fee.count()}
    return result
def get_myfee():
    data_myth_fee=data.myth_fee.value_counts()
    dicts={}
    dicts['0元'] = data_myth_fee[(data_myth_fee.index == 0)].sum()
    dicts['0-10元'] = data_myth_fee[(data_myth_fee.index > 0) & (data_myth_fee.index < 10)].sum()
    dicts['10-50元'] = data_myth_fee[(data_myth_fee.index >= 10) & (data_myth_fee.index < 50)].sum()
    dicts['50-100元'] = data_myth_fee[(data_myth_fee.index >= 50) & (data_myth_fee.index < 100)].sum()
    dicts['100-150元'] = data_myth_fee[(data_myth_fee.index >= 100) & (data_myth_fee.index < 150)].sum()
    dicts['150-200元'] = data_myth_fee[(data_myth_fee.index >= 150) & (data_myth_fee.index < 200)].sum()
    dicts['200-300元'] = data_myth_fee[(data_myth_fee.index >= 200) & (data_myth_fee.index < 300)].sum()
    dicts['300元以上'] = data_myth_fee[(data_myth_fee.index >= 300)].sum()
    result = {}
    result['MainClass'] = {'国际漫游总费用_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'国际漫游总费用汇总': data.myth_fee.count()}
    return result
def get_point_fee():
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
def get_credit_limit():
    data_credit_limit=data.credit_limit.value_counts()
    dicts = {}
    dicts['0元'] = data_credit_limit[(data_credit_limit.index == 0)].sum()
    dicts['0-10000元'] = data_credit_limit[(data_credit_limit.index > 0) & (data_credit_limit.index < 10000)].sum()
    dicts['10000-30000元'] = data_credit_limit[(data_credit_limit.index >=10000) & (data_credit_limit.index < 30000)].sum()
    dicts['30000-50000元'] = data_credit_limit[(data_credit_limit.index >=30000) & (data_credit_limit.index < 50000)].sum()
    dicts['50000元以上'] = data_credit_limit[(data_credit_limit.index >= 50000)].sum()
    result = {}
    result['MainClass'] = {'信用额度_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'信用额度汇总': data.credit_limit.count()}
    return result
def get_credit_payment_avg():
    data_credit_payment_avg = data.credit_payment_avg.value_counts()
    dicts = {}
    dicts['0元'] = data_credit_payment_avg[(data_credit_payment_avg.index == 0)].sum()
    dicts['0-10000元'] = data_credit_payment_avg[(data_credit_payment_avg.index > 0) & (data_credit_payment_avg.index < 10000)].sum()
    dicts['10000-30000元'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 10000) & (data_credit_payment_avg.index < 30000)].sum()
    dicts['30000-50000元'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 30000) & (data_credit_payment_avg.index < 50000)].sum()
    dicts['50000元以上'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 50000)].sum()
    result = {}
    result['MainClass'] = {'信用卡年度支出_MainClass_Range': {'ClassifyValue': dicts}}
    result['MainClassTotal'] = {'信用卡年度支出汇总': data.credit_payment_avg.count()}
    return result
def get_location():
    data_location=data.location.value_counts()
    counts=data_location.sum()
    result={}
    result['MainClass']={'所属区县_MainClass_Equal': {'ClassifyValue': dict(data_location)}}
    result['MainClassTotal']={'所属区县汇总':counts}
    return result












# print(get_sex())
# print(get_age())
#print(get_brand_model())
# print(get_card_type())
# print(get_netlong())
# print(get_city())













