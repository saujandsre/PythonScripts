"""
Scan a text file and let the user:

        --file → specify the file

            --count-lines, --count-words, --count-chars → choose what to count

"""



import argparse 


parser=argparse.ArgumentParser(description="Process a text file")
parser.add_argument('--file', type=str, help="Specify the file")
parser.add_argument('--count', default="lines", choices=['lines','words','chars'], help="What would you like to count ? ")
args=parser.parse_args()


lines = 0
words = 0
chars = 0

with open(args.file, 'r') as f:
    for line in f:
        lines +=1
        words += len(line.split())
        chars += len(line)

if args.count == "words":
    print(f"Total words in this {args.file} are {words}")
elif args.count == "chars":

    print(f"Total chars in this {args.file} are {chars}")
else:

    print(f"Total lines in this {args.file} are {lines}")
