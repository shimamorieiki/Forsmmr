import os
import re
import json
import glob

def main():

    with open("./config.json", "r") as f:
        json_dict = json.load(f)
        separator = json_dict["separator"]

    # textPath以下のファイル一覧を取得
    files = glob.glob('./**/*.txt', recursive=True)

    for i in files:
        headers = []
        body = []
        csvFile = i.replace(".txt","")+".csv"
        if ".txt" not in i:
            continue
        with open(i,"r") as f:
            with open(csvFile,"w") as w:

                # テキストの文字列を取得
                readLines = f.readlines();

                # 文字列を一行ずつ取得
                for line in readLines:

                    # 空白を削除する
                    line = re.sub(r"(\s|\t)+", " ", line)

                    # "#"があればヘッダーとして扱う
                    if "#" in line:
                        headers.append(line.replace("\n","").strip())
                    
                    # 空白行じゃなければbodyとして読み込む
                    elif len(line) != 1:
                        body.append(line.replace("\n","").strip().split(" "))

                # ヘッダー部分書き込み
                w.write(separator.join(headers[1:]).strip()+"\n")

                # ボディー部分書き込み
                for line in body:
                    w.write(separator.join(line)+"\n")
        # os.remove(i)
if __name__ == "__main__":
    main()