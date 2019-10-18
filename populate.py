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

from uuid import uuid4

from pony.orm import commit
from pony.orm import db_session

from database import Producto
from database import Voucher

# --------------------------------------------------------------------------- #
# Set Pragma Key ON
# --------------------------------------------------------------------------- #
#db.execute("PRAGMA foreign_keys = ON;")

# --------------------------------------------------------------------------- #
# Populate Database
# --------------------------------------------------------------------------- #

@db_session()
def random_voucher():
    """ Generate Random Voucher """
    for _i in range(10):
        Voucher(codigovoucher=str(uuid4()),
                estado=0)
    commit()


@db_session()
def productos():
    """ Sample Products """
    Producto(
        titulo="Tech Bag",
        descripcion="Something to carrey something",
        urlimagen="img/mochila.jpg")
    # Commit
    commit()

    Producto(
        titulo="Space Ship",
        descripcion="A Thing to go to another place",
        urlimagen="img/nave.jpg")

    # Commit
    commit()

# --------------------------------------------------------------------------- #
# Sample Database
# --------------------------------------------------------------------------- #

#Calling functions
productos()
random_voucher()
