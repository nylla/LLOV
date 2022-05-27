import seaborn as sns
import pandas as pd
from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt

mutations_df = pd.read_csv('mutation_data.csv')
mutations_df['Year'] = mutations_df['Year'].astype('int')

def mutation_plotter(df, xdata, ydata, style='darkgrid'):
    cdict = {'NP': '#FD56DC', 'VP35': '#39FF14', 'VP40': '#06B3A7', 'GP': '#00B5E2', 'VP30': '#0070C0',
             'VP24': '#52307C', 'L': '#011034'}

    sns.set_style(style)

    p = sns.lmplot(
        data=df, x=xdata, y=ydata, hue="Gene", ci=None,
        height=10, aspect=1, palette=cdict, scatter_kws={'alpha': 0.5},
        line_kws={"alpha": 0.5, "lw": 1, 'linestyle': '--'},
        markers=['o', 'x', '+', 's', 'v', '^', 'd' ]
    )

    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
    plt.ylabel(ydata + ' / kb', fontsize=22)
    plt.title(ydata, fontsize=22)
    # plt.xlim(2002, 2022)
    # plt.ylim(0,)
    plt.xticks([2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022])
    plt.show()
    p.savefig(ydata + '.png')

mutation_plotter(mutations_df, 'Year', 'Mutations')
mutation_plotter(mutations_df, 'Year', 'Synonimous mutations')
mutation_plotter(mutations_df, 'Year', 'Non synonimous mutations')

