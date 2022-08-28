import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class TyreseHaliburton:
    def __init__(self):
        self.hali_shooting_df = pd.read_csv("TyreseHaliburtonShooting.csv")
        self.hali_shooting_df.dropna(axis=1, inplace=True, how='all')

    def shooting_stats(self):
        print(self.hali_shooting_df.columns)

    def shooting_percentage_graph(self):
        graph_data = self.hali_shooting_df[self.hali_shooting_df['Tm'] != 'TOT']
        graph_data = graph_data.dropna(subset=['Age'])
        years = range(1, graph_data.shape[0] + 1)
        years_labels = ['2020-2021', '2021-2022 SAC', '2021-2022 IND']
        shooting_2p = graph_data['2P'].to_list()
        shooting_3p = graph_data['3P'].to_list()
        shooting_fg = graph_data['FG'].to_list()
        shooting_efg = graph_data['eFG'].to_list()
        shooting_ft = graph_data['FT'].to_list()
        plt.title('Tyrese Haliburton Shooting')
        plt.xlabel('Season')
        plt.ylabel('Shooting %')
        plt.ylim([0, 1])
        plt.yticks(np.linspace(0, 1, 11))
        plt.xticks(years, years_labels)
        plt.plot(years, shooting_ft, label='FT%', linestyle='--', marker='o')
        plt.plot(years, shooting_efg, label='eFG%', linestyle='--', marker='o')
        plt.plot(years, shooting_2p, label='2P%', linestyle='--', marker='o')
        plt.plot(years, shooting_fg, label='FG%', linestyle='--', marker='o')
        plt.plot(years, shooting_3p, label='3P%', linestyle='--', marker='o')
        plt.legend(loc='lower center')
        plt.show()
        plt.close()
        print(graph_data)
