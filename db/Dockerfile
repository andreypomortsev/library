FROM postgres:latest

COPY init.sql /docker-entrypoint-initdb.d/
COPY procedures.sql /docker-entrypoint-initdb.d/
