{% include "head.tpl" %}

<form action="" id="userdata" method="POST">
  DNI<br>
  <input type="text" name="dni" value="Ingrese DNI">
  <br>
  Nombre<br>
  <input type="text" name="nombre" value="Ingrese Nombre">
  <br>
  Apellido<br>
  <input type="text" name="apellido" value="Ingrese Apellido">
  <br>
  Email<br>
  <input type="text" name="email" value="Ingrese Email">
  <br>
  Direccion<br>
  <input type="text" name="direccion" value="Ingrese Direccion">
  <br>
  Ciudad<br>
  <input type="text" name="ciudad" value="Ingrese Ciudad">
  <br>
  Codigo Postal<br>
  <input type="text" name="cp" value="Ingrese Codigo Postal">
  <br>
  Acepta terminos y condiciones?
  <input type="radio" name="terminos" value="1">
  <br><br>
  <input type="submit" value="Submit">
</form> 

{% include "foot.tpl" %}