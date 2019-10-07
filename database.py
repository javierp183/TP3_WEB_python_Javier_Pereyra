from datetime import date
from pony.orm import *
from loader import Loader

config = Loader().settings
db = Database()
db.bind(**config['database'],create_db=True)
set_sql_debug(True)


class Producto(db.Entity):
    id = PrimaryKey(int, auto=True)
    Titulo = Optional(str, 50)
    Descripcion = Optional(str, 250)
    URLImagen = Optional(str, 1000)
    vouchers = Set('Voucher')


class Cliente(db.Entity):
    id = PrimaryKey(int, auto=True)
    DNI = Optional(int)
    Nombre = Optional(str)
    Apellido = Optional(str)
    Email = Optional(str)
    Direccion = Optional(str)
    Ciudad = Optional(str)
    CodigoPostal = Optional(str)
    FechaRegistro = Optional(str)
    vouchers = Set('Voucher')


class Voucher(db.Entity):
    id = PrimaryKey(int, auto=True)
    CodigoVoucher = Optional(str)
    Estado = Optional(bool)
    FechaRegistro = Optional(date)
    producto = Set(Producto)
    cliente = Set(Cliente)


db.generate_mapping(create_tables=True)

