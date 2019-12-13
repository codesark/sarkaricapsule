CREATE DATABASE sarkaricapsule;

CREATE USER sarkaricapsule_user WITH PASSWORD 'dbpass001';

ALTER ROLE sarkaricapsule_user SET client_encoding TO 'utf8';
ALTER ROLE sarkaricapsule_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sarkaricapsule_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE sarkaricapsule TO sarkaricapsule_user;

