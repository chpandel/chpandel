#!/usr/bin/python
import chpandel

sql = """
    INSERT INTO "users"
        ("name", "surname")
    VALUES
        ($1::text, $2::text)
"""

# sql = """
#     SELECT * FROM "users"
# """

# sql = """
#     UPDATE
#         "users"
#     SET
#         "name" = $2::text
#         , "surname" = $3::text
#     WHERE
#         "id" = $1::int
# """

chpandel.SqlQueryRecord(sql, 'Василий', 'Василич')