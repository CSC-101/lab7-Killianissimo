from typing import Optional

'''This function inputs a string and outputs and optional float. This function takes the input
string and tries to convert it to a float. If the compiler throws an error, the function returns
None.
'''
def str_to_float(input:str) -> Optional[float]:
    try:
        output = float(input)
        return output
    except ValueError:
        return None

