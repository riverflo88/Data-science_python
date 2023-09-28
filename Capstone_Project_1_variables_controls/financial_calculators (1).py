import math
while True:
     try:
          #TAKES USER INPUT FOR THE TYPE OF INVESTMENT INTENDED
          investment_type = (input("""

          investment - to calculate the amount of interest  you'll earn on your principal 
          bond - to calculate the amount you'll have to pay on your loan

          Enter either 'Investment' or 'bond' from the menu above to proceed:


          """)).lower()

          # THIS FUNCTION CALCULATES THE SIMPLE INTEREST
          # THIS FUNCTION IS NOT ACTUALLY NEEDED SINCE THE CALC WAS DONE ONCE IN THE ENTIRE CODE
          def simple_interest(principal,percent_rate,years):
               # RETURNS THE SIMPLE INTEREST AS CALCULATED BELOW
               return principal*(1 + (percent_rate/100) * years)
          
          # THIS FUNCTION CALCULATES THE COMPOUND INTEREST
          def compound(principal,percent_rate,years):
               percent_rate = percent_rate/100
               #RETURNS THE SIMPLE INTEREST AS CALCULATED BELOW
               return principal * math.pow(1 + percent_rate, years)
          
          #THIS FUNCTION CALCULATES THE REPAYMENT AMOUNT
          def repayment(rate,house_val,months):
               rate = (rate/100)/12
               return (rate * house_val)/(1-(1 + rate) **(-months))
          
          investment_type_option= ["investment","bond"]
          if investment_type not in investment_type_option:
               raise Exception() 
          
          # THIS DOES THE CALCULATION FOR  INVESTMENT
          if investment_type == "investment":
               #TAKES IN USERS INPUT FOR CALC. OF INVESTMENT
               inv_amount = int(input("Enter amoount you want to invest: "))
               inv_percent = int(input("Enter desired interest rate: "))
               inv_years= int(input("Number of Years to invest: "))
               # ACCEPTS USER INPUT FOR THE CALC. OF EITHER SIMPLE OR COMPOUND INTEREST
               sim_com = (input("Enter investment method, 'simple' or 'compound': " )).lower()
               if sim_com not in ["simple","compound"]:
                    raise Exception()
                    
                    
               #CALCS. SIMPLE INTEREST
               if sim_com == "simple":
                    print("You will get:$",simple_interest(inv_amount,inv_percent,inv_years))
               #CALCS. COMPOUND INTEREST
               if sim_com == 'compound':
                    print(f"You will get:$ {compound(inv_amount,inv_percent,inv_years)}")
                    #compound(inv_amount,inv_percent,inv_years)

          #ROUTE TO CALC. BOND INVESTMENT        
          if investment_type == "bond":
               present_house_val = int(input("Enter present value of your house: "))
               inv_rate = int(input("Enter  interest rate: "))
               inv_months= int(input("Number of months for repayment: "))
               #PRINTS OUT THE INVESTMENT DONE
               print(f"You will repay $ {repayment(inv_rate,present_house_val,inv_months)} after {inv_months}months")

     except:
          print("Error, incorrect input")