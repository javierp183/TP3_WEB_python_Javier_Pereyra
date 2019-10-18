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
from pony.orm import commit

# Framework
from bottle import jinja2_view as view
from bottle import request
from bottle import route, run, redirect
from bottle import static_file

# Tables / Objects
from database import Voucher, Producto
from database import Cliente
from loader import Loader

# Datetime
import datetime

# Settings and current time
settings = Loader().settings
now = datetime.datetime.now()

# --------------------------------------------------------------------------- #
# Function - Static - Publish content
# --------------------------------------------------------------------------- #

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# --------------------------------------------------------------------------- #
# Function - Helpers - Render output
# --------------------------------------------------------------------------- #

@route('/errorvoucher')
@view('errorvoucher.tpl', template_lookup=['views'])
def error():
    pass

@route('/thanks')
@view('thanks.tpl', template_lookup=['views'])
def thanks():
    pass

@route('/already')
@view('already_registered.tpl', template_lookup=['views'])
def thanks():
    pass

@route('/complete')
@view('complete_fields.tpl', template_lookup=['views'])
def complete():
    pass

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

    # Validate if Voucher exist.
    if Voucher.exists(codigovoucher=str(voucher)):
        code = Voucher.get(codigovoucher=str(voucher)).codigovoucher
        return redirect('/product/{}'.format(code))
    return redirect('/errorvoucher')

    if not voucher:
        return redirect('/voucher_need')


@route('/usersave', method=["POST"])
@db_session
def usersave():
    """ User data save into DB """
    array = []
    now = datetime.datetime.now()
    dni = request.params.get("dni")
    nombre = request.params.get("nombre")
    apellido = request.params.get("apellido")
    email = request.params.get("email")
    direccion = request.params.get("dir")
    ciudad = request.params.get("ciudad")
    codigopostal = request.params.get("cp")
    nvoucher = request.params.get("voucher")
    nidproducto = request.params.get("id")
    array.append(dni)
    array.append(nombre)
    array.append(apellido)
    array.append(email)
    array.append(direccion)
    array.append(ciudad)
    array.append(codigopostal)
    array.append(now)
    array.append(nvoucher)
    array.append(nidproducto)


    #Get all the objects from database
    clientes = select(p for p in Cliente)[:]
    result = {'data': [p.to_dict() for p in clientes]}

    # Get all the objects from DB and confirm if DNI
    # already exists.
    for i in result['data']:
        print(i['dni'])
        print(array[0])
        if str(i['dni']) == str(array[0]):
            return redirect('/already')

    # Validate Null spaces in textbox.
    c = 0
    save = 0
    for i in array:
        if i == "":
            c = c + 1
            if c == 7:
                return redirect('/complete')
                save = 0
        else:
            c = c + 1
            if c == 7:
                save = 1
          
    if save == 1:
        Cliente(dni=array[0], nombre=array[1],
                apellido=array[2], email=array[3],
                direccion=array[4],ciudad=array[5],
                codigoPostal=array[6],fechaRegistro=str(array[7]))
        theID = Cliente.get(dni=array[0]).id
        current_voucher = Voucher.get(codigovoucher=array[8])
        current_voucher.cliente = theID
        current_voucher.estado = 1
        current_voucher.producto = array[9]
        # Commit Cliente in to the DB
        commit()
        return redirect('/thanks')


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


@route('/confirm/<voucher>/<idx>', method=["GET"])
@view('confirm.tpl', template_lookup=['views'])
@db_session
def user_confirm_voucher(voucher, idx):

    if not voucher and not idx:
        return redirect('/voucher_need_and_id')

    data = []
    data.append(voucher)
    data.append(idx)

    return dict(context=data)

run(**settings['framework'])
