import sys
import fasttext as ft
from pprint import pprint 

'''
パラメータ説明
dim, 次元の数
lr, 学習率（1.0に近いほど学習が早いけれど不安定）
epoch, 学習回数（デフォルト5 多すぎると過学習）
'''
model = ft.train_supervised('test.txt', dim = 200, lr = 0.5, epoch = 10, thread = 16)
model.save_model("model_filename.bin")

#pprint(model.labels)

pprint(model.test_label("test.txt"))
pprint(model.test('test.txt'))