# Prompt 1
Using ChatGPT, I asked:
    "I've never used a full-stack repository before, especially in VSCode. Where would I put my SQL code to create the base tables?"

The response I received in summary:
    "SQL code usually put in models.py, but you must convert these tables in SQLAlchemy (aka. Python code, not SQL code)."


# Prompt 2
Using ChatGPT, I asked:
    "I've never heard of SQLAlchemy, so how would the syntax change for a table from SQL to Python?"

The response I received in summary:
    "Think of it like this: SQL table = Python class // SQL rows = Python objects . Here's a short conversion table:"
    | SQL            | SQLAlchemy             |
    | -------------- | ---------------------- |
    | `CREATE TABLE` | `class ... (db.Model)` |
    | `INT`          | `db.Integer`           |
    | `VARCHAR(50)`  | `db.String(50)`        |
    | `DATE`         | `db.Date`              |
    | `TIME`         | `db.Time`              |
    | `PRIMARY KEY`  | `primary_key=True`     |
    | `NOT NULL`     | `nullable=False`       |
    | `UNIQUE`       | `unique=True`          |
    | `FOREIGN KEY`  | `db.ForeignKey()`      |


# Prompt 3
Using ChatGPT, I asked:
    "How do I commit my entire VSCode project to GitHub?"

The response I received in summary:
    "Go to the Source Control tab after connecting your Git account, then it should update the commit submission after you make changes automatically."


# Prompt 4
Using ChatGPT, I asked:
    "I've never used flask shell, so how can I add data through it?"

The response I received in summary:
    "Start flask shell, then begin importing the tables in this manner: [code for inputting table data to sample table]."


# Prompt 5
Using ChatGPT, I asked:
    "What is the purpose of the routes.py file?"

The response I received in summary:
    "It mainly controls the User Actions, Database Logic, and HTML pages, and puts it all together to work coherently."


# Prompt X
Using ChatGPT, I asked:
    "test"

The response I received in summary:
    "test"


# Prompt X
Using ChatGPT, I asked:
    "test"

The response I received in summary:
    "test"