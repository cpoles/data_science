"""Visualising Roll Die Frequencies and Percentages"""

from sys import argv
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def die_roll():
    '''Produces the visual representation'''
    number_of_rolls = int(argv[1])
    # generates die rolling data
    rolls = [random.randrange(1, 7) for _ in range(number_of_rolls)]
    # get the frequencies of each die face
    values, frequencies = np.unique(rolls, return_counts=True)
    # set the plot title, axis labels and max y number
    title = f'Rolling a Six-Sided Die {number_of_rolls:,} Times'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=values, y=frequencies, palette='bright')
    axes.set_title(title)
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)
    # print frequency and percentage on top of each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / number_of_rolls:.3%}'
        axes.text(text_x, text_y, text,
                  fontsize=11, ha='center', va='bottom')
    # show the plot
    plt.show()


die_roll()
