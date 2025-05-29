class Online_store:  
    Products = {}  
    Users = []  
    
    def __init__(self, username, password):  
        self.admin_username = username  
        self.admin_password = password  

    def new_product(self, product, price_goods, number_goods):  
        username = input('Enter your username: ')  
        password = input('Enter your password: ')  
        if username == self.admin_username and password == self.admin_password:  
            self.Products[product] = (price_goods, number_goods)  
            print(f"Product '{product}' added to store.")  
        else:  
            print('The information is invalid.')  

    def product_removal(self, product):  
        username = input('Enter your username: ')  
        password = input('Enter your password: ')  
        if username == self.admin_username and password == self.admin_password:  
            if product in self.Products:  
                del self.Products[product]  
                print(f"Product '{product}' removed from store.")  
            else:  
                print("Product does not exist.")  
        else:  
            print('The information is invalid.')  

    def user_registration(self, name, family, email):  
        if email.endswith('@gmail.com'):  
            full_name = name + ' ' + family  
            self.Users.append(full_name)  
            print(f"User '{full_name}' registered successfully.")  
        else:  
            print('The information is invalid.')  

    def user_purchases(self):  
        full_name = input('Name and surname: ')  
        if full_name in self.Users: 
            products_to_buy = []  
            while True:  
                product = input('Enter product to purchase (or type "done" to finish): ')  
                if product.lower() == "done":  
                    break  
                if product in self.Products:  
                    quantity = int(input(f'Enter quantity for {product}: '))  
                    if quantity <= self.Products[product][1]:  
                        total_price = quantity * self.Products[product][0]  
                        print(f'Total price for {quantity} {product}(s): {total_price} currency units')  
                        confirm = input('Do you want to place the order? (yes/no): ')  
                        if confirm.lower() == 'yes':  
                            print('Your order has been successfully placed!')   
                            self.Products[product] = (self.Products[product][0], self.Products[product][1] - quantity)  
                        else:  
                            print('Order has not been placed.')  
                    else:  
                        print('Not enough stock available.')  
                else:  
                    print('This product does not exist')  
        else:  
            print('The information is invalid')  

store1 = Online_store("admin1", "password123")  
 
store1.new_product("pencil", 100, 50)  
store1.new_product("apple", 150, 30)  
store1.new_product("phone", 200, 100)  
 
store1.user_registration("Ali", "Mohammadi", "ali@gmail.com")  
store1.user_registration("Sara", "Karimi", "sara@gmail.com")  

print("Products in store:", store1.Products)  

store1.user_purchases()