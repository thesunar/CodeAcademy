#Ground Shipping
weight = 4.8
cost_ground_premium = 125.00


if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20.00
elif weight > 10:
  cost_ground = weight * 4.75 + 20.00

print("Your Cost For Ground : ", cost_ground)
print("For Ground Premium Member : ", cost_ground + cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50 + 0.00
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.0 + 0.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.0 + 0.00
elif weight > 10:
  cost_drone = weight * 14.25 + 0.00

print("Your Cost For Drone : ", cost_drone)
