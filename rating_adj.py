

def penalizer(mylist):

    print("Beginning of the penalizer function...")

    # Sorting the given list in descending order
    # Lambda function for sorting this list of dictionaries by the key 'votes'
    mylist.sort(reverse=True, key=lambda i: i['votes'])

    # Making for loop to iterate through the list
    for index in range(len(mylist)):

        # This if needs for missing the first element of the list
        # Because the first element is the benchmark
        if index != 0:
            # Calculating the vote number difference between the first and indexed movie
            # Round the diff number
            diff = round((mylist[0]['votes'] - mylist[index]['votes'])/1000000)

            # Penalty variable for multiplying the diff with 0.1
            penalty = round(diff * 0.1, 1)

            # Changing original movie rating based on the gained penalty score
            mylist[index]['rating'] -= penalty
            # Rounding up the rating
            mylist[index]['rating'] = round(mylist[index]['rating'], 1)
            print(mylist[index]['rating'])

    print("End of the penalizer function!")
    return mylist
