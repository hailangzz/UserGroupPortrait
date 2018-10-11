import copy

def GetExistCooperationCompanyInfoDict(MysqlObject):
    CompanyInfoDict={}
    MysqlCommand = "select CompanyName,CompanyMap from %s.UserPortrait_CooperationCompany;" % MysqlObject._UseDatabase
    MysqlObject._MysqlCursor.execute(MysqlCommand)
    CompanyRegisterTupleList = MysqlObject._MysqlCursor.fetchall()
    for RegisterTuple in CompanyRegisterTupleList:
        if RegisterTuple[0] not in CompanyInfoDict:
            CompanyInfoDict[RegisterTuple[0]]=RegisterTuple[1]

    return CompanyInfoDict



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
