"""init schema

Revision ID: 5dba61c2c13c
Revises: 
Create Date: 2021-10-06 23:44:20.819849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dba61c2c13c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """CREATE EXTENSION IF NOT EXISTS "uuid-ossp";"""
    )

    op.execute(
        """
        CREATE TABLE user_types (
            id VARCHAR PRIMARY KEY NOT NULL,
            name VARCHAR NOT NULL
        );
        """
    )

    op.execute(
        """
        CREATE TABLE genres (
            id VARCHAR PRIMARY KEY NOT NULL,
            name VARCHAR NOT NULL 
        );
        """
    )

    op.execute(
        """
        CREATE TABLE persons (
            id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v1(),
            name VARCHAR NOT NULL,
            surname VARCHAR NOT NULL,
            birth_date DATE NOT NULL
        );
        """
    )

    op.execute(
        """
        CREATE TABLE users (
            login VARCHAR NOT NULL PRIMARY KEY,
            password VARCHAR NOT NULL,
            user_type_id VARCHAR NOT NULL REFERENCES user_types(id) ON UPDATE CASCADE ON DELETE CASCADE,
            person_id UUID NOT NULL REFERENCES persons(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )

    op.execute(
        """
        CREATE TABLE emails (
            id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v1(),
            email VARCHAR NOT NULL,
            user_login VARCHAR NOT NULL REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )

    op.execute(
        """
        CREATE TABLE films (
            id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v1(),
            duration INTEGER NOT NULL,
            name VARCHAR NOT NULL,
            release_date DATE NOT NULL,
            rating NUMERIC(1),
            director_id UUID NOT NULL REFERENCES persons(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )

    op.execute(
        """
        CREATE TABLE user_favourite_films (
            user_login VARCHAR NOT NULL REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE,
            film_id UUID NOT NULL REFERENCES films(id) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY (user_login, film_id)
        );
        """
    )

    op.execute(
        """
        CREATE TABLE characters (
            id UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v1(),
            name VARCHAR NOT NULL,
            comment VARCHAR,
            film_id UUID NOT NULL REFERENCES films(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    )

    op.execute(
        """
        CREATE TABLE characters_actors (
            character_id UUID NOT NULL REFERENCES characters(id) ON UPDATE CASCADE ON DELETE CASCADE,
            person_id UUID NOT NULL REFERENCES persons(id) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY (character_id, person_id)
        );
        """
    )

    op.execute(
        """
        CREATE TABLE film_genres (
            film_id UUID NOT NULL REFERENCES films(id) ON UPDATE CASCADE ON DELETE CASCADE,
            film_genre_id VARCHAR NOT NULL REFERENCES genres(id) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY (film_id, film_genre_id)
        );
        """
    )

    op.execute(
        """
        INSERT INTO user_types(id, name) VALUES
        ('USER', 'User'),
        ('ADMIN', 'Administrator')
        """
    )

    op.execute(
        """
        INSERT INTO genres(id, name) VALUES
        ('ACTION', 'Action'),
        ('ADVENTURE', 'Adventure'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('CRIME', 'Crime'),
        ('SCI-FI', 'Sci-Fi'),
        ('FANTASY', 'Fantasy'),
        ('MUSICAL', 'Musical'),
        ('WESTERN', 'Western'),
        ('POST_APOCALYPTIC', 'Post-Apocalyptic'),
        ('WAR', 'War'),
        ('FAMILY', 'Family film'),
        ('LOVE', 'Love story'),
        ('CARTOON', 'Cartoon'),
        ('HORROR', 'Horror'),
        ('THRILLER', 'Thriller'),
        ('DOCUMENTARY', 'Documentary')
        """
    )


def downgrade():
    op.execute("DROP TABLE user_types CASCADE;")
    op.execute("DROP TABLE genres CASCADE;")
    op.execute("DROP TABLE persons CASCADE;")
    op.execute("DROP TABLE users CASCADE;")
    op.execute("DROP TABLE emails CASCADE;")
    op.execute("DROP TABLE films CASCADE;")
    op.execute("DROP TABLE user_favourite_films CASCADE;")
    op.execute("DROP TABLE characters CASCADE;")
    op.execute("DROP TABLE characters_actors CASCADE;")
    op.execute("DROP TABLE film_genres CASCADE;")
