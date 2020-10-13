## Content

- About SQLAlchemy vs DB Drivers
- About SQLAlchemy ORM
    * Engines
    * Declaratives
        * Classes, Columns & Types (Models)
        * Tables
    * Sessions
- Querying the Database
    * All & First
    * Order By
    * Offset & Limit
    * FilterBy & Filter
    * Chaining query methods
- Relationships
- Modularizing Implementation
- Updating & Deleting Record

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

- Working with the query object - https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
- Working with relationships - https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship
