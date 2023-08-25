import os

def dirs_file_list(fpath):
    file_list = []
    if os.path.exists(fpath):
        for f in os.listdir(fpath):
            new_path = fpath + '\\' + f
            if os.path.isdir(new_path):
                file_list += dirs_file_list(new_path)
            else:
                file_list.append(new_path)
    else:
        return []

    return file_list

res = dirs_file_list(r'D:\dirs\Work\python_study\resorce\第1-12章资料')
print(len(res))
print(res)
