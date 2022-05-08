#This is an extra credit exercise from p.69 in the textbook Q.12
#By: Tonia Alderbashi 

""" The logic I am using is similar to Pascal's triangle.

                                        1
                                    1   3   1
                                1   3   5   3   1
                            1   3   5   7   5   3   1
                        1   3   5   7   9   7   5   3   1
                    1   3   5   7   9   11  9   7   5   3   1

    and so on.

    For each iteration (starting at 0) I looked at the first x numbers, realized
    they were all odd numbers. I wrote a program that returns a list of odds
    between x and 0 in decreasing order. Then took the sum of that list (first
    x odd numbers including 1) with python's inbuilt sum() function.

    Since the pattern is duplicated on the other side I multiplied it by 2.
    the number in the middle is always odd and is 2x + 1, so I added that to
    the sum. 

"""
def odds(x):
    lst = [i for i in range(x,0,-1)]
    lst_odds = []
    for number in lst:
        if number % 2 != 0:
            lst_odds.append(number)
    
    return lst_odds

def neumann(x):
    n = (2 * x) - 1
    lst_to_sum = odds(n)
    lst = sum(lst_to_sum)
    sum_squares = (2 * lst) + 2*x + 1
    return sum_squares


def main():
    print("Consider the algorithm that starts with a single \n"
          "square and on each of its x iterations adds new squares \n"
          "all around the outside. This program calculates the one-by-one \n"
          "squares after x iterations *Note: n starts at 0")
    
    print()
        
    x = int(input("Enter a number x for which you would like to calculate \n"
                  "how many one-by-one squares are there at that itiration: "))
    print(neumann(x), "Total squares.")

main()
                  
