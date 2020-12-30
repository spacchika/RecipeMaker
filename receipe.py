import random as ran
import csv

breakfast_db = open('breakfast.txt', 'r')
lunch_db = open('lunch.txt', 'r')
breakfast_csv = csv.DictReader(breakfast_db)
lunch_csv = csv.DictReader(lunch_db)
breakfast = sorted(breakfast_csv, key=lambda row: row['recipe_calories'])
lunch = sorted(lunch_csv, key=lambda row: row['recipe_calories'])
breakfast_db.close()
lunch_db.close()


def random_number(food_list):
    rand_item = ran.randint(0, len(food_list) - 1)
    return rand_item


def get_breakfast():
    rand_num = random_number(breakfast)
    get_ran_break = breakfast[rand_num]
    return get_ran_break


def get_lunch():
    rand_num = random_number(lunch)
    get_ran_lunch = lunch[rand_num]
    return get_ran_lunch


def food_menu(calorie_limit):
    rand_break = random_number(breakfast)
    rand_lunch = random_number(lunch)
    get_ran_lunch = lunch[rand_lunch]['recipe_calories']
    get_ran_break = breakfast[rand_break]['recipe_calories']
    get_total_calories = int(get_ran_break) + int(get_ran_lunch)
    if int(calorie_limit) >= get_total_calories >= (int(calorie_limit) - 50):
        print("Today's Breakfast {} and calories are {}".format(breakfast[rand_break]['recipe_name'],
                                                                breakfast[rand_break]['recipe_calories']))
        print("Today's Lunch {} and calories are {}".format(lunch[rand_lunch]['recipe_name'],
                                                            lunch[rand_lunch]['recipe_calories']))


if __name__ == "__main__":
    #  max_calories = input("Enter Calorie Limit: ")
    max_calories = 1130
    food_menu(max_calories)
