def getMaxScore(F: int, *values: tuple) -> int:
    # Packing letters in a list
    letters = [0] * 5 # [a, b, c, d, e]

    copyLetters = letters.copy() # Will be used to compare results
    indexResults = letters.copy() # Will store the results

    def formula(letters: list) -> int:
        # (60 - (a+b+c+d+e))*F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5
        return (60 - sum(letters))*F + sum(map(lambda x, y: x*y, letters, values))

    # Iterates over each letter comparing the results for 0 and 10
    for i in range(len(letters)):
        temp = copyLetters.copy() # Will give the result for 0
        temp[i] = 10 # Will give the result for 10

        # If the result with 10 is greater, change letter to 10
        if formula(temp) > formula(copyLetters):
            letters[i] = 10

        # Adds the result to the list of results for later use
        indexResults[i] = formula(temp)

    # If `letters` doesn't meet the constraint
    if sum(letters) < 20:
        # Gets first and second highest values out of results
        first, second = sorted(indexResults, reverse=True)[:2]

        # Assigns the first value to the correct index
        letters[indexResults.index(first)] = 10
        # Resets the first value to avoid conflicts
        # (if there is 2 items with the same value, it would always get
        # the index of the first one)
        indexResults[indexResults.index(first)] = 0

        # Same for the second value
        letters[indexResults.index(second)] = 10


    # Returns the optimal result
    return formula(letters)


result = getMaxScore(9, 9, -5, 9, 4, 0)

print(result)
