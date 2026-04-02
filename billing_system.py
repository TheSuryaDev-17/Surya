print("--- SEHI Billing ---")
item = input("Saman: ")
price = float(input("Rate: "))
qty = float(input("Vajan: "))
total = price * qty
print("Total Bill: Rs.", total)
while True:
    print("\n--- SEHI Billing System ---")
    item = input("Saman (ya 'exit' likhein band karne ke liye): ")
    
    if item.lower() == 'exit':
        print("Business Tool band ho raha hai. Bye!")
        break
        
    price = float(input("Rate: "))
    qty = float(input("Vajan: "))
    
total = price * qty
    print(f"Billa for {item}: Rs. {total}")