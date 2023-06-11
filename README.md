## Project overview:

Designed and implemented a good relational schema for given Ebay data. Transformed the data from its JSON form into SQLite’s load file format, conforming to the proposed relational schema. Created schema in an SQLite database, loaded transformed data, and tested it by running some SQL queries over it.

## Main files:

data_parser.py, load.txt, create.sql, and desgin.pdf

## Main coding language:

python 3.9

## Run Program:

1. run "sh runParser.sh" which will run data_parser.py and generate many .dat files for bulk loading

2. run "sqlite3 <db_name> < create.sql" and then "sqlite3 <db_name> < load.txt". You will get a sqlite database file named <db_name>

3. run "sqlite3 <db_name>" to open the database with tables

4. run ".read query<number>" to run the queries

## Attributions:

I (Zelong Jiang) wrote data_parser.py, runParser.sh, load.txt, and all sql queries.

My partner Junior Esparza Diaz wrote design.pdf
