bs_hide_fields = function(compound_id){
    var selector = '#' + compound_id.replace(':', '\\:');
    var $root = $(selector);
    console.log(selector);
    var label = $root.next('label');
    label.old_input = '<input id="' + compound_id + '" name="' + compound_id + '" type="text"/>';
    label.old_label = '<label><input type="checkbox" name="checkbox" value="value" />File upload</label>';
    bs_connect_checkbox(selector, $root, label);
};

bs_connect_checkbox = function(selector, input, label){
    console.log('bs_connect');
    console.log(input);
    console.log(label);
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



// bs_hide_fields = function(compound_id){
//     var selector = '#' + compound_id.replace(':', '\\:');
//     var $root = $(selector);
//     var fupload =  $this.find('.bs_file_fileupload');
//     var furl = $this.find('.bs_file_url');
//     $this.attr('choice', 'fupload');
//     furl.hide();
//     furl.find('.bs_textinput').val('http://');
//     furl.find('input:checkbox').click(function(){
//         $(this).attr('checked', false);
//         fupload.toggle();
//         furl.toggle();
//         $this.attr('choice', 'fupload');
//     });
//     fupload.find('input:checkbox').click(function(){
//         $(this).attr('checked', false);
//         fupload.toggle();
//         furl.toggle();
//         $this.attr('choice', 'furl');
//     });
// };

