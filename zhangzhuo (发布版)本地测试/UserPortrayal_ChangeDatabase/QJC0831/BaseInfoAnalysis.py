import numpy as np
import pandas as pd
class BaseAnalysis():
    def __init__(self,datapath):
        self.datapath=datapath
        self.data=pd.read_table(self.datapath, delimiter='|', encoding='utf-8',low_memory=False,dtype={'star_type':str})
    def get_sex(self):
        data_sex=self.data.sex.value_counts()
        result={}
        dicts={}
        dicts['男']=data_sex[1]
        dicts['女'] = data_sex[0]
        result['MainClass'] ={'性别_MainClass_Equal': {'ClassifyValue':dicts}}
        result['MainClassTotal']={'性别汇总': self.data.sex.count()}
        return result
    def get_age(self):
        data_age=self.data.age.value_counts()
        result={}
        dicts={}
        dicts['0-15']=data_age[(data_age.index>=0)&(data_age.index<15)].sum()
        dicts['15-20'] = data_age[(data_age.index >=15) & (data_age.index<20)].sum()
        dicts['20-25'] = data_age[(data_age.index >=20) & (data_age.index<25)].sum()
        dicts['25-30'] = data_age[(data_age.index >=25) & (data_age.index<30)].sum()
        dicts['30-35'] = data_age[(data_age.index >=30) & (data_age.index<35)].sum()
        dicts['35-40'] = data_age[(data_age.index >=35) & (data_age.index<40)].sum()
        dicts['40-45'] = data_age[(data_age.index >=40) & (data_age.index<45)].sum()
        dicts['45-50'] = data_age[(data_age.index >=45) & (data_age.index<50)].sum()
        dicts['50-55'] = data_age[(data_age.index >=50) & (data_age.index<55)].sum()
        dicts['55-60'] = data_age[(data_age.index >=55) & (data_age.index<60)].sum()
        dicts['60以上'] = data_age[(data_age.index >=60)].sum()
        result['MainClass'] = {'年龄_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'年龄汇总': self.data.age.count()}
        return result
    def get_brand_model(self):
        brands = ['华为', '华为荣耀', '苹果', '小米', 'OPPO', 'vivo', '三星', '魅族', '360', '联想', '乐视', '金立']
        data_brand_model=self.data[['brand','model']][self.data.brand.isin(brands)]
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
            dict_new[i]={'ClassifyValue':data_model_dict_new,'ChildClassTotal':len(self.data[self.data.brand==i])}
        #dict_new.update(荣耀=dict_new.pop('华为荣耀'))
        dict_class={}
        dict_class['ChildClass']=dict_new
        dict_result={}
        dict_result['MainClass']={'手机品牌_MainClass_Equal':dict_class}
        dict_result['MainClassTotal']={'手机品牌汇总':len(data_brand_model)}
        return dict_result

    def get_listing_date(self):
        data_listing_date=self.data.listing_date.value_counts()
        dicts = {}
        #print(data_listing_date)
        for i in range(2000, 2019):
            for j in dict(data_listing_date).items():
                #print(j,type(j))
                #print(j)
                list_buf=list(j)
                #print(list_buf,str(i))
                list_buf[0]=str(list_buf[0])
                if list_buf[0][0:4] == str(i):
                    if (str(i)) not in dicts.keys():
                        dicts[str(i)] = int(list_buf[1])
                    else:
                        dicts[str(i)] += int(list_buf[1])
        result = {}
        result['MainClass'] = {'上市时间_MainClass_Equal': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'上市时间汇总': self.data.listing_date.count()}
        #print('上市时间：',result)
        return result
    
    def get_listing_price(self):
        data_new=self.data.listing_price.apply(pd.to_numeric,errors='coerce')
        data_listing_price =data_new.value_counts()
        dicts = {}
        dicts['0-500']=data_listing_price[(data_listing_price.index<500)].sum()
        dicts['500-1000'] = data_listing_price[(data_listing_price.index >=500)&(data_listing_price.index <1000)].sum()
        dicts['1000-1500'] = data_listing_price[(data_listing_price.index >=1000) & (data_listing_price.index < 1500)].sum()
        dicts['1500-2000'] = data_listing_price[(data_listing_price.index >=1500) & (data_listing_price.index < 2000)].sum()
        dicts['2000-2500'] = data_listing_price[(data_listing_price.index >=2000) & (data_listing_price.index < 2500)].sum()
        dicts['2500-3000'] = data_listing_price[(data_listing_price.index >=2500) & (data_listing_price.index < 3000)].sum()
        dicts['3000-3500'] = data_listing_price[(data_listing_price.index >=3000) & (data_listing_price.index < 3500)].sum()
        dicts['3500-4000'] = data_listing_price[(data_listing_price.index >=3500) & (data_listing_price.index < 4000)].sum()
        dicts['4000-4500'] = data_listing_price[(data_listing_price.index >=4000) & (data_listing_price.index < 4500)].sum()
        dicts['4500-5000'] = data_listing_price[(data_listing_price.index >=4500) & (data_listing_price.index < 5000)].sum()
        dicts['5000-5500'] = data_listing_price[(data_listing_price.index >=5000) & (data_listing_price.index < 5500)].sum()
        dicts['5500-6000'] =data_listing_price[(data_listing_price.index  >=5500) & (data_listing_price.index < 6000)].sum()
        dicts['6000-6500'] = data_listing_price[(data_listing_price.index >=6000) & (data_listing_price.index < 6500)].sum()
        dicts['6500-7000'] = data_listing_price[(data_listing_price.index >=6500) & (data_listing_price.index < 7000)].sum()
        dicts['7000-7500'] = data_listing_price[(data_listing_price.index >=7000) & (data_listing_price.index < 7500)].sum()
        dicts['7500-8000'] = data_listing_price[(data_listing_price.index >=7500) & (data_listing_price.index < 8000)].sum()
        dicts['8000-8500'] = data_listing_price[(data_listing_price.index >=8000) & (data_listing_price.index < 8500)].sum()
        dicts['8500-9000'] = data_listing_price[(data_listing_price.index >=8500) & (data_listing_price.index < 9000)].sum()
        dicts['9000-9500'] = data_listing_price[(data_listing_price.index >=9000) & (data_listing_price.index < 9500)].sum()
        dicts['9500以上']=data_listing_price[(data_listing_price.index >=9500)].sum()
        result = {}
        result['MainClass'] = {'上市价格_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'上市价格汇总': sum(dicts.values())}
        return result
    def get_netlong(self):
        data_netlong=self.data.netlong.fillna(value=100)
        data_result=data_netlong.value_counts()
        dicts={}
        dicts['0-3'] = data_result[(data_result.index >= 0) & (data_result.index < 3)].sum()
        dicts['3-6'] = data_result[(data_result.index >= 3) & (data_result.index < 6)].sum()
        dicts['6-12'] = data_result[(data_result.index>= 6) & (data_result.index < 12)].sum()
        dicts['12-24'] = data_result[(data_result.index>= 12) & (data_result.index < 24)].sum()
        dicts['24-36'] = data_result[(data_result.index>= 24) & (data_result.index < 36)].sum()
        dicts['36以上'] =data_result[data_result.index>=36].sum()
        result={}
        result['MainClass'] = {'在网时长_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'在网时长汇总': data_result.sum()}
        return result
    def get_card_type(self):
        data_card_type=self.data.card_type.value_counts()
        data_card_type_sum=self.data.card_type.count()
        dicts={}
        dicts['全球通']=data_card_type[data_card_type.index==1].sum()
        dicts['动感地带']=data_card_type[data_card_type.index==2].sum()
        dicts['神州行']=data_card_type[data_card_type.index==3].sum()
        dicts['大众卡']=data_card_type[data_card_type.index==4].sum()
        dicts['其他']=data_card_type_sum-dicts['全球通']-dicts['动感地带']-dicts['神州行']-dicts['大众卡']
        result={}
        result['MainClass'] = {'手机卡品牌_MainClass_Equal': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'手机卡品牌汇总': data_card_type_sum}
        return result
    def get_star_type(self):
        data_star_type = self.data.star_type.value_counts()
        dicts = {}
        list_0_5 = ['0', '1', '2', '3', '4', '5', '-999', '一星级', '二星级', '三星级', '四星级', '五星级','未评级']
        dicts['0星用户'] = data_star_type[(data_star_type.index == '0') | (data_star_type.index == '-999') | (data_star_type.index == '未评级')].sum()
        dicts['1星用户'] = data_star_type[(data_star_type.index == '1') | (data_star_type.index == '一星级')].sum()
        dicts['2星用户'] = data_star_type[(data_star_type.index == '2') | (data_star_type.index == '二星级')].sum()
        dicts['3星用户'] = data_star_type[(data_star_type.index == '3') | (data_star_type.index == '三星级')].sum()
        dicts['4星用户'] = data_star_type[(data_star_type.index == '4') | (data_star_type.index == '四星级')].sum()
        dicts['5星用户'] = data_star_type[(data_star_type.index == '5') | (data_star_type.index == '五星级')].sum()
        dicts['5星以上用户'] = data_star_type[
            (data_star_type.index.isin([x for x in list(data_star_type.index) if x not in list_0_5]))].sum()
        result = {}
        result['MainClass'] = {'用户星级_MainClass_Equal': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'用户星级汇总': self.data.star_type.count()}
        return result

    def get_city(self):
        owner_city=self.data.owner_city
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
            for i in list(zhixiacity.keys()):
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
        result_dict['MainClassTotal']={'号码归属地汇总':owner_city.count()}
        return result_dict
    def get_arpu(self):
        data_arpu = self.data.arpu.value_counts()
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
        result['MainClassTotal'] = {'本月费用总arpu汇总': self.data.arpu.count()}
        return result
    def get_out_prdct_fee(self):
        data_out_prdct_fee=self.data.out_prdct_fee.value_counts()
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
        result['MainClassTotal'] = {'本月套餐外总消费汇总': self.data.out_prdct_fee.count()}
        return result
    def get_myfee(self):
        data_myth_fee=self.data.myth_fee.value_counts()
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
        result['MainClassTotal'] = {'国际漫游总费用汇总': self.data.myth_fee.count()}
        return result
    def get_point_fee(self):
        data_point_fee = self.data.point_fee.value_counts()
        dicts={}
        dicts['0']=data_point_fee[(data_point_fee.index==0)].sum()
        dicts['0-2000'] = data_point_fee[(data_point_fee.index > 0)&(data_point_fee.index <2000)].sum()
        dicts['2000-5000'] = data_point_fee[(data_point_fee.index >=2000) & (data_point_fee.index < 5000)].sum()
        dicts['5000以上'] = data_point_fee[(data_point_fee.index >=5000)].sum()
        result = {}
        result['MainClass'] = {'积分余额_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'积分余额汇总': self.data.point_fee.count()}
        return result
    def get_credit_limit(self):
        data_credit_limit=self.data.credit_limit.value_counts()
        dicts = {}
        dicts['0'] = data_credit_limit[(data_credit_limit.index == 0)].sum()
        dicts['0-10000'] = data_credit_limit[(data_credit_limit.index > 0) & (data_credit_limit.index < 10000)].sum()
        dicts['10000-30000'] = data_credit_limit[(data_credit_limit.index >=10000) & (data_credit_limit.index < 30000)].sum()
        dicts['30000-50000'] = data_credit_limit[(data_credit_limit.index >=30000) & (data_credit_limit.index < 50000)].sum()
        dicts['50000以上'] = data_credit_limit[(data_credit_limit.index >= 50000)].sum()
        result = {}
        result['MainClass'] = {'信用额度_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'信用额度汇总': self.data.credit_limit.count()}
        return result
    def get_credit_payment_avg(self):
        data_credit_payment_avg = self.data.credit_payment_avg.value_counts()
        dicts = {}
        dicts['0'] = data_credit_payment_avg[(data_credit_payment_avg.index == 0)].sum()
        dicts['0-10000'] = data_credit_payment_avg[(data_credit_payment_avg.index > 0) & (data_credit_payment_avg.index < 10000)].sum()
        dicts['10000-30000'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 10000) & (data_credit_payment_avg.index < 30000)].sum()
        dicts['30000-50000'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 30000) & (data_credit_payment_avg.index < 50000)].sum()
        dicts['50000以上'] = data_credit_payment_avg[(data_credit_payment_avg.index >= 50000)].sum()
        result = {}
        result['MainClass'] = {'信用卡年度支出_MainClass_Range': {'ClassifyValue': dicts}}
        result['MainClassTotal'] = {'信用卡年度支出汇总': self.data.credit_payment_avg.count()}
        return result
    def get_location(self):
        data_location=self.data.location.value_counts()
        counts=data_location.sum()
        result={}
        result['MainClass']={'所属区县_MainClass_Equal': {'ClassifyValue': dict(data_location)}}
        result['MainClassTotal']={'所属区县汇总':counts}
        return result

























