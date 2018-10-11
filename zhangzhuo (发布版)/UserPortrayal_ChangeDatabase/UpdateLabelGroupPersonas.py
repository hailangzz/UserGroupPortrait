
import GlobalVariable as GV

def InitExtractPublicTaskInfo():
    GV.ExtractPublicTaskInfoDict={'ExtractTaskID':{}}
    GV.ExtractTaskInfo={'labelname':'' ,'filename':'', 'status':'' ,'createtime':'' ,'endtime':''}

def UpdateLabelGroupPersonas(MysqlObject):
    try:
        for ExtractTaskID in GV.ExtractPublicTaskInfoDict['ExtractTaskID']:
            if GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['status']==5:
                MysqlCommand = "update %s.label_group_personas set  status=%d,endtime='%s' where filename='%s';" % (MysqlObject._UseDatabase,GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['status'],
                                                                                                                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['endtime'],
                                                                                                                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['filename']
                                                                                                                )

                MysqlObject._MysqlCursor.execute(MysqlCommand)
                MysqlObject._MysqlDatabase.commit()
        InitExtractPublicTaskInfo()
    except Exception as result:
        print("更新公用数据查询批次表信息失败！ %s" % result)