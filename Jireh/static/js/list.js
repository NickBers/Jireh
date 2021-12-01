$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "nombre","orderData":3},
            {"data": "apellido"},
            {"data": "empresa"},
            {"data": "acc"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="proveedor/update/' + row.id + '/" class="btn btn-info btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="proveedor/delete/' + row.id + '/" type="button" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a type="button" class="btn btn-warning btn-sm btn-flat btnModal" data-target="#myModal"><i class="fas fa-search"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
    $('#newdata').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "nombre","orderData":3},
            {"data": "apellido"},
            {"data": "empresa"},
            {"data": "acc"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="proveedor/update/' + row.id + '/" class="btn btn-info btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="proveedor/delete/' + row.id + '/" type="button" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a type="button" class="btn btn-warning btn-sm btn-flat btnModal" data-target="#modalProveedor" data-toggle="modal"><i class="fas fa-search"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
        $('btnModal').on('click',function(){
            $('#modalProveedor').modal('show');
        });

});
   