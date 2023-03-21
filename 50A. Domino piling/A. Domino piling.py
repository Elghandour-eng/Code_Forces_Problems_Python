""""
A. Domino piling
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

Input
In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).

Output
Output one number — the maximal number of dominoes, which can be placed.
"""


#Author: Abdelwahaab Elghandour
#Date: 2023-03-21
#Problem Link: https://codeforces.com/problemset/problem/50/A


# Code
def get_input():
    #"Please enter the number of rows: " "Please enter the number of columns: "
    m,n = input()
# check if the input is a number
    if m.isdigit() and n.isdigit():
        m=int(m)
        n=int(n)
    else:
        print("Invalid input \n please enter a number")
        exit() 
    return m,n


def compute_max_dominoes(m,n):
    return (m*n)//2

# main
if __name__ == "__main__":
    m,n=get_input()
    print(compute_max_dominoes(m,n))
    


     


        
       