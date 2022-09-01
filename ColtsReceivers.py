import pandas as pd

class ColtsReceivers:

    def __init__(self):
        self.receivers_stats_df = pd.read_csv("ColtsTopReceivers.csv")

    def topReceiversPost2008(self):
        wr_stats = self.receivers_stats_df[self.receivers_stats_df['Year'] >= 2008]
        print(f'Columns: {wr_stats.columns}')
        wr_stats = wr_stats[['Player', 'Year', 'Yds', 'TD', 'Rec']]
        print(wr_stats.sort_values('Yds', ascending=False).head(30))