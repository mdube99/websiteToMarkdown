import requests
import argparse
import re
import os
from markdownify import markdownify as md

parser = argparse.ArgumentParser()# Add an argument
parser.add_argument('--website', type=str, required=True)# Parse the argument
parser.add_argument('--title', type=str, required=False)# Parse the argument
parser.add_argument('--output', type=str, required=False)# Parse the argument
args = parser.parse_args()
print('website,', args.website)

content = requests.get(args.website)

webpage = content.text

def createFile():
    if not args.output:
        f = open(f"{args.title}.md", "w")
        f.write(md(webpage, strip=['a']))
        f.close()
    else:
        # If you don't want it made in the current directory, you can specify the directory you want.
        # This will get the home directory, to which you can add any further path you want.
        nameWithPath = os.path.join(f"{os.path.expanduser('~')}/{args.output}", f"{args.title}.md")
        f = open(nameWithPath, "w")
        f.write(md(webpage, strip=['a']))
        f.close()

def main():
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
        createFile()

main()
