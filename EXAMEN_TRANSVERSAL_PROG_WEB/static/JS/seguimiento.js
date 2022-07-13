var ordenes= [
    {nombre:"Producto Uno" , estado:"enviado", clase:"estadoVerde"},
    {nombre:"Producto Dos" , estado:"en camino",clase:"estadoAzul"},
    {nombre:"Producto Tres" , estado:"entregado",clase:"estadoPurpura"},
  ]
  
  
  var acomulador_texto=""
  
  ordenes.forEach((element, index) => {
  
      var html_producto = `
      <tr>
        <th scope="row">${index}</th>
        <td>${element.nombre}</td>
        <td class="${element.clase}">${element.estado}</td>
      </tr>`
      
      acomulador_texto += html_producto
      $("#seguimiento").html( acomulador_texto )
  });

const lista_plantas = [];