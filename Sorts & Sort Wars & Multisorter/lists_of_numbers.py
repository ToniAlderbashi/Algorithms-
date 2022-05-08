import random

lst_100 = [i for i in range(1, 101)]

lst_200 = [i for i in range(1, 201)]

lst_300 = [i for i in range(1, 301)]

lst_400 = [i for i in range(1, 401)]

lst_500 = [i for i in range(1, 501)]

#inverse

lst_100_inv = lst_100[::-1]

lst_200_inv = lst_200[::-1]

lst_300_inv = lst_300[::-1]

lst_400_inv = lst_400[::-1]

lst_500_inv = lst_500[::-1]

#random 1 with 0s

def add_one():
    
    lst_100_1 = [0 for i in range(1, 101)]

    position_one = random.randrange(0,100)

    lst_100_1[position_one] = 1


    return (lst_100_1)

add_one()


#random 1 with 0s 75-100

def add_one_last():
    
    lst_100_1 = [0 for i in range(1, 501)]

    position_one = random.randrange(475,500)

    lst_100_1[position_one] = 1


    return (lst_100_1)

add_one_last()

#random 1 with 0s 0-25

def add_one_first():
    
    lst_100_1 = [0 for i in range(1, 501)]

    position_one = random.randrange(0,25)

    lst_100_1[position_one] = 1


    return (lst_100_1)

add_one_first()

