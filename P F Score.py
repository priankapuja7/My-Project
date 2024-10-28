
# Collecting financial data from user input
a = float(input("Net Income of Current Year: "))
b = float(input("Total Asset of Current Year: "))
c = float(input("Cash flow from operation: "))
d = float(input("Net Income of Previous Year: "))
e = float(input("Total Asset of Previous Year: "))
f = float(input("Long Term Debt of Current Year: "))
g = float(input("Long Term Debt of Previous Year: "))
h = float(input("Current Asset of Current Year: "))
i = float(input("Current Asset of Previous Year: "))
j = float(input("Current Liability of Current Year: "))
k = float(input("Current Liability of Previous Year: "))
l = float(input("Sales of Current Year: "))
m = float(input("Sales of Previous Year: "))
n = float(input("Gross profit of Current Year: "))
o = float(input("Gross profit of Previous Year: "))
p = float(input("No of shares declared in Current Year: "))

# Calculating financial metrics
ROA = (a / b) * 100
CFO = (c / b) * 100
DROA = (d / e) * 100
Dfina = ROA - DROA
DLEV11 = (f - g) / ((b + e) / 2)
CR1 = h - j
CR2 = i - k
DLC0 = CR1 - CR2
GR1 = n / l
GR2 = o / m
DG0 = GR1 - GR2
AT1 = l / ((b + e) / 2)
AT2 = m / ((b + e) / 2)
DTUE1 = AT1 - AT2

# Printing calculated metrics
print(f"ROA OF CURRENT YEAR = {ROA:.2f}%")
print(f"CFO = {CFO:.2f}%")
print(f"D(ROA) = {Dfina:.2f}%")
print(f"D(Leverage) = {DLEV11:.2f}")
print(f"D(Liquidity) = {DLC0:.2f}")
print(f"D(Gross Margin) = {DG0:.2f}")
print(f"D(Turnover) = {DTUE1:.2f}")

# Evaluating financial health based on calculated metrics
points = [
    ROA >= 0,
    CFO >= 0,
    CFO >= ROA,
    Dfina >= 0,
    DLEV11 >= 0,
    p >= 0,
    DLC0 >= 0,
    DG0 >= 0,
    DTUE1 >= 0,
]

# Print point results
for i, point in enumerate(points):
    print(f"POINT {1 if point else 0}")

# Calculate total points
Total = sum(points)
print(Total)

# Determine company performance
if Total in {0, 1, 2, 3}:
    print("The company is experiencing financial challenges or operational issues.")
elif Total in {4, 5, 6}:
    print("The company's performance is mixed; further investigation may be necessary.")
elif Total in {7, 8, 9}:
    print("Indicates strong financial health and operational efficiency of the company.")
else:
    print("error")