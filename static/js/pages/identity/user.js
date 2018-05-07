
$('#userCreateModal form').submit(function (event) {
    var $this = $(this);
    event.preventDefault();
    $.addLoadingCover();
    $.ajax({
        url: $this.attr('action'),
        data: $this.serialize(),
        type: $this.attr('method'),
        success: function (res) {
            res = $.handleResponse(res);
            if (res.result) {
                var newElem = '';
                $.each(res.data, function (i, item) {
                    var dateJoined = item['date_joined'] || '-';
                    var lastLogin = item['last_login'] || '-';
                    newElem +=
                        '<tr>\n' +
                        '  <td scope="row"><a href="{0}">{1}</a></td>\n'.format('/identity/user/detail/{0}/'.format(item['id']), item['username']) +
                        '  <td>{0}</td>\n'.format(item['email']) +
                        '  <td>{0}</td>\n'.format(dateJoined) +
                        '  <td>{0}</td>\n'.format(lastLogin) +
                        '</tr>';
                });

                $target = $('#userListCard tbody');
                $target.html('');
                $(newElem).hide().appendTo($target).fadeIn('slow');

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
                    'icon' : 'mdi mdi-note-multiple-outline'
                },
                'file' : {
                    'icon' : 'mdi mdi-note-outline'
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
