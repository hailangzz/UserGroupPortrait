import GlobalVariable as GV
import copy
# 说明:用来操作 TagClassify 标签种类表：

# 获得现有数据库中，标签种类的映射值···，并写入 GV.FinalResultRegisterDict 结构中去···
def GetExistTagClassifyInfoDict(MysqlObject):
    # 获取已经存在的 TagClassify 表记录信息
    try:
        ExistTagClassifyInfoDict={}  # 例如：ExistTagClassifyInfoDict{'性别':1}
        SelectTagClassifyCommand = "select TagClassifyName,TagClassifyMap  from %s.UserPortrait_TagClassify;" % (MysqlObject._UseDatabase)
        MysqlObject._MysqlCursor.execute(SelectTagClassifyCommand)
        ExistTagClassifyTupleList = MysqlObject._MysqlCursor.fetchall()
        if ExistTagClassifyTupleList:
            for ExistTagClassifyTuple in ExistTagClassifyTupleList:
                if ExistTagClassifyTuple[0] not in ExistTagClassifyInfoDict:
                    ExistTagClassifyInfoDict[ExistTagClassifyTuple[0]]=int(ExistTagClassifyTuple[1])
        return ExistTagClassifyInfoDict
    except Exception as result:
        print("获取 TagClassify 表记录错误！ %s" % result)

def InsertTagClassifyRegister(TagClassifyName,MysqlObject):
    try:
        # 自动拆分检索标签种类名称（查看是否包含子标签的Flag标志信息，并存储到TagClassifyDict数据结构中,保证记录插入的正确性···）
        TagClassifyDict = {"TagClassifyName": '', "TagClassifyFlag": '', "ClassifyValueAlgorithm": ''}
        TagClassifyCombo = TagClassifyName.split('_')
        if len(TagClassifyCombo) != 3:  # 检验标签类型名称，命名是否符合规范要求···
            print("标签种类命名不符合规范：（例如：\"华为_Phone_Equal\"）")
            return
        TagClassifyDict["TagClassifyName"] = TagClassifyCombo[0]
        TagClassifyDict["TagClassifyFlag"] = TagClassifyCombo[1]

        ExistTagClassifyInfoDict=copy.deepcopy(GetExistTagClassifyInfoDict(MysqlObject))
        if TagClassifyDict["TagClassifyName"] not in ExistTagClassifyInfoDict:
            if TagClassifyDict["TagClassifyFlag"] =='':     # 插入默认标签种类标志（MainClass）··
                InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName)  values ('%s');" % (MysqlObject._UseDatabase,TagClassifyDict["TagClassifyName"])
                MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                MysqlObject._MysqlDatabase.commit()
            else:
                InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName,TagClassifyFlag)  values ('%s','%s');" % (MysqlObject._UseDatabase,TagClassifyDict["TagClassifyName"],TagClassifyDict["TagClassifyFlag"])
                MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                MysqlObject._MysqlDatabase.commit()
        else:
            print("标签种类插入失败，标签种类重复···")

    except Exception as result:
        print("插入 TagClassify 表记录错误！ %s" % result)

def InsertTagClassifyRegister(MysqlObject):
    try:
        ExistTagClassifyInfoDict = copy.deepcopy(GetExistTagClassifyInfoDict(MysqlObject))
        #print(ExistTagClassifyInfoDict)
        for FirstFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"]:
            if FirstFloorKey == 'MainClassTotal':
                for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                    TagClassifyName=SecondFloorKey
                    # 自动拆分检索标签种类名称（查看是否包含子标签的Flag标志信息，并存储到TagClassifyDict数据结构中,保证记录插入的正确性···）
                    TagClassifyDict = {"TagClassifyName": '', "TagClassifyFlag": '', "ClassifyValueAlgorithm": ''}
                    TagClassifyCombo = TagClassifyName.split('_')
                    if len(TagClassifyCombo) != 3:  # 检验标签类型名称，命名是否符合规范要求···
                        print("标签种类命名不符合规范：（例如：\"华为_Phone_Equal\"）")
                        return
                    TagClassifyDict["TagClassifyName"] = TagClassifyCombo[0]
                    TagClassifyDict["TagClassifyFlag"] = TagClassifyCombo[1]


                    if TagClassifyDict["TagClassifyName"] not in ExistTagClassifyInfoDict:
                        if TagClassifyDict["TagClassifyFlag"] =='':     # 插入默认标签种类标志（MainClass）··
                            InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName)  values ('%s');" % (MysqlObject._UseDatabase,TagClassifyDict["TagClassifyName"])
                            MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                            MysqlObject._MysqlDatabase.commit()
                        else:
                            InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName,TagClassifyFlag)  values ('%s','%s');" % (MysqlObject._UseDatabase,TagClassifyDict["TagClassifyName"],TagClassifyDict["TagClassifyFlag"])
                            MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                            MysqlObject._MysqlDatabase.commit()
                    # else:
                    #     print("标签种类插入失败，标签种类重复···")

            elif FirstFloorKey == 'MainClass':
                for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                    TagClassifyName = SecondFloorKey
                    # 自动拆分检索标签种类名称（查看是否包含子标签的Flag标志信息，并存储到TagClassifyDict数据结构中,保证记录插入的正确性···）
                    TagClassifyDict = {"TagClassifyName": '', "TagClassifyFlag": '', "ClassifyValueAlgorithm": ''}
                    TagClassifyCombo = TagClassifyName.split('_')
                    if len(TagClassifyCombo) != 3:  # 检验标签类型名称，命名是否符合规范要求···
                        print("标签种类命名不符合规范：（例如：\"华为_Phone_Equal\"）")
                        return
                    TagClassifyDict["TagClassifyName"] = TagClassifyCombo[0]
                    TagClassifyDict["TagClassifyFlag"] = TagClassifyCombo[1]

                    if TagClassifyDict["TagClassifyName"] not in ExistTagClassifyInfoDict:
                        if TagClassifyDict["TagClassifyFlag"] == '':  # 插入默认标签种类标志（MainClass）··
                            InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName)  values ('%s');" % (
                            MysqlObject._UseDatabase, TagClassifyDict["TagClassifyName"])
                            MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                            MysqlObject._MysqlDatabase.commit()
                        else:
                            InsertTagClassifyCommand = "insert into %s.UserPortrait_TagClassify (TagClassifyName,TagClassifyFlag)  values ('%s','%s');" % (
                            MysqlObject._UseDatabase, TagClassifyDict["TagClassifyName"],
                            TagClassifyDict["TagClassifyFlag"])
                            MysqlObject._MysqlCursor.execute(InsertTagClassifyCommand)
                            MysqlObject._MysqlDatabase.commit()
                    # else:
                    #     print("标签种类插入失败，标签种类重复···")

    except Exception as result:
        print("插入 TagClassify 表记录错误！ %s" % result)


def GetExistTagClassifyInfoList(MysqlObject):
    # 获取已经存在的 TagClassify 表记录信息
    try:
        ExistTagClassifyInfoList=[]  # 例如：ExistTagClassifyInfoDict{'性别':1}
        ExistTagClassifyInfo=['TagClassifyName','TagClassifyMap']
        SelectTagClassifyCommand = "select TagClassifyName,TagClassifyMap  from %s.UserPortrait_TagClassify;" % (MysqlObject._UseDatabase)
        MysqlObject._MysqlCursor.execute(SelectTagClassifyCommand)
        ExistTagClassifyTupleList = MysqlObject._MysqlCursor.fetchall()
        if ExistTagClassifyTupleList:
            for ExistTagClassifyTuple in ExistTagClassifyTupleList:
                ExistTagClassifyInfo[0]=ExistTagClassifyTuple[0]
                ExistTagClassifyInfo[1] = ExistTagClassifyTuple[1]
        return ExistTagClassifyInfoList
    except Exception as result:
        print("获取 TagClassify 表记录错误！ %s" % result)
