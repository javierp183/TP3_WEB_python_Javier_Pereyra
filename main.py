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

# Database
from pony.orm import db_session, select

# Framework
from bottle import jinja2_view as view
from bottle import request
from bottle import route, run, redirect

# Tables
from database import Voucher, Producto
from loader import Loader

# Data compare
from dataclasses import dataclass 

# Settings
settings = Loader().settings

# --------------------------------------------------------------------------- #
# Helper
# --------------------------------------------------------------------------- #
class Confirm:
    dni = ""
    nombre = ""
    apellido = ""
    email = ""
    direccion = ""
    ciudad = ""
    codigopostal = ""


# --------------------------------------------------------------------------- #
# Application Routes
# --------------------------------------------------------------------------- #

@route('/')
@route('/<msg>')
@view('index.tpl', template_lookup=['views'])
def main_index(msg=False):
    """ Main Index """
    valiate = request.params.get('msg', False)
    result = dict(title=settings['application']['tittle'])

    if valiate:
        result['msg'] = settings['application']['message'][msg]

    return result


@route('/validate', method=["POST"])
@db_session
def validate_voucher_number():
    """ Validate if Voucher Exists """
    voucher = request.params.get('voucher', False)
    if not voucher:
        return redirect('/voucher_need')
    if Voucher.exists(codigovoucher=str(voucher)):
        code = Voucher.get(codigovoucher=str(voucher)).codigovoucher
        return redirect('/product/{}'.format(code))
    return redirect('/not_valid')


@route('/product/<voucher>')
@view('product.tpl', template_lookup=['views'])
@db_session
def get_all_products(voucher):
    """ Select a Product """
    if not voucher:
        return redirect('/')

    if not Voucher.exists(codigovoucher=str(voucher)):
        return redirect('/not_valid')

    prods = select(p for p in Producto)[:]
    result = dict(voucher=voucher, data=[p.to_dict() for p in prods])
    return dict(context=result)


@route('/confirm/<voucher>/<idx>')
@view('confirm.tpl', template_lookup=['views'])
@db_session
def user_confirm_voucher(voucher, idx):
    array = []
    dni = request.params.get("dni")
    nombre = request.params.get("nombre")
    apellido = request.params.get("apellido")
    email = request.params.get("email")
    direccion = request.params.get("direccion")
    ciudad = request.params.get("ciudad")
    codigopostal = request.params.get("cp")
    fecha = request.params.get("fecha")
    vouchers = voucher

    array.append(dni)
    array.append(nombre)
    array.append(apellido)
    array.append(email)
    array.append(direccion)
    array.append(ciudad)
    array.append(codigopostal)
    array.append(fecha)
    array.append(vouchers)    


    for i in array:
        if( i.find("Ingrese")):
            print("Aca metes el insert")
        else:
            return "No ingreso todas las opciones"

    if not voucher and not idx:
        return redirect('/voucher_need_and_id')

    result = dict(msg="test")
    return dict(context=result)

run(**settings['framework'])
