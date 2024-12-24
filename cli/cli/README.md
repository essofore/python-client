# README

Download sherlock holmes collection from Project Gutenberg on your hard drive.
Edit `sherlock-holmes.txt` and replace paths as necessary.

Run following commands:

```
poetry shell
python cli.py
```

This will bring up a command-line shell.

From the shell run following commands:

```
playback sherlock-holmes.txt
playback shakespeare.txt
```

this will upload sherlock holmes and shakespeare to the database.

then you can query the database like this:

```
search collection --collection_id 1 --query Who is Sherlock Holmes?
```
