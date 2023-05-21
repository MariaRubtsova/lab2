def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.cuisine_type = cuisine_type
            self.restaurant_name = restaurant_name

        def describe_restaurant(self):
            print(f'Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

    newRestaurant = Restaurant('Kabachoc', 'italian')
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.cuisine_type = cuisine_type
            self.restaurant_name = restaurant_name

        def describe_restaurant(self):
            print(f'Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

    newRestaurant1 = Restaurant('Kabachoc', 'italian')
    print(newRestaurant1.restaurant_name)
    print(newRestaurant1.cuisine_type)

    newRestaurant2 = Restaurant('Ukrop', 'italian')
    print(newRestaurant2.restaurant_name)
    print(newRestaurant2.cuisine_type)

    newRestaurant3 = Restaurant('Kapusta', 'italian')
    print(newRestaurant3.restaurant_name)
    print(newRestaurant3.cuisine_type)

    newRestaurant1.describe_restaurant()
    newRestaurant1.open_restaurant()

    newRestaurant2.describe_restaurant()
    newRestaurant2.open_restaurant()

    newRestaurant3.describe_restaurant()
    newRestaurant3.open_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.cuisine_type = cuisine_type
            self.restaurant_name = restaurant_name
            self.rating = rating


        def describe_restaurant(self):
            print(f'Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type}')

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

        def rating_restaurant(self):
            print(f'рейтинг год назад: 3')

        def update_rating(self):
            print(f'новый рейтинг: {self.rating}')

    a = int(input("оцените ресторан:"))



    newRestaurant = Restaurant('Kabachoc', 'italian', a)
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)


    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    newRestaurant.rating_restaurant()
    newRestaurant.update_rating()

z3()