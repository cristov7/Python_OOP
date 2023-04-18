from project.managing_app import ManagingApp


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506' ))
print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user('Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())


# Tisha Reenie was successfully registered under DLN-7246506
# Bernard Remy was successfully registered under DLN-CDYHVSR68661
# 7246506 has already been registered to our platform.
# Chevrolet Volt was successfully uploaded with LPN-CWP8032.
# Volkswagen e-Up! was successfully uploaded with LPN-COUN199728.
# Mercedes-Benz EQS was successfully uploaded with LPN-5UNM315.
# Ford e-Transit was successfully uploaded with LPN-726QOA.
# BrightDrop Zevo400 was successfully uploaded with LPN-SC39690.
# Vehicle type EcoTruck is inaccessible.
# 726QOA belongs to another vehicle.
# SOF/PLD - 144 km is unlocked and available to use.
# BUR/VAR - 87 km is unlocked and available to use.
# BUR/VAR - 87 km had already been added to our platform.
# SOF/PLD shorter route had already been added to our platform.
# BUR/VAR - 86.999 km is unlocked and available to use.
# Mercedes-Benz EQS License plate: 5UNM315 Battery: 81% Status: OK
# Chevrolet Volt License plate: CWP8032 Battery: 68% Status: Damaged
# User 7246506 is blocked in the platform! This trip is not allowed.
# Vehicle CWP8032 is damaged! This trip is not allowed.
# Route 2 is locked! This trip is not allowed.
# 1 vehicles were successfully repaired!
# 0 vehicles were successfully repaired!
# *** E-Drive-Rent ***
# Bernard Remy Driving license: CDYHVSR68661 Rating: 0.5
# Tisha Reenie Driving license: 7246506 Rating: 0
