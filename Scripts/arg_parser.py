import argparse


parser=argparse.ArgumentParser(description="Process a directory path.")
parser.add_argument('--path',type=str, default='.',help="Directory to scan")
args=parser.parse_args()


print(f"Target path: {args.path}")
