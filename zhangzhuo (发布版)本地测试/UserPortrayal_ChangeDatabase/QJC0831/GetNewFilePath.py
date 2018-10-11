import os
def filenames(path):
    with open(path,'r') as f:
        files=f.readlines()
        result=[]
        for file in files:
            result.append(file.strip('\n'))
        return result
def serves_filenames(severse_path):
    result=os.listdir(severse_path)
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
    result_names=[]
    try:
        with open(path,'a+') as f:
            for name in result:
                result_names.append(severse_path+'/'+name)
                f.write(name+'\n')
        return result_names
    except:
        return []