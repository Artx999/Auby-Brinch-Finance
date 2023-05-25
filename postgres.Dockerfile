FROM postgres:12
COPY ./database_file/users.sql /docker-entrypoint-initdb.d/
COPY ./database_file/notes.sql /docker-entrypoint-initdb.d/
COPY ./database_file/images.sql /docker-entrypoint-initdb.d/