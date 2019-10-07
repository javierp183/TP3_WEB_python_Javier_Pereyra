from bottle import route, run, template
from database import db,Voucher
from pony.orm import db_session


@route('/validate/voucher/<number>')
@db_session
def validate_voucher_number(number):
    salida = Voucher(CodigoVoucher=number).show()
    return salida

run(host='localhost', port=8080)