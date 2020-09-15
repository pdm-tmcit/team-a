import fasttext as ft

def main(text):

    #classifier = ft.load_model('model.bin')
    model = ft.load_model("model_filename.bin")

    if text == '':
        estimate = model.predict([" >> 754 村 側 に そんな こと は 言っ て ない … … だっ たら ほぼ 羊 が 真 で 決まり なん じゃ が なあ 。 オットー の 散り 際 が 虚勢 だっ たら いい ん じゃ が の 。>> 744 は 一昨日 の 話 かのう 。 占 騙 灰 2 霊 2 に 1 狼 の 環境 の 中 で 占 狼 灰 狼 の 可能 性 に 期待 し て おっ た ん じゃ 。 で 霊 だ と 占い が 不 確 じゃ が 灰 は 灰 内訳 を 確定 さ せる 。 ただ 冷静 に 考えれ ば 占い が 切り捨て られ てる ん じゃ から 占 狼 は 薄かっ た ん じゃろ な"], k=6)
    else:
        estimate = model.predict([text], k=6)
    print("ラベル: "+estimate[0][0][0].replace(' ', ''),", 確率: "+str(estimate[1][0][0]))
    #print(model.words)
    #print(model.predict('human'))

    return estimate[0][0][0].replace(' ', '-')

if __name__ == '__main__':
    main('')
