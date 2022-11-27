import requests
import argparse
import re
import os
from markdownify import markdownify as md

parser = argparse.ArgumentParser()# Add an argument
parser.add_argument('-w', '--website', type=str, required=True, help='The website that you would like to download as markdown')# Parse the argument
parser.add_argument('-f', '--filename', type=str, required=False, help='(optional) If you would like to add a specific filename to download as')# Parse the argument
parser.add_argument('-o' '--output', type=str, required=False, help='(optional) If you would like to specify an output folder. The home directory is already included.')# Parse the argument
args = parser.parse_args()
print('website,', args.website)

content = requests.get(args.website)

webpage = content.text

# Supply the name you would like for the file
def createFile(filename):
    if not args.output:
        f = open(f"{filename}.md", "w")
        f.write(md(webpage, strip=['a']))
        f.close()
    else:
        # If you don't want it made in the current directory, you can specify the directory you want.
        # This will get the home directory, to which you can add any further path you want.
        nameWithPath = os.path.join(f"{os.path.expanduser('~')}/{args.output}", f"{filename}.md")
        f = open(nameWithPath, "w")
        f.write(md(webpage, strip=['a']))
        f.close()

def main():
    if not args.filename:
        # Finds the html <title> and stores it in the "title" variable
        title = re.compile("<title>(.*?)</title>")
        matchResult = title.search(webpage)
        if matchResult:
            # supplies the proper title from the matchResult
            createFile({matchResult.group(1)})
        else:
            # If it can't find the title, it will ask the user to use --title
            print("Couldn't find <title> in the webpage, set a manual title with --title")
            quit
    else:
        createFile(args.title)

main()
