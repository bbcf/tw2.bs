bs_init_file_field = function(compound_id, select){
    var selector = '#' + compound_id.split(':').join('\\:');
    var $todelspan = $('span' + selector);
    var oc = $todelspan.attr('onchange');
    $todelspan.remove();
    var $root = $(selector);
    // hide not desired inputs
    $root.find('input:not(:radio):not(:' + select + ')').attr('name', '').hide();
    // show desired one
    $root.find('input:' + select + '').attr('name', compound_id).show();
    $root.find('input:' + select + '').attr('onchange', oc);
    // check the right radio button
    $root.find('input:radio.bsradio_' + select).attr('checked', 'checked');
    //connect the radio buttons
    $root.find(':radio').change(function(){
        var val = $(this).val();
        $root.find('input:not(:radio):not(:'+ val + ')').attr('name', '').hide();
        $root.find('input:' + val + '').attr('name', compound_id).show();
        $root.find('input:' + val + '').attr('onchange', oc);
    });
};

bs_init_triple_file_field = function(compound_id, select){
    var selector = '#' + compound_id.split(':').join('\\:');
    var $todelspan = $('span' + selector);
    var oc = $todelspan.attr('onchange');
    $todelspan.remove();
    var $root = $(selector);
    console.log(selector);
    if (select != 'select'){
        // hide select && show input desired
        $root.find('select').attr('name', '').hide();
        $root.find('input:' + select + '').attr('name', compound_id).show();
        $root.find('input:' + select + '').attr('onchange', oc);
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
            $root.find('select').attr('onchange', oc);
        } else {
            $root.find('input:' + val).attr('name', compound_id).show();
            $root.find('input:' + val + '').attr('onchange', oc);
            $root.find('select').attr('name', '').hide();
            $root.find('input:not(:radio):not(:' + val + ')').attr('name', '').hide();
        }
    });
};

bs_init_multiple = function(compound_id){

};