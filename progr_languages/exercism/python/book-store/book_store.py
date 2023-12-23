import copy

# maps size of group -> discount
SIZE_DISCOUNT = {
    1: 100,
    2: 95,
    3: 90,
    4: 80,
    5: 75
}

def total(basket):
    if not basket:
        return 0

    basket_count = {}.fromkeys(set(basket), 0)
    # count elements of the basket
    for book in basket:
        basket_count[book] += 1

    # basket_count = dict(sorted(basket_count.items(), key=lambda x: x[1]))
    
    # create groups
    groups = create_groups(basket_count)
    groups_of_four = create_groups(basket_count, of_four=True)
    groups_of_three = create_groups(basket_count, of_three=True)

    g_price, g_4price, g_3price = calculate_total_price(groups), calculate_total_price(groups_of_four), calculate_total_price(groups_of_three)

    lowest = min(g_price, g_4price, g_3price)

    if lowest > 0:
        return lowest


def create_groups(basket_count, of_four=False, of_three=False) -> list:
    basket = copy.deepcopy(basket_count)
    groups = []

    while True:
        group = []

        for book, count in basket.items():
            if count == 0:
                continue
            # add book to group
            group.append(book)
            # update basket_count
            basket[book] -= 1

            if of_four:
                if len(group) == 4:
                    break
            if of_three:
                if len(group) == 3:
                    break

        groups.append(group) 

        # check if dictionary is empty
        if all([v == 0 for v in basket.values()]):
            break
    
    if of_four or of_three:
        for group in groups:
            if len(group) == 1:
                book = group[0]
                for grp in groups:
                    if book not in grp:
                        grp.append(book)
                        groups.remove(group)
                        break
    
            

    return groups

def calculate_total_price(groups) -> int:
    total_price = 0
    # calculate group price
    for group in groups:
        # get discount
        books = len(group)
        disc = SIZE_DISCOUNT[books]

        price = books * 8 * disc 
        total_price += price

    return total_price
    
if __name__ == '__main__':
    print(total([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))