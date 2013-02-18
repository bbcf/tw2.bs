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
         $(selector).val($(this).val());
     });
};

bs_init_triple_file_field = function(compound_id, select){
    var selector = '#' + compound_id.split(':').join('\\:');
    var $root = $(selector + '\\:container');
    console.log(selector);
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
         $(selector).val($(this).val());
     });
};

