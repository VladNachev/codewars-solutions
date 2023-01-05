def human_years_cat_years_dog_years(human_years):
    years_array = []
    cat = 0
    dog = 0
    if human_years == 0:
        pass
    elif human_years == 1:
        cat = 15
        dog = 15
    elif human_years == 2:
        cat = 24
        dog = 24
    else:
        cat = 24 + ((human_years - 2) * 4)
        dog = 24 + ((human_years - 2) * 5)
    years_array = [human_years, cat, dog]
    return years_array