import paramiko
conf={
    'host_ip':'192.168.8.145',
    'port':22,
    'username':'RIOpenApi4UMC',
    'password':'OArich@139.com'
}
def filenames(path):
    with open(path,'r') as f:
        files=f.readlines()
        result=[]
        for file in files:
            result.append(file.strip('\n'))
        return result
def serves_filenames(severse_path):
    t = paramiko.Transport(conf['host_ip'],conf['port'])
    t.connect(username=conf['username'],password=conf['password'])
    sftp=paramiko.SFTPClient.from_transport(t)
    result=[]
    for filename in sftp.listdir(severse_path):
        if ".txt" in filename:
            result.append(filename)
        else:
            pass
    return result
def diff_filename(path,severse_path):
    result=filenames(path)
    serves=serves_filenames(severse_path)
    result_filt=list(set(serves).difference(set(result)))
    if len(result_filt)>0:
        return  result_filt
    else:
        pass
def new_filenamepath(path,severse_path):
    result=diff_filename(path,severse_path)
    try:
        with open(path,'a+') as f:
            f.write(result[0]+'\n')
        return(severse_path+'/'+result[0])
    except:
        return None