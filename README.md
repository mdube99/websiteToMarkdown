# websiteToMarkdown

Create a markdown file from a website. Simply supply the website with the argument --website, and it will output the markdown equivalent.

**Note:** Requires markdownify library

#### Installation:

Clone local repository, then run:

```python
pip install -r requirements.txt
```

To download a website:

```bash
python websiteToMarkdown --website 'google.com'
```

If it cannot find a title, it will ask you to supply --title:

```bash
python websiteToMarkdown --website 'google.com' --title 'asdf'
```

You can also specify an output folder:

```bash
python websiteToMarkdown --website 'google.com' --output notes/
```

This will be appended to your home directory. With the example given above, $HOME/notes/
