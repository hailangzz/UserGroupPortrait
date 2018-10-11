import QJC0831.GetNewFilePath as GetNewFilePath
class App_data_path():
    def __init__(self):
        self.path = r'/home/appSys/RIOpenApi4UMC/userportrait/filenames/app_filename.txt'
        self.severse_path = r'/home/appSys/RIOpenApi4UMC/userportrait/app'
        self.new_path=(GetNewFilePath.new_filenamepath(self.path, self.severse_path))
    def get_path(self):
        data_path=[]
        if len(self.new_path)==0:
            print('服务器还没有上传新app文件！')
        else:
            print("发现新app文件")
            for name in self.new_path:
                paths=name
                localfilename=name.split('/')[-1]
                data_path.append(r"/home/appSys/RIOpenApi4UMC/userportrait/app/%s" % (localfilename))
        return data_path





