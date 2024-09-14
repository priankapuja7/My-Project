# """Condition type 1"""
# Animal = input("Animal: ")
# Name = "purba" if Animal=="Cow" else "Purbar Future Husband"
# print(Name)
#
# """Condition type 2"""
# Cow = input("Animal: ")
# print ("purba") if Animal == "Cow" else print ("Purbar Future Husband")
#
# """Condition Rules
# and : TT=T, TF=F, FT=F, FF=F
# Or : TT=T, TF=T, FT=T, FF=F"""
#
# """Condition Type 3"""
# sales1 = int(input("2020 : "))
# sales2 = int(input("2021 : "))
# if(sales1 < sales2):
#     print("growth")
# elif(sales2 < sales1):
#     print("downfall")
# else:
#     print("NI")
#
# """Condition Type 4"""
# age= int(input("age : "))
# Vote= ("yes", "no") [age<18]
# print(Vote)
#
# """Condition Type 3"""
# Salary = float(input("salary: "))
# tax = Salary*(0.1, 0.2) [Salary>50000]
# print(tax)
#
# """Practice 1:
# # Q: User want to identify that the number is even odd or zero"""
#
# num1= int(input("number: "))
# num2= int(2)
# Analysis= num1%num2
# print(Analysis)
#
# """East Tec: num1%2"""
# num3= 0
# if(num1==0):
#     print("Zero")
# elif(Analysis == 0):
#     print("even")
# else:
#     print("odd")
#
# '''To make comment easy way to comment and remove comment is after selection press ctrl+/'''


# """Projects with Conditioners"""
# var= "Double Scheme FDR Analysis"
# print(var)
# Investment=input("Investment Amount: ")
# print(Investment)
# investment amount1 = (Investment >= 100000)
# investment amount2= (Investment >= 50000)
# investment amount3= (Investment >= 10000)
# if(Investment == investment amount1):
#     print ("Modhumoti Bank: i= 12.25%, n= 6 years  \n "
#            "National Bank: i= 11.25 %, n= 6 years 5 months \n")
# elif(Investment == investment amount2):
#     print("Global Islami Bank: i= 10.41%, n= 7 years \n"
#           "One Bank: i= 9.68%, n= 7 years 5 months \n"
#           "City Bank: i= 9.42%, n= 7 years 7 months \n"
#           "AB Bank: i= 9.29%, n= 7 years 8 months\n"
#           "Bank Asia: i= 8.01%, n= 9 years\n"
#           "NCC Bank: i= 7.41%, n= 9 years 7 months\n"
#           "Dhaka Bank: i= 7.18%, n= 10 years\n"
#           "Prime Bank: i= 7.18%, n= 10 years\n"
#           "Mutual Trust Bank: i= 6.96 %, n= 10 years 3 months\n")
# elif(Investment == investment amount3):
#     print("NRB Commercial Bank: i= 11.07%, n= 6 years 6 months")
# else:
#     print("N/A")

"""Projects with Conditioners"""
var= "Double Scheme FDR Analysis"
print(var)
Investment=input("Investment Amount: ")

if(not Investment <= 99999):
    print ("Modhumoti Bank: i= 12.25%, n= 6 years  \n "
           "National Bank: i= 11.25 %, n= 6 years 5 months \n")
elif(Investment <= 49999):
    print("Global Islami Bank: i= 10.41%, n= 7 years \n"
          "One Bank: i= 9.68%, n= 7 years 5 months \n"
          "City Bank: i= 9.42%, n= 7 years 7 months \n"
          "AB Bank: i= 9.29%, n= 7 years 8 months\n"
          "Bank Asia: i= 8.01%, n= 9 years\n"
          "NCC Bank: i= 7.41%, n= 9 years 7 months\n"
          "Dhaka Bank: i= 7.18%, n= 10 years\n"
          "Prime Bank: i= 7.18%, n= 10 years\n"
          "Mutual Trust Bank: i= 6.96 %, n= 10 years 3 months\n")
elif(Investment > 9999):
    print("NRB Commercial Bank: i= 11.07%, n= 6 years 6 months")
else:
    print("N/A")
print(Investment)
