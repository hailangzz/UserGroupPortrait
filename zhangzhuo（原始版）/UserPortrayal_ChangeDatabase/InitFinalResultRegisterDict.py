import GlobalVariable as GV
import copy
# 说明：用于初始化，最终的覆盖人数记录插入，所需要的存储数据结果：

def InitFinalResultRegisterDict0831(): # 适合原始的一个批次一次只有，单个数据文件要求的状况···
    if len(GV.ReceiveStandardDataList)==0:
        print("标准化结果数据列表为空")
        return
    else:
        for ReceiveStandardData in GV.ReceiveStandardDataList:
            for FirstFloorKey in ReceiveStandardData.keys():
                if FirstFloorKey=='MainClass':
                    for SecondFloorKey in ReceiveStandardData[FirstFloorKey].keys():
                        if SecondFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass']:
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]=copy.deepcopy(GV.ClassifyMapDict)
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["TagClassifyName"]=SecondFloorKey.split('_')[0]
                        for ThirdlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey].keys():
                            if ThirdlyFloorKey=='ClassifyValue':
                                if ThirdlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"]:
                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]={}
                                for FourthlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey].keys():
                                    if FourthlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                                        PersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey]
                                        GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]={"ClassifyValueMap":'',"PersonNumber":PersonNumber}

                            elif ThirdlyFloorKey=='ChildClass':
                                if ThirdlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"]:
                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]={}
                                for FourthlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey].keys():
                                    if FourthlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                                        GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]={}
                                    for FifthFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey]:
                                        if FifthFloorKey == 'ClassifyValue':
                                            if FifthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                                GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]={}
                                            for SixthFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                                if SixthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                                    PersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]
                                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]={"ClassifyValueMap":'',"PersonNumber":PersonNumber}
                                        elif FifthFloorKey == 'ChildClassTotal':
                                            if FifthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                                ChildClassTotalPersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]
                                                GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey] = {"ClassifyValueMap": '', "PersonNumber": ChildClassTotalPersonNumber}
                                                #GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]={"ChildClassTotalName":FourthlyFloorKey+'汇总',"ClassifyValueMap":'',"PersonNumber":ChildClassTotalPersonNumber}


                elif FirstFloorKey=='MainClassTotal':
                    for SecondFloorKey in ReceiveStandardData[FirstFloorKey].keys():
                        if SecondFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal']:
                            #print(SecondFloorKey)
                            OriginSecondFloorKey=SecondFloorKey
                            SecondFloorKey=SecondFloorKey+'_Total_Equal'
                            #print(SecondFloorKey)
                            PersonNumber=ReceiveStandardData[FirstFloorKey][OriginSecondFloorKey]
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]=copy.deepcopy(GV.ClassifyMapDict)
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]['TagClassifyName']=SecondFloorKey.split('_')[0]
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]['ClassifyValueDict'] = {"主标签汇总值":{"ClassifyValueMap":'',"PersonNumber":PersonNumber}}


def InitFinalResultRegisterDict(SingleReceiveStandardDataList): # 适合原始的一个批次一次中，有多个数据文件要求的状况···
    if len(SingleReceiveStandardDataList)==0:
        print("标准化结果数据列表为空")
        return
    else:
        # print(type(SingleReceiveStandardDataList))
        # print(SingleReceiveStandardDataList)
        # for ReceiveStandardData in SingleReceiveStandardDataList:
        #     print(ReceiveStandardData)
        for ReceiveStandardData in SingleReceiveStandardDataList:
            for FirstFloorKey in ReceiveStandardData.keys():
                if FirstFloorKey=='MainClass':
                    for SecondFloorKey in ReceiveStandardData[FirstFloorKey].keys():
                        if SecondFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass']:
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]=copy.deepcopy(GV.ClassifyMapDict)
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["TagClassifyName"]=SecondFloorKey.split('_')[0]
                        for ThirdlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey].keys():
                            if ThirdlyFloorKey=='ClassifyValue':
                                if ThirdlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"]:
                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]={}
                                for FourthlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey].keys():
                                    if FourthlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                                        PersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey]
                                        GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]={"ClassifyValueMap":'',"PersonNumber":PersonNumber}

                            elif ThirdlyFloorKey=='ChildClass':
                                if ThirdlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"]:
                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]={}
                                for FourthlyFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey].keys():
                                    if FourthlyFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey]:
                                        GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]={}
                                    for FifthFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey]:
                                        if FifthFloorKey == 'ClassifyValue':
                                            if FifthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                                GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]={}
                                            for SixthFloorKey in ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                                if SixthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                                    PersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]
                                                    GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]={"ClassifyValueMap":'',"PersonNumber":PersonNumber}
                                        elif FifthFloorKey == 'ChildClassTotal':
                                            if FifthFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey]:
                                                ChildClassTotalPersonNumber=ReceiveStandardData[FirstFloorKey][SecondFloorKey][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]
                                                GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey] = {"ClassifyValueMap": '', "PersonNumber": ChildClassTotalPersonNumber}
                                                #GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]={"ChildClassTotalName":FourthlyFloorKey+'汇总',"ClassifyValueMap":'',"PersonNumber":ChildClassTotalPersonNumber}


                elif FirstFloorKey=='MainClassTotal':
                    for SecondFloorKey in ReceiveStandardData[FirstFloorKey].keys():
                        if SecondFloorKey not in GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal']:
                            #print(SecondFloorKey)
                            OriginSecondFloorKey=SecondFloorKey
                            SecondFloorKey=SecondFloorKey+'_Total_Equal'
                            #print(SecondFloorKey)
                            PersonNumber=ReceiveStandardData[FirstFloorKey][OriginSecondFloorKey]
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]=copy.deepcopy(GV.ClassifyMapDict)
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]['TagClassifyName']=SecondFloorKey.split('_')[0]
                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClassTotal'][SecondFloorKey]['ClassifyValueDict'] = {"主标签汇总值":{"ClassifyValueMap":'',"PersonNumber":PersonNumber}}