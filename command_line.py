import sys
from typing import Optional
import convert


def list_to_floats() -> list[Optional[int]]:
    output = []
    for i in range(1, len(sys.argv)):
        if convert.str_to_float(sys.argv[i]) is not None:
            output.append(convert.str_to_float(sys.argv[i]))
    return output



if __name__ == "__main__":
    print(list_to_floats())
    print(sys.argv)
