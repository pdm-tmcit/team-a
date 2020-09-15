import csv
import fasttext as ft

def main(text):

    #classifier = ft.load_model('model.bin')
    model = ft.load_model("model_filename.bin")

    if text == '':
        estimate = model.predict([" >> 754 村 側 に そんな こと は 言っ て ない … … だっ たら ほぼ 羊 が 真 で 決まり なん じゃ が なあ 。 オットー の 散り 際 が 虚勢 だっ たら いい ん じゃ が の 。>> 744 は 一昨日 の 話 かのう 。 占 騙 灰 2 霊 2 に 1 狼 の 環境 の 中 で 占 狼 灰 狼 の 可能 性 に 期待 し て おっ た ん じゃ 。 で 霊 だ と 占い が 不 確 じゃ が 灰 は 灰 内訳 を 確定 さ せる 。 ただ 冷静 に 考えれ ば 占い が 切り捨て られ てる ん じゃ から 占 狼 は 薄かっ た ん じゃろ な"], k=6)
    else:
        estimate = model.predict([text], k=6)
    #print("ラベル: "+estimate[0][0][0].replace(' ', ''),", 確率: "+str(estimate[1][0][0]))
    #print(model.words)
    #print(model.predict('human'))

    return estimate[0][0][0].replace(' ', '-')

villager = {"1":"ボクじゃないですよやだー", "2":"ま？", "3":"村人でづ。", "4":"ナイスぅ", "5":"ぎだいあざまる", "6":"僕もつられますよ", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"へー"}
wlof = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ。", "4":"ナイスぅ", "5":"ぎだいあざ", "6":"ありがとうございます。", "7":"(....眠い....zzz）", "8":"(まだ寝てよう....zzz)", "9":"うーん"}
hamstar = {"1":"違いますよ～", "2":"ふーん", "3":"村人でづ。", "4":"やるわね。", "5":"ぎだいありがとう", "6":"ありがとう", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"ふーん"}
fortune = {"1":"違いますよ～", "2":"ん", "3":"占い師ですね～", "4":"やるわね", "5":"きたわね", "6":"ありがとう", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"へー"}
medium = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ", "4":"やるやん", "5":"ぎだいさんくす", "6":"てんくす", "7":"夜型なんだよね", "8":"(....zzz)", "9":"へー"}
hunter = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ", "4":"やるやん", "5":"ぎだいりょ", "6":"あり", "7":"(....う～ん....zzz", "8":"月がきれい...", "9":"う～ん"}
co_owner = {"1":"違うで", "2":"ふーん", "3":"共有者ですねぇ", "4":"やるわね", "5":"ぎだいあざまる", "6":"あり", "7":"(........zzz)", "8":"(....zzz)", "9":"そっかぁ"}
madman = {"1":"違うんだよなぁ", "2":"へー", "3":"村人ですね", "4":"ナイスぅ", "5":"ぎだいさんくす", "6":"あり", "7":"(....眠い....zzz)", "8":"(....zzz)", "9":"そっかぁ"}


f = open('village_g86.csv', 'r')
fp = open('test.csv','a')

reader = csv.reader(f)
header = next(reader)
for row in reader:
    #print(row,'\n\n')
    if row[3] =='':
        villager_label = main(str(a))
        print(villager_label)

        if villager_label == '__label__1':
            print(villager["1"])
            row[3] = villager["1"]
        if villager_label == '__label__2':
            print(villager["2"])
            row[3] = villager["2"]
        if villager_label == '__label__3':
            print(villager["3"])
            row[3] = villager["3"]
        if villager_label == '__label__4':
            print(villager["4"])
            row[3] = villager["4"]
        if villager_label == '__label__5':
            print(villager["5"])
            row[3] = villager["5"]
        if villager_label == '__label__6':
            print(villager["6"])
            row[3] = villager["6"]
        if villager_label == '__label__7':
            print(villager["7"])
            row[3] = villager["7"]
        if villager_label == '__label__8':
            print(villager["8"])
            row[3] = villager["8"]
        if villager_label == '__label__9':
            print(villager["9"])
            row[3] = villager["9"]


    fp.write(str(row[0]+','+row[1]+','+row[2]+','+row[3]+','+'\n'))
    a = row[3]

f.close()
fp.close()
