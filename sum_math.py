#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/Apr29/2021
# This program calculates the sum of two numbers


def main():
    # this function calculates the sum of two numbers
    print("This program adds 2 numbers together!")

    # input
    first_number = int(input("please enter the first number:"))
    second_number = int(input("please enter the second number:"))

    # process
    sum_number = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, sum_number))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
