{% include "head.tpl" %}



<h4>Ingrese sus datos personales para participar</h4>

<form action="/usersave", method="POST">
  DNI:<br>
  <input type="text" name="dni">
</br>
  NOMBRE:
  <br>
  <input type="text" name="nombre">
</br>
  APELLIDO:<br>
  <input type="text" name="apellido">
</br>
  EMAIL:<br>
  <input type="text" name="email">
</br>
  DIRECCION:<br>
  <input type="text" name="dir">
</br>
  CIUDAD:<br>
  <input type="text" name="ciudad">
</br>
  CODIGO POSTAL:
  <br>
  <input type="text" name="cp">
</br>
  Codigo de Voucher:
  <br>
  <input type="text" name="voucher" value="{{context.0}}" readonly>
  </br>
  Producto:
  <br>
    <input type="text" name="id" value="{{context.1}}" readonly>
  </br>
  <input type="submit" value="Submit" value=" ">
</form>

{% include "foot.tpl" %}