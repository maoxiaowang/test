
$('#groupCreateModal form').submit(function (event) {
    var $this = $(this);
    event.preventDefault();
    $.addLoadingCover();
    $.ajax({
        url: $this.attr('action'),
        data: $this.serialize(),
        type: $this.attr('method'),
        success: function (res) {
            $.handleResponse(res);
            $('#groupCreateModal').modal('hide');
        },
        complete: function () {
            $.cleanFormInput($this);
            $.removeLoadingCover();
        },
        error: function () {
        }
    });
});


$(function () {
    var $gTree = $('#groupPermsTree');
    if ($gTree.length > 0) {
        // init jstree
        $gTree.jstree({
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

        // change group permissions
        $('#groupPermsBtn').click(function () {
            var data = $gTree.jstree().get_checked();
            var jsonData = JSON.stringify(data);
            $.addLoadingCover();
            $.ajax({
                url: group_perms_update_url,
                data: {'checked_perms': jsonData},
                type: 'POST',
                success: function (res) {
                   $.handleResponse(res);
                   $('#groupPermsUpdateModal').modal('hide');
                },
                complete: function () {
                    $.removeLoadingCover();
                }
            })

        });
    }

});
