# 说明：操作完成后，更新公用数据查询批次表的状态码信息····
import GlobalVariable as GV

def InitExtractPublicTaskInfo():
    GV.ExtractPublicTaskInfoDict={'ExtractTaskID':{}}
    GV.ExtractTaskInfo={'labelname':'' ,'filename':'', 'status':'' ,'createtime':'' ,'endtime':''}

def UpdateLabelGroupPersonas(MysqlObject):
    try:
        for ExtractTaskID in GV.ExtractPublicTaskInfoDict['ExtractTaskID']:
            #print(GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['createtime'])
            MysqlCommand = "update %s.label_group_personas set  status=%d,endtime='%s' where filename='%s';" % (MysqlObject._UseDatabase,GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['status'],
                                                                                                            GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['endtime'],
                                                                                                            GV.ExtractPublicTaskInfoDict['ExtractTaskID'][ExtractTaskID]['filename']
                                                                                                            )
            #print(MysqlCommand)
            MysqlObject._MysqlCursor.execute(MysqlCommand)
            MysqlObject._MysqlDatabase.commit()
        #将数据提取批次任务列表初始化归零···
        InitExtractPublicTaskInfo()
    except Exception as result:
        print("更新公用数据查询批次表信息失败！ %s" % result)