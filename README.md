# BooksXBlock

BooksXBlock is an XBlock to test learner's knowledge about writers and their works. It presents four titles to the user and asks them to pick the ones that were not authored by the given writer.

## Running the XBlock

A skeleton of this XBlock has been constructed using [cookiecutter-xblock](https://github.com/edx/cookiecutter-xblock) tool which comes with a Docker test environment ready to build, based on the xblock-sdk workbench. To build it, run:

```
docker build -t booksxblock .
```

Then, to run the docker image you built, run:

```
docker run -d -p 8000:8000 --name booksxblock booksxblock
```

The XBlock SDK Workbench, including this XBlock, will be available on the list of XBlocks at http://localhost:8000

## Copyrights
Created by [OpenCraft](http://opencraft.com).

Copyright (c) 2018 OpenCraft GmbH. See included _LICENSE_ file for usage rights.
