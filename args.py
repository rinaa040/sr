import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('server', type=str)
parser.add_argument('port', type=str, help="port")
parser.add_argument('key', type=str, help="key of dict")
parser.add_argument('--digits', type=int, default=1)
parser.add_argument('--mult', type=int, default=1)

args = parser.parse_args()
response = requests.get(f"{args.server}:{args.port}").json()
print(args.key)
