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
    """Returns a list of names of the spicy foods."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of spicy foods with a heat level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Prints each spicy food with its name, cuisine, and heat level."""
    for food in spicy_foods:
        heat_level_str = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns a spicy food dictionary that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no match found

def print_spiciest_foods(spicy_foods):
    """Prints spicy foods with a heat level greater than 5."""
    spicy_foods_above_5 = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_foods_above_5)

def get_average_heat_level(spicy_foods):
    """Returns the average heat level of the spicy foods."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Integer division for average

def create_spicy_food(spicy_foods, spicy_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(spicy_food)
    return spicy_foods
