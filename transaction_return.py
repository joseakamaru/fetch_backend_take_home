
def transaction_return(transaction_list: list , spent_points: int, point_balance=False):
    # transaction_list should be a list of dictionaries with the follwing schema
    # {'payer': str, 'points': int, 'timestamp': str}
    
    # define variables:
    position_transaction_list = 0
    payer_list = list()
    cost2payer_list = list()
    count_switch = True
    balance_report = {}
    cost_report = {}


    # Get the value of the points spent
    points2subtract = spent_points['points']


    # Sort the list of dictionaries base on the timestamp. 
    sorted_transaction_list = sorted(transaction_list, key=lambda d: d['timestamp'])

    # while loop. Breaks when the position reaches the end of the list.
    while position_transaction_list < len(transaction_list):

        # Get a dictionary from the list
        dictionary_element = sorted_transaction_list[position_transaction_list]
        
        # Get the current points in the pull dictionary
        points = dictionary_element['points']

        # If we still have points proceed intot the if statement.
        if count_switch == True:
            # If the points are less then the amount spent, return zero to the current dictionary  
            #  balanace. Otherwise, subtract the remainding points and return the difference. 
            if points <= points2subtract:
                points2subtract = points2subtract - points
                dictionary_element['points'] = 0
                cost2payer_list.append({'payer': dictionary_element['payer'], 'points':-points})
            else:
                points = points - points2subtract
                dictionary_element['points'] = points
                count_switch = False
                cost2payer_list.append({'payer': dictionary_element['payer'], 'points':-points2subtract})
        
        # Position Tracker
        position_transaction_list = position_transaction_list + 1

        # Creates a list of all unique payers
        if dictionary_element['payer'] not in payer_list:
            payer_list.append(dictionary_element['payer'])


    # Iterate throught  the unique payer list.
    for payer in payer_list:

        # create a list of all dictionaries with a specific payer
        payer_history = [element for element in sorted_transaction_list if element['payer'] == payer]

        payer_history_Cost =  [element for element in cost2payer_list if element['payer'] == payer]

        # Add the payer and the current sum balance to the report field
        balance_report[payer] = sum(item['points'] for item in payer_history)

        cost_report[payer] = sum(item['points'] for item in payer_history_Cost)


    # Switch to determine the report requested.
    if point_balance == True:
        return balance_report
    else:
        return cost_report
    