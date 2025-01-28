# 1
A = True
B = False
C = False
num_a = A or B # T or F -> T
num_b = A and B # T and F -> F
num_c = B or C # F or F -> F
print(num_a, num_b, num_c)

# 2
A = True
B = False
C = False
num_a = not(A) and B # not(T) and F -> F
num_b = A or not(B) # T or not(F) -> T
num_c = A and B or C # T and F or F -> F
print(num_a, num_b, num_c)

# 3
A = True
B = False
C = False
num_a = A or B and not(C) # T or F and not(F) -> T
num_b = A and not(B) or C # T and not(F) or F -> T
num_c = not(A) and not(B) # not(T) and not(F) -> F
num_d = A and (not(B) or C) # T and (not(F) or F) -> T !!!
num_e = not(A and C) or B # not(T and F) or F -> T
num_f = A or (not(B and C)) # T or (not(F and F) -> T
print(num_a, num_b, num_c, num_d, num_e, num_f)

# 4
X = False
Y = False
Z = True
num_a = X or Y and not(Z) # F or F and not(T) -> F
num_b = X and not Y or Z # F and not F or T -> T
num_c = not(X) and not(Y) # not(F) and not(F) -> T
num_d = X and (not(Y) or Z) # F and (not(F) or T) -> F
num_e = not(X and Z) or Y # not(F and T) or F -> T
num_f = X or (not(Y or Z)) # F or (not(F or T)) -> F
print(num_a, num_b, num_c, num_d, num_e, num_f)

# 5
A = True
B = False
C = False
num_a = A or not(A and B) or C # T or not(T and F) or F -> T
num_b = not(A) or A and (B or C) # not(T) or T and (F or F) -> F !!!
num_c = (A or B and not(C)) and C # (T or F and not(F)) and F -> F
print(num_a, num_b, num_c)

# 6
A = False
B = False
C = True
num_a = (not(A) or not(B)) and not(C) # (not(F) or not(F)) and not(T) -> F
num_b = (not(A) or not(B)) and (A or B) # (not(F) or not(F)) and (F or F) -> F
num_c = A and B or A and C or not(C) # F and F or F and T or not(T) -> F
print(num_a, num_b, num_c)

# 8
A = True
B = True
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B and not(C)) #-> T
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = True
C = True
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B and not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = False
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B and not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = False
C = False
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B and not(C)) #-> F
num_c = not(not(A) or B and C) #-> (!T) F
print(num_a, num_b, num_c)
A = True
B = False
C = False
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B and not(C)) #-> T
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = True
B = True
C = False
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B and not(C)) #-> F
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = True
B = False
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B and not(C)) #-> T
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = False
B = True
C = False
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B and not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)

# 9
A = True
B = True
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = False
B = True
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = False
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = False
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = True
B = False
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = True
B = True
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = True
B = False
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = True
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)

# 10
x = 1
y = -1
num1 = x**2 - y**2 <= 0 # 1 - 1 = 0 -> T
print(num1)
x = 2
y = -2
num2 = (x >= 2) or (y**2 != 4) # T or F -> T
print(num2)
x = 2
y = 2
num3 = (x >= 0) and (y**2 > 4) # T and F -> F
print(num3)
x = 1
y = 2
num4 = (x * y != 4) and (y > x) # T and T -> T
print(num4)
x = 2
y = 1
num5 = (x * y != 0) or (y < x) # T or T -> T
print(num5)
x = 1
y = 2
num6 = (not(x * y < 1)) and (y > x) # T and T -> T
print(num6)
x = 2
y = 1
num7 = (not(x * y < 0)) or (y > x) # T or F -> T
print(num7)

# 11
A = True
B = True
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = True
C = True
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = False
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = False
B = False
C = False
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)
A = True
B = False
C = False
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = True
B = True
C = False
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = True
B = False
C = True
num_a = not(A or not(B) and C) #-> F
num_b = A and not(B or not(C)) #-> T
num_c = not(not(A) or B and C) #-> T
print(num_a, num_b, num_c)
A = False
B = True
C = False
num_a = not(A or not(B) and C) #-> T
num_b = A and not(B or not(C)) #-> F
num_c = not(not(A) or B and C) #-> F
print(num_a, num_b, num_c)

# 12
X = True
Y = True
Z = True
num_a = not(X or not(Y) and Z) #-> F
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> F
print(num_a, num_b, num_c)
X = False
Y = True
Z = True
num_a = not(X or not(Y) and Z) #-> T
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> F
print(num_a, num_b, num_c)
X = False
Y = False
Z = True
num_a = not(X or not(Y) and Z) #-> F
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> F
print(num_a, num_b, num_c)
X = False
Y = False
Z = False
num_a = not(X or not(Y) and Z) #-> T
num_b = Y or (X and not(Y) or Z) #-> F
num_c = not(not(X) and Y or Z) #-> T
print(num_a, num_b, num_c)
X = True
Y = False
Z = False
num_a = not(X or not(Y) and Z) #-> F
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> T
print(num_a, num_b, num_c)
X = True
Y = True
Z = False
num_a = not(X or not(Y) and Z) #-> F
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> T
print(num_a, num_b, num_c)
X = True
Y = False
Z = True
num_a = not(X or not(Y) and Z) #-> F
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> F
print(num_a, num_b, num_c)
X = False
Y = True
Z = False
num_a = not(X or not(Y) and Z) #-> T
num_b = Y or (X and not(Y) or Z) #-> T
num_c = not(not(X) and Y or Z) #-> F
print(num_a, num_b, num_c)

# 13
A = True
B = True
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = False
B = True
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = False
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = False
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = True
B = False
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = True
B = True
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)
A = True
B = False
C = True
num_a = not(A and B) and (not(A) or not(C)) #-> F
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> T
print(num_a, num_b, num_c)
A = False
B = True
C = False
num_a = not(A and B) and (not(A) or not(C)) #-> T
num_b = not(A and not(B)) or (A or not(C)) #-> T
num_c = A and not(B) or not(A or not(C)) #-> F
print(num_a, num_b, num_c)

# 3.15
A = int(input("Введите значение А: "))
B = int(input("Введите значение В: "))
C = int(input("Введите значение C: "))
num_a = A > 100 and B > 100
num_b = (A % 2 == 0 and B % 2 != 0) or (A % 2 != 0 and B % 2 == 0)
num_c = A > 0 or B > 0
num_d = A % 3 == 0 and B % 3 == 0 and C % 3 == 0
num_e = (A < 50 and B > 50 and C > 50) or (A > 50 and B < 50 and C > 50) or (A > 50 and B > 50 and C < 50)
num_f = A < 0 or B < 0 or C < 0
print(num_a, num_b, num_c, num_d, num_e, num_f)

# 3.16
X = int(input("Введите значение X: "))
Y = int(input("Введите значение Y: "))
Z = int(input("Введите значение Z: "))
num_a = X % 2 != 0 and Y % 2 != 0
num_b = (X > 20 and Y < 20) or (X < 20 and Y > 20)
num_c = X == 0 or Y == 0
num_d = X < 0 and Y < 0 and Z < 0
num_e = (X % 5 == 0 and Y % 5 != 0 and Z % 5 != 0) or (X % 5 != 0 and Y % 5 == 0 and Z % 5 != 0) or (X % 5 != 0 and Y % 5 != 0 and Z % 5 == 0)
num_f = X > 100 or Y > 100 or Z > 100
print(num_a, num_b, num_c, num_d, num_e, num_f)

# 3.30
A = int(input("Введите значение А: "))
num_a = int(A % 2 == 0 or A % 3 == 0) == True
num_b = int(A % 3 != 0 and A % 10 == 0) == True
print(num_a, num_b)

# 3.31
N = int(input("Введите значение N: "))
num_a = int(N % 5 == 0 or N % 7 == 0) == True
num_b = int(N % 4 == 0 and N % 10 != 0) == True
print(num_a, num_b)