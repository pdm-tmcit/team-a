import fasttext as ft

def main(text):

    #classifier = ft.load_model('model.bin')
    model = ft.load_model("model_filename.bin")

    if text == '':
        estimate = model.predict(["pizza"], k=6)
    else:
        estimate = model.predict([text], k=6)
    print("ラベル: "+estimate[0][0][0],", 確率: "+str(estimate[1][0][0]))
    #print(model.words)
    #print(model.predict('human'))

    return estimate[0][0][0]

if __name__ == '__main__':
    main('')
