

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
            diff = mylist[0]['votes'] - mylist[index]['votes']
            print('Diff: ', diff)


    print("End of the penalizer function!")