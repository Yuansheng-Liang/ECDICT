import stardict
import os
import py7zr


# 获取当前文件所在目录
current_file_directory = os.path.dirname(os.path.abspath(__file__))

db = "stardict/stardict.db"
db_dict = os.path.join(current_file_directory, db)


def convert():
    dstname = db_dict
    srcname = os.path.join(current_file_directory, "stardict/stardict.csv")

    if not os.path.exists(srcname):
        file_path = os.path.join(current_file_directory, "stardict.7z")
        extract_to_path = os.path.join(current_file_directory, "stardict")
        with py7zr.SevenZipFile(file_path, mode='r') as archive:
            print(f"正在解压文件 {file_path} ~~")
            archive.extractall(extract_to_path)

    print(f"正在生成数据库 {dstname} ~~")
    stardict.convert_dict(dstname, srcname)


def query(en_str):
    dictionary = stardict.open_dict(db_dict)
    return dictionary.query(en_str)


if __name__ == '__main__':
    if not os.path.exists(db_dict):
        convert()
    print(query("subprocess"))
