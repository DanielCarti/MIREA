import time

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def kurs_lev(days=16, color='purple'):
    kurs = pd.read_csv('C:\\Users\\Daniel\\Documents\\KursachProject\\MIREA\\BGN\\kurs1.csv', index_col=0)
    kurs.head()
    days = int(days)
    color = str(color)
    name_of_row = kurs['kurs_rub'].values[:days]
    number_days = [i + 1 for i in range(days)]

    sns.lineplot(x=number_days, y=name_of_row, color=color)
    plt.legend(labels=["Курс BGN/RUB"], title="y=BGN/RUB, x=Days")
    ts = str(time.time()).replace('.', '')
    image_path = f"C:\\Users\\Daniel\\Documents\\KursachProject\\MIREA\\Images\\kurs_levdata{ts}.png"
    plt.savefig(f'{image_path}')
    return image_path
