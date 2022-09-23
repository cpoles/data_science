def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    # create dictionary from keys with unique items
    # therefore all items are keys in the inventory
    inventory = {}.fromkeys(set(items), 0)

    for item in items:
        inventory[item] += 1

    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    if not inventory:
        inventory = create_inventory(items)
        return inventory

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if item in inventory:
            if inventory[item] == 0:
                continue
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    lst_inventory = list(inventory.items())

    return list(filter(lambda x: x[1] != 0, lst_inventory))

