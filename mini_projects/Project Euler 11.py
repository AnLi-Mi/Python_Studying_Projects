# Project Euler - Problem 11
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the below 20×20 grid?

import time
import numpy as np


# transporting data -> x - columns (0,19) and y - rows (0,19)

y00="08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
y01="49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
y02="81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
y03="52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
y04="22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
y05="24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
y06="32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
y07="67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
y08="24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
y09="21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
y10="78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
y11="16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
y12="86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
y13="19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
y14="04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
y15="88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
y16="04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
y17="20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
y18="20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
y19="01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

# creating a list of rows, so I can loop through them convering elements

matrix = [y00, y01, y02, y03, y04, y05, y06, y07, y08, y09, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19]

# converting strings to lists of strings

for i in range (0,20):
    matrix[i]=list(matrix[i].split(' '))

# converting strings to int

for lista in matrix:
    for i in range (0,20):
        lista[i]=int(lista[i])

start1 = time.time()

# converting the list of lists to a 2D NumPy Array

arr = np.array(matrix)

# prepating an empty list to fill it out with products
product1 = []
 
#horizontal  - (x in range (0,17), y in range (0,20))


for y in range (0, 20):
    for x in range (0,17):
        result =(arr[y, x] * arr [y, x+1] * arr[y, x+2] * arr[y, x+3])
        result=int(result)
        product1.append(result)


#vertical - (x in range (0,20), y in range (0, 17))

for x in range (0,20):
   for y in range (0,17):
       result=(arr[y, x] * arr[y+1, x] * arr[y+2, x] * arr[y+3, x])
       result=int(result)
       product1.append(result)

# diagonal down left (up right)

for y in range (0,17):
    for x in range (0,17):
         result=(arr[y, x] * arr[y+1, x+1] * arr[y+2, x+2] * arr[y+3, x+3])
         result=int(result)
         product1.append(result)

# diagonal down right (up left)

for y in range (19,2, -1):
    for x in range (16,-1, -1):
         result=(arr[y, x] * arr[y-1, x+1] * arr[y-2, x+2] * arr[y-3, x+3])
         result=int(result)
         product1.append(result)
        

print(max(product1))
end1 = time.time()
print(round(end1-start1 ,10))







