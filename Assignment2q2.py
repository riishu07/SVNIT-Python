product_dict = {}
while True:
    product_name = input("Enter product name (type done to quit) : ")
    if product_name =='done':
        break
    price = float(input("enter product price : Rs."))
    product_dict[product_name]= price
    
while True:
    search_product = input("Enter the product name to obtain its details (type exit to quit): ")
    if search_product == 'exit':  
            print("Exiting the program...")  
            break  
    if search_product in product_dict: 
            print(f"The price of {search_product} is: Rs{product_dict[search_product]:.2f}")  
    else:  
            print(f"{search_product} is not in the product list.")  
