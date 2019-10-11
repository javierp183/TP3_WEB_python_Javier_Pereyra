{% include "head.tpl" %}

<h1>Seleccione un producto:</h1>

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
    <td><img src="https://ecoinventos.com/wp-content/uploads/2018/03/mochila-sunpack.jpg" alt="Italian Trulli" width="500" height="333"></td>
    <td><img src="https://fsmedia.imgix.net/5a/ef/61/78/7ca8/4a16/9612/1d9d772d07b4/an-artists-rendering-of-the-spacex-crew-dragon.jpeg?crop=edges&fit=crop&auto=format%2Ccompress&dpr=2&h=325&w=650" alt="Italian Trulli" width="500" height="333"></td>
  </tr>
  <tr>
    <td><a href="/confirm/{{ context.voucher }}/{{ context.data.0.id }}"><button id="1">select</button></a></td>
    <td><a href="/confirm/{{ context.voucher }}/{{ context.data.1.id }}"><button id="2">select</button></a></td>
  </tr>
</table>


<h5>Voucher asociado: {{ context.voucher }}</h5>


{% include "foot.tpl" %}