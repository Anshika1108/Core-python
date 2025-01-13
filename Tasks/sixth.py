#Simple interest
P = int(input('Principle amount = '))
R = int(input('Rate of interest = '))
T = int(input('Time duration in year = '))
def SI(Principle = P, Rate = R, Time = T):
    return P*R*T/100
print(SI())

