def ground_shipping_cost(weight):
  if weight<=2:
    return weight*1.5 + 20
  elif weight>2 and weight<=6:
    return weight*3+20
  elif weight>6 and weight<=10:
    return weight*4+20
  elif weight>10:
    return weight*4.75+20
print(ground_shipping_cost(8.4))
premium_ground_shipping = 125

def drone_shipping_price(weight):
  if weight<=2:
    return weight*4.5
  elif weight>2 and weight<=6:
    return weight*9
  elif weight>6 and weight<=10:
    return weight*12
  elif weight>10:
    return weight*14.25 
print(drone_shipping_price(1.5))

def cheapest_cost(weight):
  ground=ground_shipping_cost(weight)
  drone=drone_shipping_price(weight)
  premium=premium_ground_shipping
  if ground<drone and ground<premium:
    print("The cheapest is ground shipping")
    print("the cost is "+str(ground))
  elif drone<ground and drone<premium:
    print("The cheapest is drone shipping")
    print("the cost is "+str(drone))
  elif premium<ground and premium<drone:
    print("The cheapest is premium shipping")
    print("the cost is "+str(premium))
cheapest_cost(4.8)