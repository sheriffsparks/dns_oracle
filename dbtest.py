import sqlalchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import sys

def connect(user,password, db, host='localhost',port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user,password,host,port,db)

    con=sqlalchemy.create_engine(url,client_encoding='utf8')

    meta=sqlalchemy.MetaData(bind=con, reflect=True)

    return con,meta

con, meta = connect('dnspy','dnstester','dns')


tld_table=meta.tables['tld']
sub_table=meta.tables['subdomains']


if len(sys.argv) < 2:
    sys.exit()
query=sys.argv[1]
fields=query.split('.')
if len(fields)>=2:
    tld=".".join(fields[-2:])
else:
    sys.exit()

row=con.execute(tld_table.select().where(tld_table.c.domain==tld)).fetchone()
if row: #this means tld is in tld table, next we have to check if the subdomain is already in the subdomains table
    print "TLD already exists"
    tid=row['id']
    count=row['count']
    in_table=con.execute(sub_table.select().where(sub_table.c.query==query)).fetchone()
    if in_table: #subdomain exists so do nothing
        print "already in table it exists"
    else:
        print "adding to subdomain table"
        result=con.execute(sub_table.insert().values(query=query,id=tid))
        #need to update count
        count=count+1
        con.execute(tld_table.update().where(tld_table.c.id==tid).values(count=count))
else: #tld not in table, need to add it and put subdomain in sub table
    #put tld in tld table
    print "Added to tld and subdomain table"
    r=con.execute(tld_table.insert().values(domain=tld,count=1))
    tid=r.inserted_primary_key[0]
    con.execute(sub_table.insert().values(query=query,id=tid))

#session_factory = sessionmaker(con)
dbsess=scoped_session(sessionmaker(con))
tlds = dbsess.query(tld_table.c.domain).all()
print tlds
