import os
import re
import json

def main():


    with open("./config.json", "r") as f:
        json_dict = json.load(f)
        separator = json_dict["separator"]

    # このプログラムのフォルダからのパス
    textPath = './text'
    csvPath = './csv'

    # textPath以下のファイル一覧を取得
    files = os.listdir(textPath)
    file = [f for f in files if os.path.isfile(os.path.join(textPath, f))]


    for i in file:
        headers = []
        body = []
        textFile = textPath+"/"+i
        csvFile = csvPath+"/"+i.replace(".txt","")+".csv"
        with open(textFile,"r") as f:
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

if __name__ == "__main__":
    main()