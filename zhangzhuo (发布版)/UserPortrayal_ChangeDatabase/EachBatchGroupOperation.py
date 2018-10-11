# 说明：将每一个批次的所有插入操作集合到一个函数中进行···
import GlobalVariable as GV
import MySQLOperation as MSQLO
import OperateClassifyValue as OCV
import OperateCooperationCompany as OCC
import OperateDataExtractBatch as ODEB
import OperateTagClassify as OTC

import QJC0831.QJCMain as QJCM
import InitFinalResultRegisterDict as IFRRD
import FillTagClassifyMap as FTCM
import FillClassifyValueMap as FCVM
import FillDataExtractBatch as FDEB
import InsertResultPersonNumber as IRPN
import ExtractPublicTaskInfo as EPTI
import EachBatchGroupOperation as EBGO
import copy
import datetime

def InitEachBatchGlobalVariable():
    GV.FinalResultRegisterDict = {"CompanyName": '', "BatchDate": '', "BatchMap": '',"ResultRegisterDict": {"MainClass": {}, "MainClassTotal": {}}}
    GV.ClassifyMapDict = {"TagClassifyName": '', "TagClassifyMap": 0, "ClassifyValueDict": {}}
    GV.InsertResultRegisterDict = {'InsertBatchAndValueMapList': [], 'TotalPopulationList': []}

def EachBatchGroupOperation(MysqlObject):
    print('start analysis of data!')
    GV.ReceiveStandardDataDict = copy.deepcopy(QJCM.QJC0831_Main())
    print('analysis data wating for insert database !')
    if GV.ReceiveStandardDataDict:
        for SingleReceiveStandardDataListFileName in GV.ReceiveStandardDataDict:
            EBGO.InitEachBatchGlobalVariable()
            IFRRD.InitFinalResultRegisterDict(GV.ReceiveStandardDataDict[SingleReceiveStandardDataListFileName])

            for ExtractTaskID in GV.ExtractPublicTaskInfoDict['ExtractTaskID']:
                SingleReceiveStandardDataListFileName=SingleReceiveStandardDataListFileName.split('/')[-1]
                if GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['filename'].strip('.txt') == SingleReceiveStandardDataListFileName:
                    CompanyName = (GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['labelname'])
                    BatchTuple = (GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['labelname'],
                                  GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['createtime'])
                    OCC.InsertCooperationCompanyRegister(MysqlObject, CompanyName)
                    ODEB.InsertBatchRegister(MysqlObject, BatchTuple)
                    OTC.InsertTagClassifyRegister(MysqlObject)
                    FTCM.FillTagClassifyMap(MysqlObject)
                    OCV.InsertClassifyValueRegister(MysqlObject)
                    FCVM.FillClassifyValueMap(MysqlObject)
                    FDEB.FillDataExtractBatch(MysqlObject, BatchTuple[0], BatchTuple[1])
                    IRPN.InsertResultPersonNumber(MysqlObject)
                    GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['status']=5
                    Today=datetime.datetime.now()
                    GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['endtime'] = datetime.datetime.strftime(Today, '%Y-%m-%d %H:%M:%S')

    else:
        print('没有新的数据统计分析任务···')


