from project.product import Product
from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.cold_beverage import ColdBeverage
from project.beverage.hot_beverage import HotBeverage
from project.beverage.tea import Tea
from project.food.cake import Cake
from project.food.dessert import Dessert
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.salmon import Salmon
from project.food.soup import Soup
from project.food.starter import Starter


product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
