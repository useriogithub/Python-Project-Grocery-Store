#Objective: User selects department, food (includes price), adds food to cart different outputs given if price is above or below certain amount, dependent upon budget function
#after, adds food to cart | total amount of items + price = total_shopping_trip(function)


#functions: department, shopping_list, 


def departments(deli, frozen, bakery, produce, meat):
    user_input = ''
    input_message = input('Select a department to shop in')


food_in_deli = {
    {'sliced ham': '8.99'},
    {'cobb salad': '10.00'},
    {'hot and ready chicken': '8.99'},
    {'antipasta': '5.99'},
    {'Rueben sandwich': '4.79'}   
}

food_produce = {
    {'oranges': '1.99'},
    {'red leaf lettuce': '1.89'},
    {'brussell sprouts': '2.99'},
    {'Strawberries': '5.99'}
}

print(len(food_in_deli))

food_in_frozen = {
    
}
food_in_frozen = {'supreme pizza', 'delights frozen lasanga', 'shredded cheese'}

food_in_bakery = {'white bread', 'blueberry muffins', 'Tiramasu', 'Silver Dollar Rolls'}


#def myMapCart():
    #food_in_deli = {'sliced ham', 'cobb salad', 'hot and ready chicken', 'anitpasta','Rueben sandwich'}
    #for i in range(5):
        #items = input("enter the food you would like to buy: ")
        #final_items = map(myMapCart, food_in_deli)

        #print(items)


def checkout():
    pass

    


    
    
    
#list in options need to turn into the list of food items

#if user chooses deli, that goes into the food_in_......list, which then user can select from list



#for index, item in enumerate(Department_options):
    #input_message += f'({index + 1}) {item} \n'



#if user picks certain department, goes to food_in_......" function



#cart function
#if items in cart are above or below a certain level, different outputs are printed
 
 
#if prices in total cart from list are between 40 and 50: return print statment

#my_cart 
#items from food_in..... 
#if prices are below 50: return print("Your total is.  below budget, great job at saving this time!") else: print("your total is 
#  try to stay within budget next time!")