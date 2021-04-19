# coin_tossing.py
'''Dynamically graphing frequencies of coin tossings'''

# import libraries
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys


# define the update function that FuncAnimation calls once per animation frame


def update(frame_number, tosses, faces, frequencies):
    '''Configures bar plot contents for each animation frame.'''
    # toss coin and update frequencies
    for _ in range(tosses):
        frequencies[random.randrange(1, 3) - 1] += 1

        # reconfigure plot for updated toss frequencies
        plt.cla()  # clear old contents of current figure
        axes = sns.barplot(faces, frequencies, palette='bright')  # new bars
        axes.set_title(f'Coin Frequencies for {sum(frequencies):,} Tosses')
        axes.set(xlabel='Toss', ylabel='Frequency')
        axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

        # display frequency & percentage above each path (bar)
        for bar, frequency in zip(axes.patches, frequencies):
            text_x = bar.get_x() + bar.get_width() / 2.0
            text_y = bar.get_height()
            text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
            axes.text(text_x, text_y, text, ha='center', va='bottom')


# file executing
print(sys.argv[0])

# read command-line arguments for number of frames and rolls per frame
number_of_frames = int(sys.argv[1])
tosses_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Tossing a Coin')  # Figure for animation
values = ['Heads', 'Tails']  # coin sides for display on x-axis
frequencies = [0] * 2  # two-element list of die frequencies

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(figure, update, repeat=False,
                                        frames=number_of_frames,
                                        interval=23,
                                        fargs=(tosses_per_frame, values,
                                               frequencies))


plt.show()


