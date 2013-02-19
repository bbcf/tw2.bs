bs_init_file_field = function(compound_id, select){
    var selector = '#' + compound_id.split(':').join('\\:');
    var $root = $(selector + '\\:container');
    // hide not desired inputs
    $root.find('input:not(:radio):not(:' + select + ')').attr('name', '').hide();
    // show desired one
    $root.find('input:' + select + '').attr('name', compound_id).show();
    // check the right radio button
    $root.find('input:radio.bsradio_' + select).attr('checked', 'checked');
    //connect the radio buttons
    $root.find(':radio').change(function(){
        var val = $(this).val();
        $root.find('input:not(:radio):not(:'+ val + ')').attr('name', '').hide();
        $root.find('input:' + val + '').attr('name', compound_id).show();
    });
    // connect the values changes
     $root.find('input:not(:radio)').change(function(){
        $(selector).val($(this).val()).trigger("change");
        var row_id = compound_id.substring(0, compound_id.lastIndexOf(':'));
        var id_prefix = row_id.substring(0, row_id.lastIndexOf(':')+1);
        var id_end = compound_id.substring(compound_id.lastIndexOf(':')+1,  compound_id.length);
        var next_num = parseInt(row_id.substr(row_id.lastIndexOf(':')+1)) + 1;
        if (next_num){
            bs_init_file_field(id_prefix + next_num + ':' + id_end, select);
        }
     });
};

bs_init_triple_file_field = function(compound_id, select){
    var selector = '#' + compound_id.split(':').join('\\:');
    var $root = $(selector + '\\:container');
    if (select != 'select'){
        // hide select && show input desired
        $root.find('select').attr('name', '').hide();
        $root.find('input:' + select + '').attr('name', compound_id).show();
        // hide not desired inputs
        $root.find('input:not(:radio):not(:' + select + ')').attr('name', '').hide();
    } else {
        $root.find('input:not(:radio)').attr('name', '').hide();
    }
    // check the right radio button
    $root.find('input:radio.bsradio_' + select).attr('checked', 'checked');
    
    //connect the radio buttons
    $root.find(':radio').change(function(){
        var val = $(this).val();
        if (val == 'select'){
            $root.find('input:not(:radio)').attr('name', '').hide();
            $root.find('select').attr('name', compound_id).show();
        } else {
            $root.find('input:' + val).attr('name', compound_id).show();
            $root.find('select').attr('name', '').hide();
            $root.find('input:not(:radio):not(:' + val + ')').attr('name', '').hide();
        }
    });
    // connect the values changes
     $root.find('input:not(:radio), select').change(function(){
        $(selector).val($(this).val()).trigger("change");
        var row_id = compound_id.substring(0, compound_id.lastIndexOf(':'));
        var id_prefix = row_id.substring(0, row_id.lastIndexOf(':')+1);
        var id_end = compound_id.substring(compound_id.lastIndexOf(':')+1,  compound_id.length);
        var next_num = parseInt(row_id.substr(row_id.lastIndexOf(':')+1)) + 1;
        if (next_num){
            bs_init_triple_file_field(id_prefix + next_num + ':' +id_end, select);
        }
     });
};

