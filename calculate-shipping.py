premium_ground = 125


def ground_cost(weight):
    if (weight <= 2.0):
        return(1.50 * weight + 20)
    elif (weight > 2.0) and (weight <= 6.0):
        return(3 * weight + 20)
    elif (weight > 6.0) and (weight <= 10.0):
        return(4 * weight + 20)
    else:
        return(4.75 * weight + 20)


print(ground_cost(8.4))


def drone_cost(weight):
    if (weight <= 2.0):
        return(4.50 * weight)
    elif (weight > 2.0) and (weight <= 6.0):
        return(9 * weight)
    elif (weight > 6.0) and (weight <= 10.0):
        return(12 * weight)
    else:
        return(14.25)


print(drone_cost(1.5))


def best_shipping(weight):
    ground = ground_cost(weight)
    premium = premium_ground
    drone = drone_cost(weight)

    if ground < drone and ground < premium:
        print("Ground Shipping is cheapest and will cost " +
              str(ground) + " dollars.")
    elif (drone) < (ground) and (drone) < (premium):
        print("Drone Shipping is cheapest and will cost " +
              str(drone) + " dollars.")
    else:
        print("Premium Ground Shipping is cheapest and will cost " +
              str(premium) + " dollars.")


best_shipping(17)
