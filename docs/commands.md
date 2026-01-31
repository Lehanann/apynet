#

 docker compose down

 docker volume rm intranet_mongo-db

 docker volume rm intranet_pgsql-db

 docker volume prune

  docker compose up -d
# execution du scipt sql - 
# creation des tables et insertion du jeu de donnes
psql -h 127.0.0.1 -U lehannet -d intranet -a -f intranet_schema_v2.sql