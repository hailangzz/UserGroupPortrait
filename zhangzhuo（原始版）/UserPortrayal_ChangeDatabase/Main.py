import GlobalVariable as GV
import MySQLOperation as MSQLO
import OperateClassifyValue as OCV
import OperateCooperationCompany as OCC
import OperateDataExtractBatch as ODEB
import OperateTagClassify as OTC
#import QJC_Single.OriginDataStatistics as ODS
import QJC0831.QJCMain as QJCM
import InitFinalResultRegisterDict as IFRRD
import FillTagClassifyMap as FTCM
import FillClassifyValueMap as FCVM
import FillDataExtractBatch as FDEB
import InsertResultPersonNumber as IRPN
import ExtractPublicTaskInfo as EPTI
import copy
import gc
import EachBatchGroupOperation as EBGO
import UpdateLabelGroupPersonas as ULGP
import time

#最简单的数据插入版本···
def main0826():
    #MysqlObject=MSQLO.Mysql('192.168.7.31',3306,'ngoss_dim','ngoss_dim')
    MysqlObject = MSQLO.Mysql('127.0.0.1', 3306, 'root', 'mysql')
    #print(MysqlObject._UseDatabase)
    OriginDataPath=r'./QJC_Single/test10000.txt'
    GV.ReceiveStandardDataList=copy.deepcopy(ODS.OriginDataStatistics(OriginDataPath))
    #print(GV.ReceiveStandardDataList)
    IFRRD.InitFinalResultRegisterDict()
    #print(GV.FinalResultRegisterDict)
    #插入公司映射记录···
    CompanyName=('广发银行信用卡')
    OCC.InsertCooperationCompanyRegister(MysqlObject,CompanyName)
    CompanyName1=('PPmoney')
    OCC.InsertCooperationCompanyRegister(MysqlObject,CompanyName1)

    BatchTuple=('广发银行信用卡','2018-08-27 08:23:45')
    ODEB.InsertBatchRegister(MysqlObject,BatchTuple)
    OTC.InsertTagClassifyRegister(MysqlObject)
    FTCM.FillTagClassifyMap(MysqlObject)
    OCV.InsertClassifyValueRegister(MysqlObject)
    FCVM.FillClassifyValueMap(MysqlObject)
    FDEB.FillDataExtractBatch(MysqlObject,'广发银行信用卡','2018-08-27 08:23:45')
    #print(GV.FinalResultRegisterDict)
    IRPN.InsertResultPersonNumber(MysqlObject)
    EPTI.ExtractPublicTaskInfo(MysqlObject)
    print(GV.ExtractPublicTaskInfoDict)

#自动化运行实现不够完全···0831
def main0831():
    MysqlObject=MSQLO.Mysql('192.168.7.31',3306,'ngoss_dim','ngoss_dim')
    #MysqlObject = MSQLO.Mysql('127.0.0.1', 3306, 'root', 'mysql')
    # print(MysqlObject._UseDatabase)
    #OriginDataPath = r'./QJC_Single/test10000.txt'
    GV.ReceiveStandardDataList = copy.deepcopy(QJCM.QJC0831_Main())
    #print('done!')
    # print(GV.ReceiveStandardDataList)
    if GV.ReceiveStandardDataList:
        for SingleReceiveStandardDataList in GV.ReceiveStandardDataList:
            IFRRD.InitFinalResultRegisterDict(GV.ReceiveStandardDataList[SingleReceiveStandardDataList])
            EPTI.ExtractPublicTaskInfo(MysqlObject)
            print(GV.ExtractPublicTaskInfoDict)
            # print(GV.FinalResultRegisterDict)

            CompanyName = ('广发银行信用卡')
            OCC.InsertCooperationCompanyRegister(MysqlObject, CompanyName)
            # CompanyName1 = ('PPmoney')
            # OCC.InsertCooperationCompanyRegister(MysqlObject, CompanyName1)

            BatchTuple = ('广发银行信用卡', '2018-08-27 08:23:45')
            ODEB.InsertBatchRegister(MysqlObject, BatchTuple)
            OTC.InsertTagClassifyRegister(MysqlObject)
            FTCM.FillTagClassifyMap(MysqlObject)
            OCV.InsertClassifyValueRegister(MysqlObject)
            FCVM.FillClassifyValueMap(MysqlObject)
            FDEB.FillDataExtractBatch(MysqlObject, '广发银行信用卡', '2018-08-27 08:23:45')
            # print(GV.FinalResultRegisterDict)
            IRPN.InsertResultPersonNumber(MysqlObject)
    else:
        print('没有新的数据统计分析任务···')

#实现自动化，但未优化···
def main0831_2():
    MysqlObject=MSQLO.Mysql('192.168.7.31',3306,'ngoss_dim','ngoss_dim')
    #MysqlObject = MSQLO.Mysql('127.0.0.1', 3306, 'root', 'mysql')
    # print(MysqlObject._UseDatabase)
    #OriginDataPath = r'./QJC_Single/test10000.txt'

    # print(GV.ReceiveStandardDataList)
    EPTI.ExtractPublicTaskInfo(MysqlObject)
    if len(GV.ExtractPublicTaskInfoDict['ExtractTaskID'])!=0:
        GV.ReceiveStandardDataDict = copy.deepcopy(QJCM.QJC0831_Main())
        #for TaskID in GV.ReceiveStandardDataList[ExtractTaskID]:
        if GV.ReceiveStandardDataDict:
            for SingleReceiveStandardDataListFileName in GV.ReceiveStandardDataDict:
                EBGO.InitEachBatchGlobalVariable()
                IFRRD.InitFinalResultRegisterDict(GV.ReceiveStandardDataDict[SingleReceiveStandardDataListFileName])
                #print(GV.ExtractPublicTaskInfoDict)
                # print(GV.FinalResultRegisterDict)
                for ExtractTaskID in GV.ExtractPublicTaskInfoDict['ExtractTaskID']:
                    if GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['filename'].strip('.txt')==SingleReceiveStandardDataListFileName:
                        # 插入公司映射记录···
                        #CompanyName = ('广发银行信用卡')
                        CompanyName=(GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['labelname'])
                        OCC.InsertCooperationCompanyRegister(MysqlObject, CompanyName)
                        # CompanyName1 = ('PPmoney')
                        # OCC.InsertCooperationCompanyRegister(MysqlObject, CompanyName1)
                        #BatchTuple = ('广发银行信用卡', '2018-08-27 08:23:45')
                        BatchTuple=(GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['labelname'],GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['createtime'])
                        ODEB.InsertBatchRegister(MysqlObject, BatchTuple)
                        OTC.InsertTagClassifyRegister(MysqlObject)
                        FTCM.FillTagClassifyMap(MysqlObject)
                        OCV.InsertClassifyValueRegister(MysqlObject)
                        FCVM.FillClassifyValueMap(MysqlObject)
                        #FDEB.FillDataExtractBatch(MysqlObject, '广发银行信用卡', '2018-08-27 08:23:45')
                        FDEB.FillDataExtractBatch(MysqlObject, BatchTuple[0], BatchTuple[1])
                        # print(GV.FinalResultRegisterDict)
                        IRPN.InsertResultPersonNumber(MysqlObject)
        else:
            print('没有新的数据统计分析任务···')

#0905(可自动化运行，但有待同事协调运行)···
def main():
    print ('Start Program:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #while True:
        #MysqlObject=MSQLO.Mysql('192.168.7.31',3306,'ngoss_dim','ngoss_dim') #测试服务器··
        #MysqlObject = MSQLO.Mysql('127.0.0.1', 3306, 'root', 'mysql')        #本地服务器··
    MysqlObject = MSQLO.Mysql('192.168.8.162', 3306, 'ngoss_dim', 'ngoss_dim')#生产线服务器··
    # print(MysqlObject._UseDatabase)
    #OriginDataPath = r'./QJC_Single/test10000.txt'
    EPTI.ExtractPublicTaskInfo(MysqlObject)
    if len(GV.ExtractPublicTaskInfoDict['ExtractTaskID'])!=0:
        #print(GV.ExtractPublicTaskInfoDict['ExtractTaskID'])
        EBGO.EachBatchGroupOperation(MysqlObject)
        ULGP.UpdateLabelGroupPersonas(MysqlObject)
    MysqlObject.DatabaseClose()

        #time.sleep(1)
        #print("等待中···!")

if __name__ == '__main__':
    main()
    gc.collect()
    #print(GV.FinalResultRegisterDict)
    print("over program!")
