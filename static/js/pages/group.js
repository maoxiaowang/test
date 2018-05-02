
$('#groupCreateModal form').submit(function (event) {
    var $this = $(this);
    event.preventDefault();
    if ($.formInputEmpty($this)) return false;
    $.addLoadingCover();
    $.ajax({
        url: $this.attr('action'),
        data: $this.serialize(),
        type: $this.attr('method'),
        success: function (res) {
            if (!(res instanceof Object)) {
                res = $.parseJSON(res);
            }
            $.each(res.messages, function (i, item) {
                if (res.result) {toastr.success(item);} else {toastr.error(item);}
            });
        },
        complete: function () {
            $('#groupCreateModal').modal('hide');
            $.cleanFormInput($this);
            $.removeLoadingCover();
        },
        error: function () {
        }
    });
});


$(function () {
    var $groupPermsTree = $('#groupPermsTree');
    if ($groupPermsTree.length > 0) {
        $groupPermsTree.jstree({
        'core' : {
            'themes' : {
                'responsive': false
            }
        },
        'types' : {
            'default' : {
                'icon' : 'fa fa-folder'
            },
            'file' : {
                'icon' : 'fa fa-file'
            }
        },
        'plugins' : ['types', 'checkbox']
    });
    }

});
