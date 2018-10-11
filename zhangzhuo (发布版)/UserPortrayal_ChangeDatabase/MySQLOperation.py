import pymysql
import datetime
#import GlobalVariable as GV
import copy

class Mysql:
    _MysqlHost = {"host": '', "port": 0, "user": '', "password": ''}
    _MysqlDatabase=''
    _MysqlCursor=''
    _UseDatabase=''

    def __init__(self, host, port, user, password,DatabaseName='label_support'):
        self._MysqlHost["host"]=host
        self._MysqlHost["port"]=port
        self._MysqlHost["user"]=user
        self._MysqlHost["password"]=password
        self._UseDatabase=DatabaseName.lower()
        self._TableList=['UserPortrait_CooperationCompany','UserPortrait_DataExtractBatch','UserPortrait_TagClassify','UserPortrait_ClassifyValue','UserPortrait_ResultPersonNumber']
        self.ConnectMysql()  # 先获取数据库连接
        #self.DropTables()
        self.CheckDatabase(self._UseDatabase)  #再检索创建数据库及数据表结构

    def CheckDatabase(self,DatabaseName='label_support'):
        DatabaseName = DatabaseName
        DatabaseTuple = ()
        DatabaseList = []
        MysqlCommand = "show databases;"
        self._MysqlCursor.execute(MysqlCommand)
        DatabaseTuple = self._MysqlCursor.fetchall()
        for TupleList in DatabaseTuple:
            DatabaseList.append(TupleList[0])
        if DatabaseName not in DatabaseList:
            self.CreateDatabase(DatabaseName)
        self.CheckUserTagTable(DatabaseName,self._TableList)

    def CreateDatabase(self,DatabaseName='label_support'):
        try:
            MysqlCommand="create database if not exists %s;" % DatabaseName
            self._MysqlCursor.execute(MysqlCommand)
        except Exception as result:
            print("新建数据库错误！ %s" % result)

    def CheckUserTagTable(self, DatabaseName="label_support",TableList=['UserPortrait_CooperationCompany','UserPortrait_DataExtractBatch','UserPortrait_TagClassify','UserPortrait_ClassifyValue','UserPortrait_ResultPersonNumber']):
        DatabaseExistTableTuple = ()
        DatabaseExistTableList = []
        MysqlCommand = "use %s;" % DatabaseName
        self._MysqlCursor.execute(MysqlCommand)
        MysqlCommand = "show tables;"
        self._MysqlCursor.execute(MysqlCommand)
        DatabaseExistTableTuple = self._MysqlCursor.fetchall()
        for TupleList in DatabaseExistTableTuple:
            DatabaseExistTableList.append(TupleList[0])
	    #DatabaseExistTableList.append(TupleList[0].lower())
        #print(DatabaseExistTableList)
        if 'UserPortrait_CooperationCompany' not in DatabaseExistTableList:
            self.CreateCooperationCompanyTable()
        if 'UserPortrait_DataExtractBatch' not in DatabaseExistTableList:
            self.CreateDataExtractBatchTable()
        if 'UserPortrait_TagClassify' not in DatabaseExistTableList:
            self.CreateTagClassifyTable()
        if 'UserPortrait_ClassifyValue' not in DatabaseExistTableList:
            self.CreateClassifyValueTable()
        if 'UserPortrait_ResultPersonNumber' not in DatabaseExistTableList:
            self.CreateResultPersonNumberTable()

    def CreateCooperationCompanyTable(self,DatabaseName="label_support"):
        try:
            MysqlCommand="use %s;" % DatabaseName
            #CreateCooperationCompany="create table if not exists CooperationCompany(ID int auto_increment unique comment '公司名称映射表索引',CompanyName Varchar(50)  not null unique comment '公司名称', CompanyMap  Char(20) comment '公司名称映射值',PRIMARY KEY(CompanyMap ));"
            #(0827 修改···)
            CreateCooperationCompany = "create table if not exists UserPortrait_CooperationCompany(CompanyName Varchar(50)  not null unique comment '公司名称', CompanyMap  int auto_increment comment '公司名称映射值',PRIMARY KEY(CompanyMap ));"
            self._MysqlCursor.execute(MysqlCommand)
            self._MysqlCursor.execute(CreateCooperationCompany)
        except Exception as result:
            print("新建 UserPortrait_CooperationCompany 数据表错误！ %s" % result)
    def CreateDataExtractBatchTable(self,DatabaseName="label_support"):
        try:
            MysqlCommand="use %s;" % DatabaseName
            #CreateDataExtractBatch="create table if not exists DataExtractBatch (CompanyMap  Char(20) not null comment '公司名称映射值', BatchDate datetime not null comment '数据提取日期', BatchMap int auto_increment comment '数据提取批次映射值',PRIMARY KEY(BatchMap),unique KEY complex_unique(CompanyMap  , BatchDate),FOREIGN KEY (CompanyMap) REFERENCES CooperationCompany (CompanyMap));"
            CreateDataExtractBatch = "create table if not exists UserPortrait_DataExtractBatch (CompanyMap  int not null comment '公司名称映射值', BatchDate datetime not null comment '数据提取日期', BatchMap int auto_increment comment '数据提取批次映射值',PRIMARY KEY(BatchMap),unique KEY complex_unique(CompanyMap  , BatchDate),FOREIGN KEY (CompanyMap) REFERENCES UserPortrait_CooperationCompany (CompanyMap));"
            self._MysqlCursor.execute(MysqlCommand)
            self._MysqlCursor.execute(CreateDataExtractBatch)
        except Exception as result:
            print("新建 UserPortrait_DataExtractBatch 数据表错误！ %s" % result)
    def CreateTagClassifyTable(self,DatabaseName="label_support"):
        try:
            MysqlCommand="use %s;" % DatabaseName
            CreateTagClassify="create table if not exists UserPortrait_TagClassify ( TagClassifyName Varchar(50)  not null unique comment '用户画像标签种类名称',TagClassifyFlag char(20)  not null default 'MainClass' comment '标签分类标志', TagClassifyMap  int auto_increment comment '用户画像标签种类映射值',PRIMARY KEY(TagClassifyMap ));"
            self._MysqlCursor.execute(MysqlCommand)
            self._MysqlCursor.execute(CreateTagClassify)
        except Exception as result:
            print("新建 UserPortrait_TagClassify 数据表错误！ %s" % result)
    def CreateClassifyValueTable(self,DatabaseName="label_support"):
        try:
            MysqlCommand="use %s;" % DatabaseName
            CreateClassifyValue="create table if not exists UserPortrait_ClassifyValue (TagClassifyMap int comment '用户画像标签种类映射值', ClassifyValue Varchar(50) not null comment '标签值描述' ,FatherTagName Varchar(50) not null comment '父标签名称',TagGradeFlag smallint not null comment '标签登记标志', ClassifyValueFlag char(20) not null default 'Equal' comment '标签值运算规则',ValueMin int comment '最小值',ValueMax int comment '最大值', ClassifyValueMap  int auto_increment comment '标签值映射',PRIMARY KEY(ClassifyValueMap),unique KEY complex_unique(TagClassifyMap ,ClassifyValue,FatherTagName),FOREIGN KEY (TagClassifyMap) REFERENCES UserPortrait_TagClassify (TagClassifyMap));"
            self._MysqlCursor.execute(MysqlCommand)
            self._MysqlCursor.execute(CreateClassifyValue)
        except Exception as result:
            print("新建 UserPortrait_ClassifyValue 数据表错误！ %s" % result)
    def CreateResultPersonNumberTable(self,DatabaseName="label_support"):
        try:
            MysqlCommand="use %s;" % DatabaseName
            CreateResultPersonNumber="create table UserPortrait_ResultPersonNumber (ID bigint primary key auto_increment comment '用户覆盖数结果记录索引', BatchMap int  not null comment '数据提取批次映射值', ClassifyValueMap int not null comment '标签值映射', TotalPopulation  bigint not null comment '标签覆盖人数',unique KEY complex_unique(BatchMap  , ClassifyValueMap),FOREIGN KEY (BatchMap) REFERENCES UserPortrait_DataExtractBatch (BatchMap),FOREIGN KEY (ClassifyValueMap) REFERENCES UserPortrait_ClassifyValue (ClassifyValueMap));"
            self._MysqlCursor.execute(MysqlCommand)
            self._MysqlCursor.execute(CreateResultPersonNumber)
        except Exception as result:
            print("新建 UserPortrait_ResultPersonNumber 数据表错误！ %s" % result)

    def ConnectMysql(self):
        try:
            self._MysqlDatabase = pymysql.connect(host=self._MysqlHost["host"],port=self._MysqlHost["port"],user=self._MysqlHost["user"], passwd=self._MysqlHost["password"])
            self._MysqlCursor=self._MysqlDatabase.cursor()
            #print(self._MysqlCursor)
            #print(self._MysqlDatabase)
        except Exception as result:
            print("连接数据库错误！ %s" % result)   # 连接数据库，成员函数···

    def DropTables(self):
        #RequisiteTableList = ['CooperationCompany', 'DataExtractBatch', 'TagClassify', 'ClassifyValue','ResultPersonNumber']
        #必须按照顺序删除表····有外键约束··
        RequisiteTableList = ['UserPortrait_ResultPersonNumber', 'UserPortrait_ClassifyValue', 'UserPortrait_TagClassify', 'UserPortrait_DataExtractBatch', 'UserPortrait_CooperationCompany']
        for Table in RequisiteTableList:
            MysqlDropCommand="drop table %s.%s;" % (self._UseDatabase,Table)
            #print(MysqlDropCommand)
            self._MysqlCursor.execute(MysqlDropCommand)

    def DatabaseClose(self):
        self._MysqlDatabase.close()
#testa=Mysql('127.0.0.1',3306,'root','mysql')
