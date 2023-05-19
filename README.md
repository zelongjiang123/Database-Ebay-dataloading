## Project overview:

A fairly large volume of data downloaded from the eBay web site and stored in JSON files is provided.
JSON is a model primarily used to store semi-structured data. It has become increasingly
popular in recent years, and, for now, you can treat it as just another type of data that is straightforward to
read. In this project, you will examine the data and apply the principles of database design that we learned
in class in order to implement a good relational schema for it. You will then write a Python program to
transform the data from its JSON form into SQLite’s load file format, conforming to your relational schema.
You will create your schema in a SQLite database, load your transformed data, and test it by running some
SQL queries over it.

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
