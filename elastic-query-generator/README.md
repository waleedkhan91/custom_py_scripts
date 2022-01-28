The main purpose of this repo is to demonstrate elasticsearch query generator program which we can use to generate any query based on our requirements. The other programs in different directories are some old exercises which I have just commited here for no reason. So ignore those and enjoy this script.

Use following command to execute this script.

    docker build . -t py-elastic
    docker run -v $(pwd)/app.py:/usr/app/elastic/src/app.py --rm -it py-elastic