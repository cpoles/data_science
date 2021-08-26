"""Visualising Roll Dice and Percentages"""


from sys import argv
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def dice_roll():
    # get number of rolls input
    num_rolls = int(argv[1])

    # simulate dice rolls
    rolls = [random.randrange(1, 7) + random.randrange(1, 7) for _ in range(num_rolls)]
    # get the frequencies for each dice sum
    sums, frequencies = np.unique(rolls, return_counts=True)
    # set the plot title, axis labels and max y number
    title = f'Rolling Two Six-Sided Dice {num_rolls:,} Times'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=frequencies, y=sums, palette='bright', orient='h')
    axes.set_title(title)
    axes.set(xlabel='Frequency', ylabel='Dice Value')
    axes.set_xlim(right=max(frequencies) * 1.10) 
    axes.set_ylim(bottom=-1, top=12)
    # print frequency and percentage on top of each bar
    
    for bar, frequency in zip(axes.patches, frequencies):
        text_y = bar.get_y() + bar.get_height()
        text_x = bar.get_width() * 1.10
        text = f'{frequency:,}\n{frequency / num_rolls:.3%}'
        axes.text(text_x, text_y, text,
            fontsize=10, ha='center', va='bottom')
    
    # show the plot
    plt.show()
    

dice_roll()
