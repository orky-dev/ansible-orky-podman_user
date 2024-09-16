import argparse

parser = argparse.ArgumentParser(description='Get the largest subuid/subgid start range number and then generate next one')
parser.add_argument('-f','--filepath', help='Absolute filepath to the subuid/subgid file', required=True)
parser.add_argument('-s','--subcounts', help='Range for subuid/subgid', required=True)
argv = vars(parser.parse_args())
filepath = argv['filepath']
subcounts = int(argv['subcounts'])

with open(filepath) as file:
    newlist=[]
    for item in file:
        x = item.split(":")
        newlist.append(x[1])

largest_number = 2147483648 - subcounts - 1
for num in newlist:
    num = int(num)
    if num > largest_number:
        largest_number = num
print(largest_number + subcounts + 1, end="")
