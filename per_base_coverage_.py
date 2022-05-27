import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_csv('coverage.csv', dtype=int)


def coverage_plot (data, color):
    ''' data: A pandas dataframe, with a 'Position' column, and a 'Coverage' column,
        color: The hex code of a color as a string
        sample usage `coverage_plot(data, '#A0D3FE')` '''

    ## Version 1

    sns.set_style('dark')
    fig, ax1 = plt.subplots(figsize=(70, 10))
    sns.lineplot(data=data, x="Position", y="Coverage", ax=ax1)
    data['Coverage'].plot.area(stacked=False, color={'Coverage': color}, alpha=0.2, ax=ax1)
    ax1.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, pos: format(x/1000,'1.1f')))
    ax1.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.xlim(0, 19000)
    plt.xlabel('Position (kilobase)', fontsize=50)
    plt.ylabel('Coverage', fontsize=50)
    plt.savefig('per_base_coverage.svg')

    plt.show()

coverage_plot(data, '#A0D3FE')