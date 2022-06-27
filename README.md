"# fetch_backend_take_home" 

transaction_list should be a list of dictionaries, where each dictionary has the the follwing schema
    {'payer': str, 'points': int, 'timestamp': str}

spent_points is just a single dictionary with the above schema

I have a switch to determine the type of report requested. 