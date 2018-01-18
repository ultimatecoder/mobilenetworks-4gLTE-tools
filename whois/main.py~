import argparse
import json
import sys

import fetcher
from ip_type import ip_type
import run_command


if __name__ == '__main__':
    description = (
        "whois - a CLI tool for determining the approximate"
        " geo-location of a 4G LTE/3G user visiting your app/site"
        " using just the IP address. This is a thin wrapper over"
        " the Fastah GeoIP REST API and uses statistical models"
        " to provide city-level results.\n"
        "Register at https://console.api.getfastah.com/signup\n"
        "Select your desired developer plan\n"
        "Use to value of Access token as -t or --token parameter."
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'ips',
        type=ip_type,
        nargs='*',
        help="IP address in the form of valid IP address. Example: 103.10.66.11"
    )
    parser.add_argument(
        '-t', '--token',
        type=str,
        help="Token value of Primary key you got after registration."
    )
    parser.add_argument(
        '-c', '--default-token',
        dest="default_token",
        action='store_true',
        help="Change the default value of token stored at '~/.whoisrc' file."
    )
    parser.add_argument(
        '-d', '--delete-token',
        dest='delete_token',
        type=str,
        help="Delete the token from the stored configuration file '~/.whoisrc.'"
    )
    args = parser.parse_args()
    if args.default_token:
        tokens = run_command.get_tokens()
        if not tokens:
            print("Unable to find stored tokens.")
            sys.exit(1)
        else:
            for i in range(10):
                print("Stored tokens:")
                for (i, token) in enumerate(tokens):
                    print("{}: {}".format(i, token))
                try:
                    i = int(input(
                        "Please choose valid index of expected token: "))
                    if i >= 0 and i < len(tokens):
                        run_command.set_default_token(position=i)
                        print("Token updated successfully.")
                        break
                    else:
                        message = "Invalid input. Valid values between 0 and {}"
                        print(message.format(len(tokens)))
                except ValueError:
                    print("Please enter a valid integer input")
            else:
                print("Maximum time reached.")
                sys.exit(1)
    elif args.delete_token:
        print("Not implimented error.")
        sys.exit(1)
    elif args.ips:
        if not args.token:
            token = run_command.get_default_token()
            if not token:
                print("Argument -t, --token is missing.")
                sys.exit(1)
        else:
            token = args.token
            run_command.add_token(token)
        responses = fetcher.fetch_multiple_details(args.ips, token)
        if not responses:
            print("Error while receiving response.")
            sys.exit(1)
        print(json.dumps(responses))
    elif not args.ips:
        print("IP as default argument is expected.")
        sys.exit(1)
