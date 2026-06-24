p = int(input("Principal = "))
apr = float(input("APR = "))
n = float(input("year = "))
money = p * (1 + apr) ** n
print("Total principal and interest:", money)
