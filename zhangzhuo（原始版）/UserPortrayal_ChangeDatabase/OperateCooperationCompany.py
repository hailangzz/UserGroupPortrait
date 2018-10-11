import copy
#说明：操作公司信息映射表的模块
def GetExistCooperationCompanyInfoDict(MysqlObject):
    CompanyInfoDict={}
    MysqlCommand = "select CompanyName,CompanyMap from %s.UserPortrait_CooperationCompany;" % MysqlObject._UseDatabase
    MysqlObject._MysqlCursor.execute(MysqlCommand)
    CompanyRegisterTupleList = MysqlObject._MysqlCursor.fetchall()
    for RegisterTuple in CompanyRegisterTupleList:
        if RegisterTuple[0] not in CompanyInfoDict:
            CompanyInfoDict[RegisterTuple[0]]=RegisterTuple[1]

    return CompanyInfoDict

# 0826修改公司映射表结构前···
def InsertCooperationCompanyRegister1(MysqlObject,CompanyTuple):
    try:
        CompanyInfoDict=copy.deepcopy(GetExistCooperationCompanyInfoDict(MysqlObject))
        CompanyMapList=[]
        for CompanyName in CompanyInfoDict:
            CompanyMapList.append(int(CompanyInfoDict[CompanyName]))

        #print(CompanyInfoDict,CompanyMapList)
        if CompanyTuple[0] not in CompanyInfoDict and CompanyTuple[1] not in CompanyMapList:
            MysqlCommand = "insert into %s.UserPortrait_CooperationCompany (CompanyName,CompanyMap) Values('%s','%s')" % (MysqlObject._UseDatabase, CompanyTuple[0], CompanyTuple[1])
            # print(MysqlCommand)
            MysqlObject._MysqlCursor.execute(MysqlCommand)
            MysqlObject._MysqlDatabase.commit()
    except Exception as result:
        print("插入公司名称记录失败！ %s" % result)

def InsertCooperationCompanyRegister(MysqlObject,CompanyName):
    try:
        CompanyInfoDict=copy.deepcopy(GetExistCooperationCompanyInfoDict(MysqlObject))
        CompanyMapList=[]
        for ExistCompanyName in CompanyInfoDict:
            CompanyMapList.append(int(CompanyInfoDict[ExistCompanyName]))

        if CompanyName not in CompanyInfoDict.keys() :
            MysqlCommand = "insert into %s.UserPortrait_CooperationCompany (CompanyName) Values('%s')" % (MysqlObject._UseDatabase, CompanyName)
            MysqlObject._MysqlCursor.execute(MysqlCommand)
            MysqlObject._MysqlDatabase.commit()
    except Exception as result:
        print("插入公司名称记录失败！ %s" % result)
