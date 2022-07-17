import csv
import io
from turtle import towards


def execute(f):
    result = []
    reader = csv.reader(f)
    for line in reader:
        one = int(line[0])
        two = int(line[1])
        three = one + two
        line.append(three)
        result.append(line)
    return result


src = """\
20,40
50,90
77,22
"""

with io.StringIO(src) as f:
    result = execute(f)
    print(result)
