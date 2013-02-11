bs_hide_fields = function(){
    $('.bs_file_container').each(function(){
        var $this = $(this);
        var fupload =  $this.find('.bs_file_fileupload');
        var furl = $this.find('.bs_file_url');
        $this.attr('choice', 'fupload');
        furl.hide();
        furl.find('.bs_textinput').val('http://');
        furl.find('input:checkbox').click(function(){
            $(this).attr('checked', false);
            fupload.toggle();
            furl.toggle();
            $this.attr('choice', 'fupload');
        });
        fupload.find('input:checkbox').click(function(){
            $(this).attr('checked', false);
            fupload.toggle();
            furl.toggle();
            $this.attr('choice', 'furl');
        });
    });
    
};

