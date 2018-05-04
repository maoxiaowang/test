
$('#userCreateModal form').submit(function (event) {
    var $this = $(this);
    event.preventDefault();
    $.addLoadingCover();
    $.ajax({
        url: $this.attr('action'),
        data: $this.serialize(),
        type: $this.attr('method'),
        success: function (res) {
            $.handleResponse(res);
            if (res.result) {
                $('#userCreateModal').modal('hide');
                $.cleanFormInput($this);
            }
        },
        complete: function () {

            $.removeLoadingCover();
        },
        error: function () {
        }
    });
});

$(function () {
    var $gTree = $('#userPermsTree');
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
        $('#userPermsBtn').click(function () {
            var data = $gTree.jstree().get_checked();
            var jsonData = JSON.stringify(data);
            $.addLoadingCover();
            $.ajax({
                url: user_perms_update_url,
                data: {'checked_perms': jsonData},
                type: 'POST',
                success: function (res) {
                   $.handleResponse(res);
                   $('#userPermsUpdateModal').modal('hide');
                },
                complete: function () {
                    $.removeLoadingCover();
                }
            })

        });
    }

});
