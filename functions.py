def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        print("apply the discount")
        
    else:
        return("original price")
    
    
price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the discount percentage:"))
discount =((price * discount_percent)/100) 
final_price =(price - discount)
print("final price")
    
    
    
    