import GlobalVariable as GV
import OperateClassifyValue as OCV
import copy

def FillClassifyValueMap(MysqlObject):
    ExistClassifyValueInfoDict = copy.deepcopy(OCV.GetExistClassifyValueInfoDict(MysqlObject))
    #ExistClassifyValueInfoList = []
    #for ExistClassifyValueMap in ExistClassifyValueInfoDict:
        #ExistClassifyValueInfoList.append(ExistClassifyValueInfoDict[ExistClassifyValueMap])

    ResultRegisterClassifyValueList = ['TagClassifyMap', 'ClassifyValue', 'FatherTagName']
    for FirstFloorKey in  GV.FinalResultRegisterDict["ResultRegisterDict"]:
        if FirstFloorKey=='MainClassTotal':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey].keys():
                ResultRegisterClassifyValueList[0] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']
                ResultRegisterClassifyValueList[1] ='主标签汇总值'
                ResultRegisterClassifyValueList[2] =GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyName']
                for ExistClassifyValueMap in ExistClassifyValueInfoDict:
                    if ExistClassifyValueInfoDict[ExistClassifyValueMap]==ResultRegisterClassifyValueList:
                        GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict']["主标签汇总值"]["ClassifyValueMap"]=ExistClassifyValueMap
        elif FirstFloorKey=='MainClass':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey].keys():
                for ThirdlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'].keys():
                    if ThirdlyFloorKey == 'ClassifyValue':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'][ThirdlyFloorKey].keys():
                            ResultRegisterClassifyValueList[0] = GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']
                            ResultRegisterClassifyValueList[1] = FourthlyFloorKey
                            ResultRegisterClassifyValueList[2] = GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyName']
                            for ExistClassifyValueMap in ExistClassifyValueInfoDict:
                                if ExistClassifyValueInfoDict[ExistClassifyValueMap] == ResultRegisterClassifyValueList:
                                    GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'][ThirdlyFloorKey][FourthlyFloorKey]["ClassifyValueMap"] = ExistClassifyValueMap

                    elif ThirdlyFloorKey == 'ChildClass':
                        for FourthlyFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'][ThirdlyFloorKey].keys():
                            for FifthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'][ThirdlyFloorKey][FourthlyFloorKey].keys():
                                if FifthFloorKey=='ChildClassTotal':
                                    ResultRegisterClassifyValueList[0] = GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']
                                    ResultRegisterClassifyValueList[1] = FourthlyFloorKey
                                    ResultRegisterClassifyValueList[2] = GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyName']
                                    for ExistClassifyValueMap in ExistClassifyValueInfoDict:
                                        if ExistClassifyValueInfoDict[ExistClassifyValueMap] == ResultRegisterClassifyValueList:
                                            GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]['ClassifyValueMap']=ExistClassifyValueMap
                                elif FifthFloorKey=='ClassifyValue':
                                    for SixthFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['ClassifyValueDict'][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey]:
                                        ResultRegisterClassifyValueList[0] = GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']
                                        ResultRegisterClassifyValueList[1] = SixthFloorKey
                                        ResultRegisterClassifyValueList[2] = FourthlyFloorKey
                                        for ExistClassifyValueMap in ExistClassifyValueInfoDict:
                                            if ExistClassifyValueInfoDict[ExistClassifyValueMap] == ResultRegisterClassifyValueList:
                                                GV.FinalResultRegisterDict["ResultRegisterDict"]['MainClass'][SecondFloorKey]["ClassifyValueDict"][ThirdlyFloorKey][FourthlyFloorKey][FifthFloorKey][SixthFloorKey]['ClassifyValueMap']=ExistClassifyValueMap







