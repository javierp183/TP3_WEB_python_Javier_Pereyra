from database import db,Voucher
from pony.orm import commit,db_session
import uuid


@db_session()
def populanga():
    for i in range(1000):
        Voucher(CodigoVoucher=str(uuid.uuid4()),
        Estado=0)
    commit()


populanga()