def simple_interest(P, R, T):
    return P * R * T / 100

def total_amount(SI,P):
    return SI + P

def main():
    P_str = input("Enter the principal amount in dollars (P): ")
    P = float(P_str.replace('$', ''))
    R = float(input("Enter the annual interest rate (R): "))
    T = float(input("Enter the time in years (T): "))

    
    SI = simple_interest(P, R, T)
    print("Simple Interest = ", SI)
    
    total_amt = total_amount(SI,P)
    print("Therefore, the total is $" + format(total_amt, '.2f'))

if __name__ == "__main__":
    main() 
    
    