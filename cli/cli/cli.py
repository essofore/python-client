import cmd
import argparse
import readline
import sys
from commands import *
from essofore_client import Client
import logging

# use this to inspect httpx requests to the server. see: https://www.python-httpx.org/logging/
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.ERROR
)

class Cli(cmd.Cmd):
    intro = 'Essofore v0.1.0. Type help or ? to list commands.'
    prompt = '>> '
    file = None
    client = None

    def __init__(self, client):
        if client is None:
            raise ValueError('client is null')
        super().__init__()
        self.client = client

    def onecmd(self, line):
        # if we don't do this any unhandled exception will bring down the whole app
        try:
            return super().onecmd(line)
        except Exception as e:
            print("Error:", e)

    # this is to prevent last command from being executed again if no input is provided. see:
    # https://stackoverflow.com/a/21066546
    def emptyline(self):
         pass            

    def do_create_collection(self, args):
        'Create a new collection: create collection --collection_id sherlock-holmes'
        create_collection.execute(self.client, args)

    def do_upload_document(self, args):
        'Add document to a collection: upload document --collection_id sherlock-holmes --document_id hound-of-baskervilles --file /path/to/file.txt --doc_type TXT --title "The Hound of Baskervilles"'
        upload_document.execute(self.client, args)

    def do_download_document(self, args):
        'Add document to a collection: download document --collection_id sherlock-holmes --document_id hound-of-baskervilles --source_url https://www.gutenberg.org/cache/epub/2852/pg2852.txt --doc_type TXT --title "The Hound of Baskervilles"'
        download_document.execute(self.client, args)

    def do_search_collection(self, args):
        'Search a collection: search collection --collection_id sherlock-holmes --query "Who is Sherlock Holmes?" -k 5'
        search_collection.execute(self.client, args)

    def do_inspect_catalog(self, args):
        'Inspect catalog: inspect catalog'
        inspect_catalog.execute(self.client)
    
    def do_inspect_collection(self, args):
        'Inspect collection: inspect collection --collection_id sherlock-holmes'
        inspect_collection.execute(self.client, args)

    def do_inspect_document(self, args):
        'Inspect document: inspect document --collection_id sherlock-holmes --document_id hound-of-baskervilles'
        inspect_document.execute(self.client, args)

    def do_delete_document(self, args):
        'Delete document: delete document --collection_id sherlock-holmes --document_id hound-of-baskervilles'
        delete_document.execute(self.client, args)

    def do_delete_collection(self, args):
        'Delete collection: delete collection --collection_id sherlock-holmes'
        delete_collection.execute(self.client, args)

    def do_rename_collection(self, args):
        'Rename collection: rename collection --old_id 1 --new_id 2'
        rename_collection.execute(self.client, args)

    def do_rename_document(self, args):
        'Rename document: rename collection --collection_id 1 --old_id foo --new_id bar'
        rename_document.execute(self.client, args)

    def do_update_collection(self, args):
        'Update dollection: update collection --collection_id 1 --metadata "author=Arthur Conan Doyle" "publisher=Bantam Books"'
        update_collection.execute(self.client, args)

    def do_update_document(self, args):
        'Update document: update document --collection_id 1 --document_id pg2350 --metadata year=1885 rating=4.5 pages=300'
        update_document.execute(self.client, args)

    def do_quit(self, arg):
        'exit the program:  QUIT'
        self.close()
        return True
    
    def do_exit(self, arg):
        'exit the program:  EXIT'
        self.close()
        return True

    # ----- record and playback -----
    # https://docs.python.org/3/library/cmd.html
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        if self.file and 'playback' not in line and 'PLAYBACK' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def default(self, line):
        """Handle unknown commands"""
        parts = line.split()
        if len(parts) < 2:
            print('** Unknown command')
            return
        try:
            w = getattr(self, 'do_' + parts[0] + '_' + parts[1]) 
        except AttributeError:
            print('** Unknown command')
            return
        w(' '.join(parts[2:]))        

def create_client(args):
    if args.host is None:
        args.host = 'http://localhost:8080'
    return Client(args.host)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--host')
    args = p.parse_args()
    client = create_client(args)
    Cli(client).cmdloop()