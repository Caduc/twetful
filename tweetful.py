
import authorization
import json
import requests
import argparse
import sys
from urls import *

def make_parser():
    #ArgumentParser.add_subparsers
    parser = argparse.ArgumentParser(description='ingest twitter API calls: timeline')
    subparsers = parser.add_subparsers(dest="command", help="available commands")

    #timeline
    timeline_parse = subparsers.add_parser("timeline", help = "Show Twitter Timeline")
    return parser


def main():
    ##  main function
    print ("arg that was entered is: " + sys.argv[1])
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    auth = authorization.authorize()

    if command == "timeline":
        response = requests.get(TIMELINE_URL, auth=auth)
        print json.dumps(response.json(), indent=4)

    else:
        #print "geuss again sucka"
        return    


if __name__ == '__main__':
    main()

