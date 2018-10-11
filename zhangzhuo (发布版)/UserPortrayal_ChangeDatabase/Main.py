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
import copy
import gc
import EachBatchGroupOperation as EBGO
import UpdateLabelGroupPersonas as ULGP
import time

def main():
    print ('Start Program:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    MysqlObject = MSQLO.Mysql('192.168.8.162', 3306, 'ngoss_dim', 'ngoss_dim')#生产线服务器··
    EPTI.ExtractPublicTaskInfo(MysqlObject)
    if len(GV.ExtractPublicTaskInfoDict['ExtractTaskID'])!=0:
        EBGO.EachBatchGroupOperation(MysqlObject)
        ULGP.UpdateLabelGroupPersonas(MysqlObject)
    MysqlObject.DatabaseClose()

if __name__ == '__main__':
    main()
    gc.collect()
    print("over program!")
