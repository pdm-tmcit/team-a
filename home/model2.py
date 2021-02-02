import csv
import fasttext as ft
import MeCab
import pprint
import random

def main(text):

    #classifier = ft.load_model('model.bin')
    model = ft.load_model("model_filename.bin")

    if text == '':
        estimate = model.predict([" >> 754 �� �� �� ����� ���� �� ���� �� �Ȃ� �c �c ���� ���� �ق� �r �� �^ �� ���܂� �Ȃ� ���� �� �Ȃ� �B �I�b�g�[ �� �U�� �� �� ���� ���� ���� ���� �� ���� �� �� �B>> 744 �� ���� �� �b ���̂� �B �� �x  �D 2 �� 2 �� 1 �T �� �� �� �� �� �� �T �D �T �� �\ �� �� ���� �� �� ���� �� �� ���� �B �� �� �� �� �肢 �� �s �m �� �� �� �D �� �D ���� �� �m�� �� ���� �B ���� ��� �� �l���� �� �肢 �� �؂�̂� ��� �Ă� �� ���� ���� �� �T �� ������ �� �� ����� ��"], k=6)
    else:
        estimate = model.predict([text], k=6)
    #print("���x��: "+estimate[0][0][0].replace(' ', ''),", �m��: "+str(estimate[1][0][0]))
    #print(model.words)
    #print(model.predict('human'))

    return estimate[0][0][0].replace(' ', '-')

villager = {"1":"�{�N����Ȃ��ł���₾�[", "2":"�܁H", "3":"���l�łÁB", "4":"�i�C�X��", "5":"�����������܂�", "6":"�l �����܂���", "7":"(....����....zzz�j", "8":"(....zzz)", "9":"�ց["}
wlof = {"1":"�Ⴂ�܂���`", "2":"�܁H", "3":"���l�łÁB", "4":"�i�C�X��", "5":"����������", "6":"���肪�Ƃ��������܂��B", "7":"(....����....zzz�j", "8":"(�܂��Q�Ă悤....zzz)", "9":"���[��"}
hamstar = {"1":"�Ⴂ�܂���`", "2":"�Ӂ[��", "3":"���l�łÁB", "4":"����ˁB", "5":"���������肪�Ƃ�", "6":"���肪�Ƃ�", "7":"(....����....zzz�j", "8":"(....zzz)", "9":"�Ӂ[��"}
fortune = {"1":"�Ⴂ�܂���`", "2":"��", "3":"�肢�t�ł��ˁ`", "4":"�����", "5":"�������", "6":"���肪�Ƃ�", "7":"(....����....zzz�j", "8":"(....zzz)", "9":"�ց["}
medium = {"1":"�Ⴂ�܂���`", "2":"�܁H", "3":"���l�ł�", "4":"�����", "5":"���������񂭂�", "6":"�Ă񂭂�", "7":"�� �^�Ȃ񂾂��", "8":"(....zzz)", "9":"�ց["}
hunter = {"1":"�Ⴂ�܂���`", "2":"�܁H", "3":"���l�ł�", "4":"�����", "5":"���������", "6":"����", "7":"(....���`��....zzz", "8":"�������ꂢ...", "9":"���`��"}
co_owner = {"1":"�Ⴄ��", "2":"�Ӂ[��", "3":"���L�҂ł��˂�", "4":"�����", "5":"�����������܂�", "6":"����", "7":"(........zzz)", "8":"(....zzz)", "9":"��������"}
madman = {"1":"�Ⴄ�񂾂�Ȃ�", "2":"�ց[", "3":"���l�ł���", "4":"�i�C�X��", "5":"���������񂭂�", "6":"����", "7":"(....����....zzz)", "8":"(....zzz)", "9":"��������"}


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

def export(day,doubt_to,black,white):#�������o�͕���
    if day == "pre":
        return
    print(day)
    print("SUS",end="")
    Exec = most(doubt_to)   #���Y�Ώۂ̏o��
    print("BLACK",end="")
    Orac = most(black)  #�肢�Ώۂ̏o��
    print("WHITE" + str(white)) #�݂��Ώۂ������͎E�Q��̑Ώۂ̏o��
    if day != "�v�����[�O":
        if doubt_to != {}:
            Exec = random.choice(Exec)
        else:
            Exec = random.choice(chr_list)
        print("Executioned : " + Exec)
        if black != {}:
            Orac = random.choice(Orac)
        else:
            Orac = random.choice(chr_list)
        print("Oracle : " + Orac)
        if white != {}:
            Sacr = random.choice(list(white.keys()))
            Prot = random.choice(list(white.keys()))
        else:
            Sacr = random.choice(chr_list)
            Prot = random.choice(chr_list)
        print("Sacrifice : " + Sacr)
        print("Protected : " + Prot)
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
        if remark[i] == "��":
            if remark[i+1] in name:
                adana = name[remark[i+1]]
                if adana not in black:
                    black[adana] = 1
                else:
                    black[adana] += 1
            while remark[i+j] in name or remark[i+j] == "�A":
                if remark[i+j] in name:
                    adana = name[remark[i+j]]
                    if adana not in black:
                        black[adana] = 1
                    else:
                        black[adana] += 1
                elif remark[i+j] == "�A":
                    pass
                j+=1



        if remark[i] == "��":
            if remark[i+1] in name:
                adana = name[remark[i+1]]
                if adana not in white:
                    white[adana] = 1
                else:
                    white[adana] += 1
            while remark[i+j] in name or remark[i+j] == "�A":
                if remark[i+j] in name:
                    adana = name[remark[i+j]]
                    if adana not in black:
                        black[adana] = 1
                    else:
                        black[adana] += 1
                elif remark[i+j] == "�A":
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