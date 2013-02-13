bs_init_file_field = function(compound_id){
    var selector = '#' + compound_id.replace(':', '\\:');
    var $root = $(selector);
    console.log(selector);
    var label = $root.next('label');
    label.old_input = '<input id="' + compound_id + '" name="' + compound_id + '" type="file"/>';
    label.old_label = '<label><input type="checkbox" name="checkbox" value="value" />Url</label>';
    bs_connect_checkbox(selector, $root, label);
};

bs_connect_checkbox = function(selector, input, label){
    var cb = $(label).find('input:checkbox');
    $(cb).click(function(){
        var ninput = label.old_input;
        var nlabel = label.old_label;
        input.replaceWith(ninput);
        label.replaceWith(nlabel);
        $label = $(selector).next('label');
        $label.old_label = label;
        $label.old_input = input;
        $(this).attr('checked', false);
        bs_connect_checkbox(selector, $(selector), $label);
    });

};