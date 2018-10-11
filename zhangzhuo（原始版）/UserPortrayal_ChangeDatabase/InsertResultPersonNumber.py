# 说明 ： 最终插入结果人数覆盖记录···
import GlobalVariable as GV
import copy

def GetResultBatchAndValueMap(MysqlObject):
    BatchAndValueMapList=[]
    BatchAndValueMap=['BatchMap','ClassifyValueMap']
    MysqlCommand = "select BatchMap,ClassifyValueMap from %s.UserPortrait_ResultPersonNumber;" % MysqlObject._UseDatabase
    #print(MysqlObject._MysqlHost)
    #print(MysqlCommand)
    MysqlObject._MysqlCursor.execute(MysqlCommand)
    BatchAndValueMapTupleList = copy.deepcopy(MysqlObject._MysqlCursor.fetchall())
    #print(BatchAndValueMapTupleList)
    if BatchAndValueMapTupleList:
        for BatchAndValueMapTuple in BatchAndValueMapTupleList:
            #if BatchAndValueMapTuple[1]:
                #print('GetResultBatchAndValueMap',BatchAndValueMapTuple[1])
            BatchAndValueMap[0]=BatchAndValueMapTuple[0]
            BatchAndValueMap[1] = BatchAndValueMapTuple[1]
            BatchAndValueMapList.append(copy.deepcopy(BatchAndValueMap))
    return BatchAndValueMapList

def InsertResultPersonNumber1(MysqlObject):
    ExistBatchAndValueMapList=GetResultBatchAndValueMap(MysqlObject)
    InsertBatchAndValueMap=['BatchMap','ClassifyValueMap']
    InsertBatchAndValueMap[0]=GV.FinalResultRegisterDict['BatchMap']
    for FirstFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"]:
        if FirstFloorKey=='MainClassTotal':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                InsertBatchAndValueMap[1]=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict']['主标签汇总值']["ClassifyValueMap"]
                if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                    # 此时插入结果覆盖人数记录···
                    TotalPopulation=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict']['主标签汇总值']["PersonNumber"]
                    InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                                 "values (%d,%d,%d);" % (
                                                 MysqlObject._UseDatabase,
                                                 InsertBatchAndValueMap[0],
                                                 InsertBatchAndValueMap[1],
                                                 TotalPopulation)
                    MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
                    MysqlObject._MysqlDatabase.commit()

        elif FirstFloorKey=='MainClass':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                for ThirdlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"]:
                    if ThirdlyFloorKey=='ClassifyValue':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                            InsertBatchAndValueMap[1] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]['ClassifyValueMap']
                            if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]['PersonNumber']
                                InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                                             "values (%d,%d,%d);" % (
                                                                 MysqlObject._UseDatabase,
                                                                 InsertBatchAndValueMap[0],
                                                                 InsertBatchAndValueMap[1],
                                                                 TotalPopulation)
                                MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
                                MysqlObject._MysqlDatabase.commit()

                    elif ThirdlyFloorKey=='ChildClass':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                            for FifthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                if FifthFloorKey=='ChildClassTotal':
                                    InsertBatchAndValueMap[1] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]['ClassifyValueMap']
                                    if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                        TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]['PersonNumber']
                                        InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                                                     "values (%d,%d,%d);" % (
                                                                         MysqlObject._UseDatabase,
                                                                         InsertBatchAndValueMap[0],
                                                                         InsertBatchAndValueMap[1],
                                                                         TotalPopulation)
                                        MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
                                        MysqlObject._MysqlDatabase.commit()
                                elif FifthFloorKey == 'ClassifyValue':
                                    for SixthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                        InsertBatchAndValueMap[1]=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]['ClassifyValueMap']
                                        if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                            TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]['PersonNumber']
                                            InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                                                         "values (%d,%d,%d);" % (
                                                                             MysqlObject._UseDatabase,
                                                                             InsertBatchAndValueMap[0],
                                                                             InsertBatchAndValueMap[1],
                                                                             TotalPopulation)
                                            MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
                                            MysqlObject._MysqlDatabase.commit()

def InsertResultPersonNumber(MysqlObject):
    ExistBatchAndValueMapList=GetResultBatchAndValueMap(MysqlObject)
    #print(ExistBatchAndValueMapList)
    InsertResultRegisterDict={'InsertBatchAndValueMapList':[],'TotalPopulationList':[]}
    InsertBatchAndValueMap=['BatchMap','ClassifyValueMap']
    InsertBatchAndValueMap[0]=GV.FinalResultRegisterDict['BatchMap']
    for FirstFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"]:
        if FirstFloorKey=='MainClassTotal':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                InsertBatchAndValueMap[1]=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict']['主标签汇总值']["ClassifyValueMap"]
                # if not InsertBatchAndValueMap[1]:
                #     print(InsertBatchAndValueMap[1])
                if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                    # 此时插入结果覆盖人数记录···
                    TotalPopulation=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict']['主标签汇总值']["PersonNumber"]
                    InsertResultRegisterDict['InsertBatchAndValueMapList'].append(copy.deepcopy(InsertBatchAndValueMap))
                    InsertResultRegisterDict['TotalPopulationList'].append(TotalPopulation)

        elif FirstFloorKey=='MainClass':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                for ThirdlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"]:
                    if ThirdlyFloorKey=='ClassifyValue':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                            InsertBatchAndValueMap[1] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]['ClassifyValueMap']

                            if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]['PersonNumber']
                                InsertResultRegisterDict['InsertBatchAndValueMapList'].append(copy.deepcopy(InsertBatchAndValueMap))
                                InsertResultRegisterDict['TotalPopulationList'].append(TotalPopulation)

                    elif ThirdlyFloorKey=='ChildClass':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                            for FifthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                if FifthFloorKey=='ChildClassTotal':
                                    InsertBatchAndValueMap[1] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]['ClassifyValueMap']

                                    if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                        TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]['PersonNumber']
                                        InsertResultRegisterDict['InsertBatchAndValueMapList'].append(copy.deepcopy(InsertBatchAndValueMap))
                                        InsertResultRegisterDict['TotalPopulationList'].append(TotalPopulation)

                                elif FifthFloorKey == 'ClassifyValue':
                                    for SixthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                        InsertBatchAndValueMap[1]=GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]['ClassifyValueMap']
                                        if InsertBatchAndValueMap not in ExistBatchAndValueMapList:
                                            TotalPopulation =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]['PersonNumber']
                                            InsertResultRegisterDict['InsertBatchAndValueMapList'].append(copy.deepcopy(InsertBatchAndValueMap))
                                            InsertResultRegisterDict['TotalPopulationList'].append(TotalPopulation)

    GV.InsertResultRegisterDict=copy.deepcopy(InsertResultRegisterDict)
    #print(GV.InsertResultRegisterDict)
    # for BatchAndValueMap in GV.InsertResultRegisterDict['InsertBatchAndValueMapList']:
    #     if not BatchAndValueMap[1]:
    #         print(BatchAndValueMap)


    InsertResultRegisterAction(MysqlObject)

def InsertResultRegisterAction(MysqlObject):
    try:
        InsertAllResultRegisterString=[]
        for InsertResultRegisterIndex in range(len(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'])):
            if GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][1]: #无种类值映射的脏数据不插入···
                InsertSingleResultRegisterString = '('
                InsertSingleResultRegisterString+=str(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][0])+','+str(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][1])+','+str(GV.InsertResultRegisterDict['TotalPopulationList'][InsertResultRegisterIndex])+')'
                InsertAllResultRegisterString.append(InsertSingleResultRegisterString)
                #print(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex])
                #print(InsertSingleResultRegisterString)
                # if InsertResultRegisterIndex<len(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'])-1:
                #     InsertAllResultRegisterString+=InsertSingleResultRegisterString+','
                # else:
                #     InsertAllResultRegisterString += InsertSingleResultRegisterString
            #print(InsertAllResultRegisterString)
        for SingleResultRegisterString in InsertAllResultRegisterString:

            InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                         "values %s;" % (
                                             MysqlObject._UseDatabase,SingleResultRegisterString)
            #print(InsertClassifyValueCommand)
            MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
            MysqlObject._MysqlDatabase.commit()
    except Exception as result:
        print(" InsertResultRegisterAction 覆盖人数结果表插入错误！ %s" % result)

def InsertResultRegisterAction1(MysqlObject):
    try:
        InsertAllResultRegisterString=''
        for InsertResultRegisterIndex in range(len(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'])):

            if GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][1]: #无种类值映射的脏数据不插入···
                InsertSingleResultRegisterString = '('
                InsertSingleResultRegisterString+=str(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][0])+','+str(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex][1])+','+str(GV.InsertResultRegisterDict['TotalPopulationList'][InsertResultRegisterIndex])+')'
                InsertAllResultRegisterString+=InsertSingleResultRegisterString
            #print(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'][InsertResultRegisterIndex])
            #print(InsertSingleResultRegisterString)
            # if InsertResultRegisterIndex<len(GV.InsertResultRegisterDict['InsertBatchAndValueMapList'])-1:
            #     InsertAllResultRegisterString+=InsertSingleResultRegisterString+','
            # else:
            #     InsertAllResultRegisterString += InsertSingleResultRegisterString
        #print(InsertAllResultRegisterString)

        InsertClassifyValueCommand = "insert into %s.UserPortrait_ResultPersonNumber (BatchMap,ClassifyValueMap,TotalPopulation)  " \
                                     "values %s;" % (
                                         MysqlObject._UseDatabase,InsertAllResultRegisterString)
        #print(InsertClassifyValueCommand)
        MysqlObject._MysqlCursor.execute(InsertClassifyValueCommand)
        MysqlObject._MysqlDatabase.commit()
    except Exception as result:
        print(" InsertResultRegisterAction 覆盖人数结果表插入错误！ %s" % result)


