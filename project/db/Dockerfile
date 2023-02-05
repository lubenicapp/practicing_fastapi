FROM mariadb:10.9

COPY create.sql /docker-entrypoint-initdb.d/
RUN chmod -R 775 /docker-entrypoint-initdb.d
