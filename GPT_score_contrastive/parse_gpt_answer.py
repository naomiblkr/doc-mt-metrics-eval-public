import re


def parse_answer(response):
    """Parse GPT answer and extract score"""
    # get all numbers in a list
    numbs = re.findall(r'\d+', response)
    if len(numbs) == 1:
        return int(numbs[0])
    elif len(numbs) == 2:
        # return only the first number if response is in format "85 out of 100" or "75/100"
        if int(numbs[1]) == 100:
            return int(numbs[0])
        # return the second number if response is in format "out of 100, ... 85"
        if (int(numbs[0]) == 100) and (int(numbs[1]) < 100):
            return int(numbs[1])
    # return None if no score is found
    elif len(numbs) == 0:
        return None
    # return the first number if there are multiple numbers in answer
    # should be the score as it is usually at the beginning of the response
    else:
        return int(numbs[0])
    
