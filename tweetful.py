
import authorization
import json
import requests
import argparse
import sys
from urls import *

def make_parser():
    #ArgumentParser.add_subparsers
    parser = argparse.ArgumentParser(description='ingest twitter API calls: timeline')
    subparser = parser.add_subparser(dest="command", help="available commands")

    #timeline
    timeline_parse = subparsers.add_subparser("timeline", help = "Show Twitter Timeline")


def main():
    ##  main function
    parser = make_parser()
    arguments = parse.parse_args(sys.argv[0])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    auth = authorization.authorize()
    
    if command == "TL":
        response = requests.get(TIMELINE_URL, auth=auth)
        print json.dumps(response.json(), indent=4)

    else:
        print "geuss again sucka"
        return    


if __name__ == '__main__':
    main()

