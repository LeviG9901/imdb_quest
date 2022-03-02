

def penalizer(mylist):

    print("Beginning of the penalizer function...")

    # Sorting the given list in descending order
    # Lambda function for sorting this list of dictionaries by the key 'votes'
    mylist.sort(reversed=True, key=lambda i: i['votes'])

    print("End of the penalizer function!")