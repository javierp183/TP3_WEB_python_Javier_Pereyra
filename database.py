#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from datetime import date
from pony.orm import Database
from pony.orm import PrimaryKey
from pony.orm import Optional
from pony.orm import Set
from pony.orm import set_sql_debug
from loader import Loader

# --------------------------------------------------------------------------- #
# Database
# --------------------------------------------------------------------------- #

config = Loader().settings

db = Database()
db.bind(**config['database']['engine'], create_db=True)


if config['database']['debug']:
    set_sql_debug(True)

# --------------------------------------------------------------------------- #
# Tables Schemas
# --------------------------------------------------------------------------- #


class Producto(db.Entity):
    """ Products Table """
    id = PrimaryKey(int, auto=True)
    titulo = Optional(str, 50)
    descripcion = Optional(str, 250)
    urlimagen = Optional(str, 1000)
    codigovoucher = Set('Voucher')


class Cliente(db.Entity):
    """ Client Table """
    id = PrimaryKey(int, auto=True)
    dni = Optional(int)
    nombre = Optional(str)
    apellido = Optional(str)
    email = Optional(str)
    direccion = Optional(str)
    ciudad = Optional(str)
    codigoPostal = Optional(str)
    fechaRegistro = Optional(str)
    vouchers = Set('Voucher')


class Voucher(db.Entity):
    """ Voucher Table """
    id = PrimaryKey(int, auto=True)
    codigovoucher = Optional(str)
    estado = Optional(bool)
    fecharegistro = Optional(date)
    producto = Set(Producto)
    cliente = Set(Cliente)

# --------------------------------------------------------------------------- #
# Create Tables
# --------------------------------------------------------------------------- #

db.generate_mapping(create_tables=True)

# --------------------------------------------------------------------------- #
# END
# --------------------------------------------------------------------------- #

# EOF
