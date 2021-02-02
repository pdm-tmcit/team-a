import csv
import fasttext as ft
import MeCab
import pprint
import random

def main(text):

    #classifier = ft.load_model('model.bin')
    model = ft.load_model("model_filename.bin")

    if text == '':
        estimate = model.predict([" >> 754 村 側 に そんな こと は 言っ て ない … … だっ たら ほぼ 羊 が 真 で 決まり なん じゃ が なあ 。 オットー の 散り 際 が 虚勢 だっ たら いい ん じゃ が の 。>> 744 は 一昨日 の 話 かのう 。 占 騙  灰 2 霊 2 に 1 狼 の 環境 の 中 で 占 狼 灰 狼 の 可能 性 に 期待 し て おっ た ん じゃ 。 で 霊 だ と 占い が 不 確 じ ゃ が 灰 は 灰 内訳 を 確定 さ せる 。 ただ 冷静 に 考えれ ば 占い が 切り捨て られ てる ん じゃ から 占 狼 は 薄かっ た ん じゃろ な"], k=6)
    else:
        estimate = model.predict([text], k=6)
    #print("ラベル: "+estimate[0][0][0].replace(' ', ''),", 確率: "+str(estimate[1][0][0]))
    #print(model.words)
    #print(model.predict('human'))

    return estimate[0][0][0].replace(' ', '-')

villager = {"1":"ボクじゃないですよやだー", "2":"ま？", "3":"村人でづ。", "4":"ナイスぅ", "5":"ぎだいあざまる", "6":"僕 もつられますよ", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"へー"}
wlof = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ。", "4":"ナイスぅ", "5":"ぎだいあざ", "6":"ありがとうございます。", "7":"(....眠い....zzz）", "8":"(まだ寝てよう....zzz)", "9":"うーん"}
hamstar = {"1":"違いますよ～", "2":"ふーん", "3":"村人でづ。", "4":"やるわね。", "5":"ぎだいありがとう", "6":"ありがとう", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"ふーん"}
fortune = {"1":"違いますよ～", "2":"ん", "3":"占い師ですね～", "4":"やるわね", "5":"きたわね", "6":"ありがとう", "7":"(....眠い....zzz）", "8":"(....zzz)", "9":"へー"}
medium = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ", "4":"やるやん", "5":"ぎだいさんくす", "6":"てんくす", "7":"夜 型なんだよね", "8":"(....zzz)", "9":"へー"}
hunter = {"1":"違いますよ～", "2":"ま？", "3":"村人でづ", "4":"やるやん", "5":"ぎだいりょ", "6":"あり", "7":"(....う～ん....zzz", "8":"月がきれい...", "9":"う～ん"}
co_owner = {"1":"違うで", "2":"ふーん", "3":"共有者ですねぇ", "4":"やるわね", "5":"ぎだいあざまる", "6":"あり", "7":"(........zzz)", "8":"(....zzz)", "9":"そっかぁ"}
madman = {"1":"違うんだよなぁ", "2":"へー", "3":"村人ですね", "4":"ナイスぅ", "5":"ぎだいさんくす", "6":"あり", "7":"(....眠い....zzz)", "8":"(....zzz)", "9":"そっかぁ"}


def most(dicts):
    j = 0
    Max = []
    Maxn = []
    for i in dicts:
        if j == 0:
            Max.append(dicts[i])
            Maxn.append(i)
        if dicts[i] > Max[0]:
            Max = []
            Maxn = []
            Max.append(dicts[i])
            Maxn.append(i)
        elif j == 1 and dicts[i] == Max[0]:
            Max.append(dicts[i])
            Maxn.append(i)
        j = 1
    print(str(Maxn) + ":" + str(Max))
    return Maxn
    #return (str(Maxn) + ":" + str(Max))

def export(day,doubt_to,black,white):#ここが出力部分
    if day == "pre":
        return
    print(day)
    print("SUS",end="")
    Exec = most(doubt_to)   #処刑対象の判定
    print("BLACK",end="")
    Orac = most(black)  #占い対象の判定
    print("WHITE" + str(white)) #庇う対象もしくは殺害先の対象の判定
    if day != "プロローグ":
        if doubt_to != {}:
            Exec = random.choice(Exec)
        else:
            Exec = random.choice(chr_list)
        print("Executioned : " + Exec)#Execが処刑先
        if black != {}:
            Orac = random.choice(Orac)
        else:
            Orac = random.choice(chr_list)
        print("Oracle : " + Orac)#Oracが占い先
        if white != {}:
            Sacr = random.choice(list(white.keys()))
            Prot = random.choice(list(white.keys()))
        else:
            Sacr = random.choice(chr_list)
            Prot = random.choice(chr_list)
        print("Sacrifice : " + Sacr)#Sacrが人狼の殺害先
        print("Protected : " + Prot)#Protが狩人の庇う先
    print("\n")



#ADD NAME_DICT
name = {}
chr_list=[]
fn = open('player_name.txt', 'r')
for line in fn:
    line = line.replace("\n","")
    line = line.split(":")
    #print(line)
    name[line[1]] = line[0]
fn.close()


doubt_to = {}
chr_flag = {}
black = {}
white = {}
m_t = MeCab.Tagger('-Owakati')
count = 0
day = "pre"

f = open('village_g10all.csv', 'r')
fp = open('test.csv','a')

reader = csv.reader(f)
header = next(reader)
for row in reader:

    if str(row[0]) != day:  #RESET
        export(day,doubt_to,black,white)
        day = row[0]
        doubt_to = {}
        black = {}
        white = {}
    #print(str(count) + ":" + str(row))

    row[3] = m_t.parse(str(row[3]))
    row[3] = row[3].replace('\n','')
    remark = row[3].split(' ')
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

    #ADD
    if row[1] not in chr_flag:
        chr_flag[row[1]] = 0
        chr_list.append(row[1])

    if row[1] not in doubt_to:
        doubt_to[row[1]] = 0

    for i in range(len(remark)):
        j=2
        if remark[i] == "●":
            if remark[i+1] in name:
                adana = name[remark[i+1]]
                if adana not in black:
                    black[adana] = 1
                else:
                    black[adana] += 1
            while remark[i+j] in name or remark[i+j] == "、":
                if remark[i+j] in name:
                    adana = name[remark[i+j]]
                    if adana not in black:
                        black[adana] = 1
                    else:
                        black[adana] += 1
                elif remark[i+j] == "、":
                    pass
                j+=1



        if remark[i] == "○":
            if remark[i+1] in name:
                adana = name[remark[i+1]]
                if adana not in white:
                    white[adana] = 1
                else:
                    white[adana] += 1
            while remark[i+j] in name or remark[i+j] == "、":
                if remark[i+j] in name:
                    adana = name[remark[i+j]]
                    if adana not in black:
                        black[adana] = 1
                    else:
                        black[adana] += 1
                elif remark[i+j] == "、":
                    pass
                j+=1

    #print(str(chr_flag) + "\n")
    #print(doubt_to)

    #print(str(count) + ":" + main(str(a)) + str(a))

    if main(str(a)) == '__label__1':
        doubt_to[row[1]] += 1
    count += 1

export(day,doubt_to,black,white)
#print(day)
#pprint.pprint(most(doubt_to))
#print("BLACK" + str(most(black)))
#print("WHITE" + str(most(white)))

f.close()
fp.close()
