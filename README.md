# README

## Run the server

In below we assume you have an Essofore server up and running somewhere and have opened up necessary port to allow traffic to/from a client.

## Pre-requisites

In a real-world setup you would be using Essofore just like you use a database like MySQL or PostgreSQL.
There will be a server instance the running of which is covered elsewhere and there would be one or more backend service(s) making calls to the server using the REST API.
Here we show how to make calls to a server using Python. 

Before we can start using the client, we need to install a bunch of pre-requisites. Always refer to official documentation for latest instructions.

0. Install `python`

1. Install `pipx`

```
sudo apt install pipx
```

2. Install `poetry`. Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. It should in no case be installed in the environment of the project that is to be managed by Poetry. In addition, the isolated virtual environment in which poetry is installed should not be activated for running poetry commands.

Accordingly, begin by creating a separate virtual environment for poetry:

```
python3 -m venv poetry-venv
```

activate the new virtual environment:

```
source poetry-venv/bin/activate
```

install `poetry` in this virtual environment:

```
pipx install poetry
```

now deactivate the virtual environment:

```
deactivate
```

3. Now `cd` to the `cli` directory and from there run `poetry install`:

```
cd cli
poetry install
```

Note that we have not activated any virtual environment while running `poetry install`. This will install all the dependencies declared in `pyproject.toml`.

This finishes installing the pre-requisites and the python client. The steps in this section do not have to be repeated again. If you sync to a new version of the client, you will have to
re-run `poetry install` to install any new dependencies but other than that everything in this section is a one-time setup.

## Python CLI

1. cd to `cli` directory and from there activate a new shell by running:

```
poetry shell
```

2. `cd` to the `cli/cli` subdirectory and from there run:

```
python cli.py --host http://ip-address/port
```

If all goes well, you should see a prompt like following:

```
Essofore v0.1.0. Type help or ? to list commands.
>>
```

What you have done here is connected to the server using a CLI just like you do with MySQL or PostgreSQL command-line clients. Let the games begin!

### Inspecting the catalog

Begin by inspecting the database:

```
inspect catalog
```

You should see empty result. Next, let us create a _collection - a collection is a container that stores related documents_.
For example, we can create a collection to store all the novels of Sherlock Holmes. Do this by running:

### Creating a collection

```
create collection --collection_id 1 --title Sherlock Holmes
```

Great! Now lets add some documents to the collection. You can try adding your own documents or download the works of Arthur Conan Doyle (the creator of Sherlock Holmes)
from [Project Gutenberg](https://www.gutenberg.org/ebooks/search/?query=sherlock+holmes&submit_search=Go%21) in a subdirectory `/data/sherlock-holmes` under `cli/cli`:

```
wget https://www.gutenberg.org/cache/epub/1661/pg1661.txt
wget https://www.gutenberg.org/cache/epub/244/pg244.txt
wget https://www.gutenberg.org/cache/epub/2852/pg2852.txt
wget https://www.gutenberg.org/cache/epub/2097/pg2097.txt
wget https://www.gutenberg.org/cache/epub/834/pg834.txt
wget https://www.gutenberg.org/cache/epub/3289/pg3289.txt
wget https://www.gutenberg.org/cache/epub/108/pg108.txt
wget https://www.gutenberg.org/cache/epub/2350/pg2350.txt
wget https://www.gutenberg.org/cache/epub/69700/pg69700.txt
```

Now let's add them to the database. Do that by running and modifying paths as necessary:

### Adding documents to a collection

```
upload document --collection_id 1 --document_id pg3289 --title The Valley of Fear --file ./data/sherlock-holmes/pg3289.txt --doc_type txt
upload document --collection_id 1 --document_id pg1661 --title The Adventures of Sherlock Holmes --file ./data/sherlock-holmes/pg1661.txt --doc_type txt
upload document --collection_id 1 --document_id pg108 --title The Return of Sherlock Holmes --file ./data/sherlock-holmes/pg108.txt --doc_type txt
upload document --collection_id 1 --document_id pg2097 --title The Sign of the Four --file ./data/sherlock-holmes/pg2097.txt --doc_type txt
upload document --collection_id 1 --document_id pg2350 --title His Last Bow --file ./data/sherlock-holmes/pg2350.txt --doc_type txt
upload document --collection_id 1 --document_id pg2852 --title The Hound of the Baskervilles --file ./data/sherlock-holmes/pg2852.txt --doc_type txt
upload document --collection_id 1 --document_id pg834 --title The Memoirs of Sherlock Holmes --file ./data/sherlock-holmes/pg834.txt --doc_type txt
upload document --collection_id 1 --document_id pg69700 --title The Case Book of Sherlock Holmes --file ./data/sherlock-holmes/pg69700.txt --doc_type txt
upload document --collection_id 1 --document_id pg244 --title A Study in Scarlet --file ./data/sherlock-holmes/pg244.txt --doc_type txt
```

These commands are also available in `cli/cli/sherlock-holmes.txt` and the CLI has a nify feature that allows you to run all the commands in a text file like so:

```
playback sherlock-holmes.txt
```

Try querying the catalog once again and see what you get:

```
inspect catalog
```

### Searching Documents in a Collection

We can now execute search queries against the documents in a collection. Do that by running following commands:

```
search collection --collection_id 1 --query "Who is Sherlock Holmes?"
search collection --collection_id 1 --query "Who is Dr. Watson?"
search collection --collection_id 1 --query "How are Sherlock Holmes and Dr. Watson related?"
search collection --collection_id 1 --query "Where does Sherlock Holmes live?"
search collection --collection_id 1 --query "How old is Sherlock Holmes?"
```

By default the top 5 results are fetched from the database. This can be changed via the `-k` parameter to the CLI.

### Python API

Below is the `python` code that would accomplish the steps we have performed till now:

1. create collection
2. add documents
3. search

```
from essofore_client.api.collections import create_collection, upload_document, search
from essofore_client.models.document_type import DocumentType
create_collection.sync_detailed(collection_id="1", title="Sherlock Holmes", client=client)
with open('./data/sherlock-holmes/pg3289.txt, 'rb') as f:
  upload_document.sync_detailed(client=client,
                              collection_id = "1",
                              document_id = "pg2350",
                              title="The Hound of the Baskervilles", 
                              doc_type=DocumentType.TXT,
                              source_url = url,
                              body=Blob(f))
response = search.sync_detailed(client=client, collection_id="1", q="Who is Sherlock Holmes?", k=5)
for r in response.parsed:
    print_search_result(r)
```

In a real-world implementation the line `with open('./data/sherlock-holmes/pg3289.txt, 'rb') as f:` would be replaced by a call that fetches a document from S3 or another blob storage
where your actual data is likely stored e.g., Sharepoint, Confluence etc. Note that you do not have to store a copy of the document on your client before uploading it to the server.
You open a binary stream and pipe it to the server.

### Ingesting Public URLs

For documents available on public URLs, there is a shortcut to add them to the database by giving the public URL. We show how to do that now.
First, create a new collection to store the works of Shakespeare:

```
create collection --collection_id 2 --title Shakespeare
```

And now add to the collection by downloading from the public URL:

```
download document --collection_id 2 --document_id pg100 --title Complete Works of William Shakespeare --source_url https://www.gutenberg.org/cache/epub/100/pg100.txt --doc_type TXT
```

The `python` code would look like:

```
from essofore_client.api.documents import download_document
from essofore_client.models.download_document_metadata import DownloadDocumentMetadata
...
response = download_document.sync_detailed(client=client,
                                                collection_id = collection_id,
                                                document_id = document_id,
                                                title=title,
                                                source_url=source_url,
                                                doc_type=doc_type,
                                                metadata=metadata)
```

Exit the CLI by typing `exit` or `quit` when you are done. Also take care to exit the `poetry` shell when done.

### Exploring Further

Type `help` to see list of all the commands available in the CLI:

```
>> help

Documented commands (type help <topic>):
========================================
create_collection  help                quit               update_collection
delete_collection  inspect_catalog     record             update_document
delete_document    inspect_collection  rename_collection  upload_document
download_document  inspect_document    rename_document
exit               playback            search_collection
```

There are commands to remove documents from a collection and delete entire collection itself. You can also rename documents and collections but you cannot move a document
from one collection to another. You have to do that explicitly via a combination of commands.

Study the source code of commands under `cli/cli/commands` to understand how the CLI uses the python client library `essofore-client` to communicate with the database.
You can similarly write clients in any programming language you like and are not limited to `python` since the core communication happens to the server over a REST API.

## Other Languages

You are not limited to using Python to program against the server. You can use OpenAPI generators like [this](https://github.com/OpenAPITools/openapi-generator) one together with the provided [api.yaml](api.yaml) file in this repo to generate a client in another language.

## Help and Support

- [Google Groups](https://groups.google.com/g/essofore)
