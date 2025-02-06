-- postgresql
/* 
dr run -d --name lrng-db \
    -e POSTGRES_PASSWORD=Contra12345$ \
    -e POSTGRES_DB=local_reango \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -e POSTGRES_USER=rng \
    -e TZ=America/Mexico_City \
    --mount src=lrng,dst=/var/lib/postgresql/data \
    -p 5437:5432 \
    --shm-size=1024m \
    postgres

export DB_HOST="localhost"
export DB_USER="rng"
export DB_PASSWORD="Contra12345$"
export DB_NAME="local_reango"
export DB_PORT="5437"

dr exec -it lrng-db psql -U rng -d local_reango
*/

CREATE TABLE chats (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) NOT NULL,
    model VARCHAR(255),
    usuario VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

