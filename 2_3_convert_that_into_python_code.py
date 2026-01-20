def fill_kettle():
    pass


def plug_in_kettle():
    pass


def boil_water():
    pass


def wash_cup():
    pass


def add_to_cup(item):
    pass


def pour(item, into):
    pass


def stir(container):
    pass


def serve_chai():
    pass


def make_chai():

    kettle_has_water = False
    cup_is_clean = True

    if not kettle_has_water:
        fill_kettle()

    plug_in_kettle()
    boil_water()

    if not cup_is_clean:
        wash_cup()

    add_to_cup("tea leaves")
    add_to_cup("sugar")

    pour("boiled water", into="cup")
    stir("cup")

    serve_chai()


make_chai()