# display_cards.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from deck import DeckOfCards

'''Program for displaying a deck of Cards'''
deck_of_cards = DeckOfCards()
deck_of_cards.shuffle()

path = Path('.').joinpath('oop/card_images')

figure, axes_list = plt.subplots(nrows=4, ncols=13)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name.lower()
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

figure.tight_layout()
plt.show()