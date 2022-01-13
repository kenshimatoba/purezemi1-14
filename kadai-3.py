import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryob.ttc', size=10)
#データ準備
join1 = np.array([1452])
app1 = np.array([3231])
join2 = np.array([1796])
app2 = np.array([3747])
join3 = np.array([1894])
app3 = np.array([3726])
join4 = np.array([2584])
app4 = np.array([5853])
join5 = np.array([2735])
app5 = np.array([8866])
join6 = np.array([3447])
app6 = np.array([10913])
#グラフの装飾
plt.xlim(1000,3500)#x軸の表示範囲
plt.ylim(3000,12000)#y軸の表示範囲
plt.title("年度別のオープンキャンパス参加者数と志願者数", fontproperties=fp)#タイトル
plt.xlabel("オープンキャンパス参加者数(人)",fontproperties=fp)#x軸ラベル
plt.ylabel("志願者数(人)",fontproperties=fp)#y軸ラベル
plt.grid(True)#目盛線表示
plt.tick_params(labelsize=8)#目盛線のラベルサイズ

#グラフの描画
plt.scatter(join1, app1, s=50, c="b", marker="o", alpha=0.5,label="2014")
plt.scatter(join2, app2, s=50, c="g", marker="o", alpha=0.5,label="2015")
plt.scatter(join3, app3, s=50, c="r", marker="o", alpha=0.5,label="2016")
plt.scatter(join4, app4, s=50, c="c", marker="o", alpha=0.5,label="2017")
plt.scatter(join5, app5, s=50, c="m", marker="o", alpha=0.5,label="2018")
plt.scatter(join6, app6, s=50, c="y", marker="o", alpha=0.5,label="2019")

plt.legend(loc="upper left",fontsize=10 )#凡例表示 
plt.show()#図の表示