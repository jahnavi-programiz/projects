'''FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.
A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
Distance in kms                     Delivery charge in Rs per km
For first 3kms                                  0
For next 3kms                                   3
For the remaining                               6
Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer. 
The below information must be used to check the validity of the data provided by the customer: 
Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.
Distance in kms must be greater than 0.
Quantity ordered should be minimum 1.
If any of the input is invalid, the bill amount should be considered as -1.'''
#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)






'''def calculate_bill(food_type, quantity, distance):
    # Validate inputs
    if food_type not in ['V', 'N'] or quantity < 1 or distance <= 0:
        return -1
    
    # Set the cost per plate based on food type
    if food_type == 'V':
        cost_per_plate = 120
    else:
        cost_per_plate = 150
    
    # Calculate the food cost
    food_cost = cost_per_plate * quantity
    
    # Calculate the delivery charge
    if distance <= 3:
        delivery_charge = 0
    elif distance <= 6:
        delivery_charge = (distance - 3) * 3
    else:
        delivery_charge = (3 * 3) + ((distance - 6) * 6)
    
    # Calculate the final bill amount
    final_bill = food_cost + delivery_charge
    
    return final_bill

# Example usage
food_type = 'N'  # 'V' for vegetarian, 'N' for non-vegetarian
quantity = 2
distance = 8

bill_amount = calculate_bill(food_type, quantity, distance)
print(f"The final bill amount is: Rs.{bill_amount}")
'''