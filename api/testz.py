name = int(input())
n = list(map(int, input().split(" ")))
sum_of_n = int(name*(name+1)/2)

for i in n:
    s = i*(i+1)
    if s>sum_of_n:
        print(i)
        break


# name =input()             # Reading input from STDIN
# a,b = name.split(" ")
# a_factors = []


# print('Hi, %s.' % name)         # Writing output to STDOUT
