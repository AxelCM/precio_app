<script type="text/javascript">
$(function () {
  $('#TableResult').DataTable({
    responsive:true,
    language: 'lan_es',
    ordering: 'false',
        });
    });

    $(function () {
      $('#TableResult2').DataTable({
        responsive:true,
        autoWidth: true,
        ordering: false,

        "language": lan_es,
        } );
    } );

    function toggle(){
      checkboxes = document.getElementsByName('id');
      validator = document.getElementById('validator');
      for(var i=0, n=checkboxes.length;i<n;i++) {
        checkboxes[i].checked = validator.checked;

      }
    }


    var lan_es =
    {
    "sProcessing":     "Procesando...",
    "sLengthMenu":     "Mostrar _MENU_ registros",
    "sZeroRecords":    "No se encontraron resultados",
    "sEmptyTable":     "Ningún dato disponible en esta tabla",
    "sInfo":           "Mostrando registros del _START_ al _END_  de _TOTAL_ registros",
    "sInfoEmpty":      "Mostrando 0 registros",
    "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
    "sInfoPostFix":    "",
    "sSearch":         "Buscar:",
    "sUrl":            "",
    "sInfoThousands":  ",",
    "sLoadingRecords": "Cargando...",
    "oPaginate": {
        "sFirst":    "Primero",
        "sLast":     "Último",
        "sNext":     "Siguiente",
        "sPrevious": "Anterior"
    },
    "oAria": {
        "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
    }
}
