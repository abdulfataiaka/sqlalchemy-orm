## Content

- About SQLAlchemy vs DB Drivers
- About SQLAlchemy ORM
    * Engines
    * Declaratives
        * Classes, Columns & Types (Models)
        * Tables
    * Sessions

## Steps

- Create Declarative Base
- Create "Models" extending the Declarative Base
- Create tables
- Interact with the tables via the "Models"
- Create Relationships

## Custom Directives

- Authors (id, username, password) - `Author`
- Books (id, author_id, title) - `Book`

## Resources

- Query Methods Reference - https://docs.sqlalchemy.org/en/13/orm/query.html
- Column & Type Classes Reference - https://docs.sqlalchemy.org/en/13/core/type_basics.html
- About the directive base metadata : https://docs.sqlalchemy.org/en/13/core/metadata.html
