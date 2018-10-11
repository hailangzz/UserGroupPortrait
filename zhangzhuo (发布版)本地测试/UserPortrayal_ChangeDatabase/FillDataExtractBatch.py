# 说明：填充数据提取批次的信息···
import OperateCooperationCompany as OCC
import OperateDataExtractBatch as ODEB
import GlobalVariable as GV
import copy

def FillDataExtractBatch(MysqlObject,CommpanyName,BatchDate):
    CompanyInfoDict=copy.deepcopy(OCC.GetExistCooperationCompanyInfoDict(MysqlObject))
    BatchInfoDict=copy.deepcopy(ODEB.GetExistBatchInfoDict(MysqlObject))

    CompanyMap=CompanyInfoDict[CommpanyName]
    BatchInfo=[CompanyMap,BatchDate]
    for BatchMap in BatchInfoDict:
        if BatchInfo==BatchInfoDict[BatchMap]:
            GV.FinalResultRegisterDict['CompanyName']=CommpanyName
            GV.FinalResultRegisterDict['BatchDate'] = BatchDate
            GV.FinalResultRegisterDict['BatchMap'] = BatchMap


