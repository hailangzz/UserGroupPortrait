import os,shutil

def deletetestdata(filenamelist):
    strfilenamelist=[]
    for filename in filenamelist:
        strfilenamelist.append(str(filename)+'.txt')
    #print(strfilenamelist)
    appdatapath=r'F:\UserGroupPortraitData\app'
    #os.path.join(path, sub_name)
    os.chdir(appdatapath)  # 切换到app目录
    listfile=os.listdir(appdatapath)
    print(listfile)
    for filetxt in strfilenamelist:
        filepath=os.path.join(appdatapath, filetxt)
        os.remove(filepath)
    basicdatapath =r'F:\UserGroupPortraitData\basic'
    os.chdir(basicdatapath)  # 切换到basic目录
    for filetxt in strfilenamelist:
        filepath = os.path.join(basicdatapath, filetxt)
        os.remove(filepath)
    servicepath =r'F:\UserGroupPortraitData\service'
    os.chdir(servicepath)  # 切换到service目录
    for filetxt in strfilenamelist:
        filepath = os.path.join(servicepath, filetxt)
        os.remove(filepath)

def copydata(filenamelist):
    strfilenamelist = []
    for filename in filenamelist:
        strfilenamelist.append(str(filename)+'.txt')
    appdatapath = r'F:\UserGroupPortraitData\app'
    basicdatapath = r'F:\UserGroupPortraitData\basic'
    servicepath = r'F:\UserGroupPortraitData\service'
    applistfile = os.listdir(appdatapath)
    basiclistfile = os.listdir(basicdatapath)
    servicelistfile = os.listdir(servicepath)

    apptestdatapatn=r'F:\UserGroupPortraitData\test\app'
    basictestdatapatn = r'F:\UserGroupPortraitData\test\basic'
    servicetestdatapatn = r'F:\UserGroupPortraitData\test\service'
    for file in strfilenamelist:
        if file not in applistfile:
            shutil.copyfile(os.path.join(apptestdatapatn, file), os.path.join(appdatapath, file))

    for file in strfilenamelist:
        if file not in basiclistfile:
            shutil.copyfile(os.path.join(basictestdatapatn, file), os.path.join(basicdatapath, file))

    for file in strfilenamelist:
        if file not in servicelistfile:
            shutil.copyfile(os.path.join(servicetestdatapatn, file), os.path.join(servicepath, file))


def updatedealfilerecord(filenamelist):
    strfilenamelist = []
    for filename in filenamelist:
        strfilenamelist.append(str(filename) + '.txt')

    appdealrecordpath=r'F:\UserGroupPortraitDataCheck\filenames\app_filename.txt'
    basicdealrecordpath = r'F:\UserGroupPortraitDataCheck\filenames\basic_filename.txt'
    servicedealrecordpath = r'F:\UserGroupPortraitDataCheck\filenames\service_filename.txt'

    appdealrecord=[]
    basicdealrecord=[]
    servicedealrecord=[]

    appdealfilecur=open(appdealrecordpath,'r')
    appdeallist=appdealfilecur.readlines()
    for appdealname in appdeallist:
        if appdealname not in strfilenamelist:
            appdealrecord.append(appdealname)
    appdealfilecur.close()


    appdealfilecur=open(appdealrecordpath,'w')
    for appdealname in appdealrecord:
        appdealfilecur.write(appdealname)
    appdealfilecur.close()

    basicdealfilecur = open(basicdealrecordpath, 'r')
    basicdeallist = basicdealfilecur.readlines()
    for basicdealname in basicdeallist:
        if basicdealname not in strfilenamelist:
            basicdealrecord.append(basicdealname)
    basicdealfilecur.close()

    basicdealfilecur = open(basicdealrecordpath, 'w')
    for basicdealname in basicdealrecord:
        basicdealfilecur.write(basicdealname)
    basicdealfilecur.close()

    servicedealfilecur = open(servicedealrecordpath, 'r')
    servicedeallist = servicedealfilecur.readlines()
    for servicedealname in servicedeallist:
        if servicedealname not in strfilenamelist:
            servicedealrecord.append(servicedealname)
    servicedealfilecur.close()

    servicedealfilecur = open(servicedealrecordpath, 'w')
    for servicedealname in servicedealrecord:
        servicedealfilecur.write(servicedealname)
    servicedealfilecur.close()


def updatedealfilerecord():
    paths=[]
    appdealrecordpath = r'F:\UserGroupPortraitDataCheck\filenames\app_filename.txt'
    basicdealrecordpath = r'F:\UserGroupPortraitDataCheck\filenames\basic_filename.txt'
    servicedealrecordpath = r'F:\UserGroupPortraitDataCheck\filenames\service_filename.txt'
    paths.append(appdealrecordpath)
    paths.append(basicdealrecordpath)
    paths.append(servicedealrecordpath)

    for path in paths:
        with open(path, 'r') as f1:
            lines = f1.readlines()
        with open(path, 'w+') as f2:
            for l in lines[:-4]:
                f2.write(l)


def main():
    filenamelist=[1536654436,1536888240]
    #filenamelist = []
    #deletetestdata(filenamelist)
    #copydata(filenamelist)
    updatedealfilerecord()

if __name__ == '__main__':
    main()
    print("over program!")