<html>
  <head>
    </head>
    <body>
<h3>Seleccione un producto:</h3>

<table>
  <tr>
    <th>Producto: {{ context.data.0.titulo }} </th>
    <th>Producto: {{ context.data.1.titulo }}</th>
  </tr>
  <tr>
    <td>Descripcion: {{ context.data.0.descripcion }} </td>
    <td>Descripcion: {{ context.data.1.descripcion }} </td>
  </tr>
  <tr>
      
    <td><img src="http://localhost:8080/static/css/images/bag.jpg" alt="My Bag" width="500" height="333"></td>
    <td><img src="http://localhost:8080/static/css/images/spacex.jpg" alt="Italian Trulli" width="500" height="333"></td>
    
  </tr>
  <tr>
    <td><a href="/confirm/{{ context.voucher }}/{{ context.data.0.id }}"><button id="1">select</button></a></td>
    <td><a href="/confirm/{{ context.voucher }}/{{ context.data.1.id }}"><button id="2">select</button></a></td>
  </tr>
</table>

<h5>Voucher asociado: {{ context.voucher }}</h5>
</body>
</html>