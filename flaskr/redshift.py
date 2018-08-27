from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

creds = (
    'redshift+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
        db_creds['USER'],
        db_creds['PASSWORD'],
        db_creds['HOST'],
        db_creds['PORT'],
        db_creds['DATABASE']
    )
)

print("create engine")
engine = create_engine(
    creds
)

print("create connection")
connection = engine.connect()

try:
    print("query")
    result = connection.execute(
        "SELECT * FROM social_accounts"
    )

    print("print results")
    for row in result:
        print(row)

    result.close()
# print creds
except Exception:
    connection.close()

connection.close()