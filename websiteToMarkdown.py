import requests
import argparse
import re
from markdownify import markdownify as md

parser = argparse.ArgumentParser()# Add an argument
parser.add_argument('--website', type=str, required=True)# Parse the argument
parser.add_argument('--title', type=str, required=False)# Parse the argument
args = parser.parse_args()
print('website,', args.website)

content = requests.get(args.website)

webpage = content.text


if not args.title:
    # Finds the html <title> and stores it in the "title" variable
    title = re.compile("<title>(.*?)</title>")
    matchResult = title.search(webpage)
    if matchResult:
        f = open(f"{matchResult.group(1)}.md", "w")
        f.write(md(webpage, strip=['a']))
        f.close()
    else:
        # If it can't find the title, it will ask the user to use --title
        print("Couldn't find <title> in the webpage, set a manual title with --title")
        quit
else:
    title = args.title
    f = open(f"{args.title}.md", "w")
    f.write(md(webpage, strip=['a']))
    f.close()
