This is used to create and add table and 
run queries or insert and read data

this is written to support SQLite3 Database which is default installed


when we call the package it has both 
in setup_dp.py file
SetupDatabase - create_connection , close_connection and create_table if table does not exist

in core.py file
CoreDatabase - connect , run_query , close_connection , insert_record
query_table , run_query  for running queries for diff purposes


