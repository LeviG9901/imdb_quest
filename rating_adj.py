

def penalizer(mylist):

    print("Beginning of the penalizer() function...")

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
            diff = round((mylist[0]['votes'] - mylist[index]['votes'])/100000)

            # Penalty variable for multiplying the diff with 0.1
            penalty = round(diff * 0.1, 1)

            # Changing original movie rating based on the gained penalty score
            mylist[index]['rating'] -= penalty
            # Rounding up the rating
            mylist[index]['rating'] = round(mylist[index]['rating'], 1)
            print(mylist[index]['rating'])

    print("End of the penalizer function!")
    return mylist


def oscar_calculator(po_list):
    print("Beginning of the oscar_calculator() function...")

    # For cycle iterates trough mylist
    for index in range(len(po_list)):
        # Checks if the indexed movie's number of oscar is between 1 and 2
        if 1 <= po_list[index]['oscars'] <= 2:
            # Changing the movie rating according to oscar number
            po_list[index]['rating'] += 0.3
            po_list[index]['rating'] = round(po_list[index]['rating'], 1)
        # Checks if the indexed movie's number of oscar is between 3 and 5
        if 3 <= po_list[index]['oscars'] <= 5:
            # Changing the movie rating according to oscar number
            po_list[index]['rating'] += 0.5
            po_list[index]['rating'] = round(po_list[index]['rating'], 1)
        # Checks if the indexed movie's number of oscar is between 6 and 10
        if 6 <= po_list[index]['oscars'] <= 10:
            # Changing the movie rating according to oscar number
            po_list[index]['rating'] += 1
            po_list[index]['rating'] = round(po_list[index]['rating'], 1)
        # Checks if the indexed movie's number of oscar is more then 10
        if 10 < po_list[index]['oscars']:
            # Changing the movie rating according to oscar number
            po_list[index]['rating'] += 1.5
            po_list[index]['rating'] = round(po_list[index]['rating'], 1)

    print("End of the oscar_calculator() function!")
    return po_list
