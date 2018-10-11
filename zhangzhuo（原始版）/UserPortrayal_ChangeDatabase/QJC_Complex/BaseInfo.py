import GetNewFilePath
import paramiko
import os
path = r'F:\data_resource\file_xzt\filenames\basic_filename.txt'
severse_path = '/home/appSys/RIOpenApi4UMC/xzt1/basic'
new_path=(GetNewFilePath.new_filenamepath(path, severse_path))
def sftp_down_file(server_path, local_path):
    try:
        t = paramiko.Transport(GetNewFilePath.conf['host_ip'], GetNewFilePath.conf['port'])
        t.connect(username=GetNewFilePath.conf['username'], password=GetNewFilePath.conf['password'])
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
    except Exception as e:
        print (e)
def getfilename(path):
    for (path, path_, filename) in os.walk(path):
        return filename
if new_path==None:
    print('服务器还没有上传新文件！')
else:
    print("发现新文件")
    localfilename=new_path.split('/')[-1]
    sftp_down_file(new_path, r"F:\data_resource\file_xzt\basic\%s.txt"%(localfilename))
    data_path = r"F:\data_resource\file_xzt\app\%s" % (localfilename)





