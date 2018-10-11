import copy
import OperateCooperationCompany as OCC
# 说明：操作批次信息表，插入或检索···

def GetExistBatchInfoDict(MysqlObject):
    BatchInfoDict={}
    MysqlCommand = "select BatchMap,CompanyMap,DATE_FORMAT(BatchDate,'%%Y-%%m-%%d %%H:%%i:%%S') from %s.UserPortrait_DataExtractBatch;" % MysqlObject._UseDatabase
    MysqlObject._MysqlCursor.execute(MysqlCommand)
    BatchRegisterTupleList = MysqlObject._MysqlCursor.fetchall()
    for BatchRegisterTuple in BatchRegisterTupleList:
        if BatchRegisterTuple[0] not in BatchInfoDict:
            BatchInfoDict[BatchRegisterTuple[0]]=[BatchRegisterTuple[1],BatchRegisterTuple[2]]

    return BatchInfoDict

def InsertBatchRegister(MysqlObject,BatchTuple):
    CompanyInfoDict=copy.deepcopy(OCC.GetExistCooperationCompanyInfoDict(MysqlObject))
    BatchInfoDict=copy.deepcopy(GetExistBatchInfoDict(MysqlObject))
    ExistBatchInfoList=[]
    for BatchMap in BatchInfoDict:
        ExistBatchInfoList.append(BatchInfoDict[BatchMap])
    InsertCompanyMap=CompanyInfoDict[BatchTuple[0]]
    InsertBatchInfo=[InsertCompanyMap,BatchTuple[1]]
    if InsertBatchInfo not in ExistBatchInfoList:
        MysqlCommand = "insert into %s.UserPortrait_DataExtractBatch (CompanyMap,BatchDate) Values('%s','%s')" % (MysqlObject._UseDatabase, InsertCompanyMap, BatchTuple[1])
        MysqlObject._MysqlCursor.execute(MysqlCommand)
        MysqlObject._MysqlDatabase.commit()

