from project.christmas_pastry_shop_app import ChristmasPastryShopApp


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())


# Added delicacy Gingy - Gingerbread to the pastry shop.
# Gingerbread Gingy: 200g - 5.20lv.
# Added booth number 1 in the pastry shop.
# Added booth number 10 in the pastry shop.
# Booth 1 has been reserved for 30 people.
# Booth 1 ordered Gingy.
# Booth 1:
# Bill: 80.20lv.
# Booth 1 has been reserved for 5 people.
# Booth 1 ordered Gingy.
# Booth 1 ordered Gingy.
# Booth 1 ordered Gingy.
# Booth 1:
# Bill: 28.10lv.
# Income: 108.30lv.
