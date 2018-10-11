import GlobalVariable as GV
import OperateTagClassify as OTC

def FillTagClassifyMap(MysqlObject):
    ExistTagClassifyInfoDict=OTC.GetExistTagClassifyInfoDict(MysqlObject)
    for FirstFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"]:
        # 似乎没必要做区分···
        if FirstFloorKey =='MainClass':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']=ExistTagClassifyInfoDict[GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyName']]
        elif FirstFloorKey =='MainClassTotal':
            for SecondFloorKey in GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey]:
                GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyMap']=ExistTagClassifyInfoDict[GV.FinalResultRegisterDict["ResultRegisterDict"][FirstFloorKey][SecondFloorKey]['TagClassifyName']]