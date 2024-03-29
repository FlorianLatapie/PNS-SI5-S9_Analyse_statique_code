import sqlalchemy

# bad
query = "SELECT * FROM foo WHERE id = '%s'" % identifier
query = "INSERT INTO foo VALUES ('a', 'b', '%s')" % value
query = "DELETE FROM foo WHERE id = '%s'" % identifier
query = "UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier
query = """WITH cte AS (SELECT x FROM foo)
SELECT x FROM cte WHERE x = '%s'""" % identifier
# bad alternate forms
query = "SELECT * FROM foo WHERE id = '" + identifier + "'"
query = "SELECT * FROM foo WHERE id = '{}'".format(identifier)
query = "SELECT * FROM foo WHERE id = '[VALUE]'".replace("[VALUE]", identifier)

# bad
cur.execute("SELECT * FROM foo WHERE id = ?", (identifier,))
cur.execute("INSERT INTO foo VALUES ('a', 'b', ?)", (value,))
cur.execute("DELETE FROM foo WHERE id = ?", (identifier,))
cur.execute("UPDATE foo SET value = 'b' WHERE id = ?", (identifier,))
# bad alternate forms
cur.execute("SELECT * FROM foo WHERE id = ?", (identifier,))
cur.execute("SELECT * FROM foo WHERE id = ?", (identifier))
cur.execute("SELECT * FROM foo WHERE id = '[VALUE]'".replace("[VALUE]", identifier))

# bad f-strings
cur.execute("SELECT ? FROM foo WHERE id = 1", (column_name))
cur.execute("SELECT ? FROM foo WHERE id = 1", (a+b))
cur.execute("INSERT INTO ? VALUES (1)", (table_name))
cur.execute("UPDATE ? SET id = 1", (table_name))

# good
cur.execute("SELECT * FROM foo WHERE id = '%s'", identifier)
cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')", value)
cur.execute("DELETE FROM foo WHERE id = '%s'", identifier)
cur.execute("UPDATE foo SET value = 'b' WHERE id = '%s'", identifier)

# bug: 
def a():
    def b():
        pass
    return b

a()("SELECT %s FROM foo" % val)

# real world false positives
choices=[('server_list', _("Select from active instances"))]
print("delete from the cache as the first argument")
