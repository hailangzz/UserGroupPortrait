import QJC0831.BaseInfoAnalysis as BaseInfoAnalysis
import QJC0831.AppInfoAnalysis as AppInfoAnalysis
import QJC0831.ServiceInfoAnalysis as ServiceInfoAnalysis
import QJC0831.AppInfo as AppInfo
import QJC0831.BaseInfo as BaseInfo
import QJC0831.ServiceInfo as ServiceInfo
import time
import copy

def QJC0831_Main0831_1():
    MultiReceiveStandardDataList = []
    AppInfo_path=AppInfo.data_path
    BaseInfo_path=BaseInfo.data_path
    ServiceInfo_path=ServiceInfo.data_path
    # import time
    filenums=len(AppInfo_path)
    if filenums :
        for filenumber in range(filenums):
            SingleReceiveStandardDataList = []
            start_time=time.time()
            age=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_age()
            sex=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_sex()
            brand_model=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_brand_model()
            listing_date=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_listing_date()
            listing_price = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_listing_price()
            netlong = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_netlong()
            card_type = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_card_type()
            star_type = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_star_type()
            city=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_city()
            arpu=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_arpu()
            out_prdct_fee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_out_prdct_fee()
            myfee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_myfee()
            point_fee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_point_fee()
            credit_limit = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_credit_limit()
            credit_payment_avg = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_credit_payment_avg()
            location = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_location()

            app=AppInfoAnalysis.AppAnalysis(AppInfo_path[filenumber]).get_appname()
            app_classify=AppInfoAnalysis.AppAnalysis(AppInfo_path[filenumber]).get_classifyname()
            service=ServiceInfoAnalysis.ServiceAnalysis(ServiceInfo_path[filenumber]).get_service()
            # end_time=time.time()
            # print(age)
            # print(sex)
            # print(city)
            # print(brand_model)
            # print(location)
            # print(list_date)
            # print(list_price)
            # print(app)
            # print(app_classify)
            # print(service)
            #
            # print('程序运行时间为:%f'%(end_time-start_time))
            SingleReceiveStandardDataList.append(age)
            SingleReceiveStandardDataList.append(sex)
            SingleReceiveStandardDataList.append(brand_model)
            SingleReceiveStandardDataList.append(listing_date)
            SingleReceiveStandardDataList.append(listing_price)
            SingleReceiveStandardDataList.append(card_type)
            SingleReceiveStandardDataList.append(star_type)
            SingleReceiveStandardDataList.append(city)
            SingleReceiveStandardDataList.append(arpu)
            SingleReceiveStandardDataList.append(out_prdct_fee)
            SingleReceiveStandardDataList.append(myfee)
            SingleReceiveStandardDataList.append(point_fee)
            SingleReceiveStandardDataList.append(credit_limit)
            SingleReceiveStandardDataList.append(credit_payment_avg)
            SingleReceiveStandardDataList.append(location)
            SingleReceiveStandardDataList.append(app)
            SingleReceiveStandardDataList.append(app_classify)
            SingleReceiveStandardDataList.append(service)
        MultiReceiveStandardDataList.append(copy.deepcopy(SingleReceiveStandardDataList))
    else:
        print('没有发现新文件，继续扫描')

    return MultiReceiveStandardDataList#缺乏自动运行模块功能···


def QJC0831_Main():
    MultiReceiveStandardDataList = {}
    AppInfo_path=AppInfo.App_data_path().get_path()
    BaseInfo_path=BaseInfo.Basic_data_path().get_path()
    ServiceInfo_path=ServiceInfo.Service_data_path().get_path()
    filenums=len(AppInfo_path) and len(BaseInfo_path) and len(ServiceInfo_path)

    if filenums :
        for filenumber in range(filenums):
            filename=AppInfo_path[filenumber].split('\\')[-1].strip('.txt')

            if filename not in MultiReceiveStandardDataList:
                MultiReceiveStandardDataList[filename]=[]
                start_time=time.time()
                age=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_age()
                sex=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_sex()
                brand_model=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_brand_model()
                listing_date=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_listing_date()
                listing_price = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_listing_price()
                netlong = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_netlong()
                card_type = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_card_type()
                star_type = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_star_type()
                city=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_city()
                arpu=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_arpu()
                out_prdct_fee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_out_prdct_fee()
                myfee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_myfee()
                point_fee=BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_point_fee()
                credit_limit = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_credit_limit()
                credit_payment_avg = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_credit_payment_avg()
                location = BaseInfoAnalysis.BaseAnalysis(BaseInfo_path[filenumber]).get_location()

                app=AppInfoAnalysis.AppAnalysis(AppInfo_path[filenumber]).get_appname()
                app_classify=AppInfoAnalysis.AppAnalysis(AppInfo_path[filenumber]).get_classifyname()
                service=ServiceInfoAnalysis.ServiceAnalysis(ServiceInfo_path[filenumber]).get_service()
                print('%s:Data analysis  completed,waiting for insert database! ' % filename)
                MultiReceiveStandardDataList[filename].append(age)
                MultiReceiveStandardDataList[filename].append(sex)
                MultiReceiveStandardDataList[filename].append(brand_model)
                MultiReceiveStandardDataList[filename].append(listing_date)
                MultiReceiveStandardDataList[filename].append(listing_price)
                MultiReceiveStandardDataList[filename].append(netlong)
                MultiReceiveStandardDataList[filename].append(card_type)
                MultiReceiveStandardDataList[filename].append(star_type)
                MultiReceiveStandardDataList[filename].append(city)
                MultiReceiveStandardDataList[filename].append(arpu)
                MultiReceiveStandardDataList[filename].append(out_prdct_fee)
                MultiReceiveStandardDataList[filename].append(myfee)
                MultiReceiveStandardDataList[filename].append(point_fee)
                MultiReceiveStandardDataList[filename].append(credit_limit)
                MultiReceiveStandardDataList[filename].append(credit_payment_avg)
                MultiReceiveStandardDataList[filename].append(location)
                MultiReceiveStandardDataList[filename].append(app)
                MultiReceiveStandardDataList[filename].append(app_classify)
                MultiReceiveStandardDataList[filename].append(service)
    else:
        print('没有发现新文件，继续扫描')
    print('All analysis task is finished!')
    return MultiReceiveStandardDataList
