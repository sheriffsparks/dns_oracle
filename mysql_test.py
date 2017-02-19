import MySQLdb as mdb
from sets import Set
# SELECT SUBSTRING_INDEX(DOMAIN, '.', -2) AS tld, COUNT(*) AS total
#   FROM EVIL
#     GROUP BY tld
#       HAVING COUNT(*) > 10;
user="dnspy"
password="dnstester"
database="dns"
url="localhost"


def connect_db(url,user, password, database):
    return mdb.connect(url,user,password, database)

con=connect_db(url, user, password, database)
cur=con.cursor()
cur.execute("SELECT SUBSTRING_INDEX(QUERY, '.', -2) AS tld, COUNT(*) AS total FROM dns GROUP BY tld HAVING COUNT(*) > 2")

results= cur.fetchall()
l=[i[0] for i in results]
s=Set(l)
print l
print s
print type(s)
print "tmz.com" in s

