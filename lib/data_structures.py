spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [x.get('name') for x in spicy_foods]
    return names

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [x for x in spicy_foods if x.get('heat_level') > 5]
    return spiciest_foods

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
     for x in spicy_foods:
        emoji = "🌶"
        print(f'{x.get("name")} ({x.get("cuisine")}) | Heat Level: {emoji * x.get("heat_level")}' )

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        food_cuisine = x.get('cuisine','did not find the cuisine')
        if food_cuisine == cuisine:
            dict = x
    return dict

get_spicy_food_by_cuisine(spicy_foods, 'American')

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        heat_level = food.get('heat_level',0)
        total += heat_level
    av = int(total / len(spicy_foods))
    return av
             
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    gen_new_spicy_foods = (x for x in spicy_foods)
    new_spicy_foods = list(gen_new_spicy_foods)
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

create_spicy_food(spicy_foods, spicy_food)
