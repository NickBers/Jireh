var tblProducts;
var vents = {   
    items : {
        cliente: '',
        created:'',
        subtotal:'',
        iva:'',
        total:'',
        products:[]
    },
    calculate_invoice: function () {
        var subtotal=0.00;
        var iva = 0.16;
        $.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;
        $('input[name="subtotal"]').val(this.items.subtotal)
        $('input[name="total"]').val(this.items.total);
        
    },
    add:function (item){        
        this.items.products.push(item);
        this.list()
    },
    list: function () {
        this.calculate_invoice();
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "nombre"},
                {"data": "categoria.nombre"},
                {"data": "pvp"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-times"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm" autocomplete="off" value="'+row.cant+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row,data,displayNum,displayIndex,dataIndex){
                $(row).find('input[name="cant"]');
            },
            initComplete: function (settings, json) {

            }
        });
    },
};
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#created').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        minDate: moment().format("YYYY-MM-DD")
    });
    $('input[name="search"]').autocomplete({
        source: function (request,response){
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data:{
                    'action':'search_products',
                    'term':request.term
                },
                dataType: 'json',
            }).done(function(data){
                response(data);
            }).fail(function(jqXHR,textStatus, errorTrown){

            }).always(function(data){

            });
        },
        delay: 500,
        minLenght:1,
        select: function(event,ui){
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            ui.item.total = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');
        }
    });
    $('#tblProducts tbody').on('change','input[name="cant"]', function(){
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        //var data = tblProducts.row(tr.row).data();
        vents.items.products[tr.row].cant = cant;
        console.log(vents.items.products);  
        vents.calculate_invoice();  
        $('td:eq(5)',tblProducts.row(tr.row).node()).html('$'+vents.items.products[tr.row].subtotal);  
    });
});