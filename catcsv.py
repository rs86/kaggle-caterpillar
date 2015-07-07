import sys
import csv
import os

def main(argv):
    if len(argv) == 0:
        return

    filename = argv[0]
    print 'Showing CSV: ' + filename

    f = open(filename, 'r')
    reader = csv.reader(f)

    rows = []
    for row in reader:
        rows.append(row)
    
    widths = []

    for i in range(len(rows[0])):
        widths.append(2+max([len(r[i]) for r in rows]))

    for row in rows:
        for val, width in zip(row, widths):
            sys.stdout.write(val.ljust(width))
        sys.stdout.write("\n")

main(sys.argv[1:])
