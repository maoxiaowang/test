
$(function () {

    var $gTree = $('#groupPermsTree');
    if ($gTree.length > 0) {
        /* detail page */

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

        // group users select
        $('#group_user_multi_select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionFooter: "<div class='text-muted font-13 m-t-10 text-center'>已加入{0}组的用户</div>".format(group_name),
            afterInit: function (ms) {
                var that = this,
                    $selectableSearch = that.$selectableUl.prev(),
                    $selectionSearch = that.$selectionUl.prev(),
                    selectableSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selectable:not(.ms-selected)',
                    selectionSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selection.ms-selected';

                that.qs1 = $selectableSearch.quicksearch(selectableSearchString)
                    .on('keydown', function (e) {
                        if (e.which === 40) {
                            that.$selectableUl.focus();
                            return false;
                        }
                    });

                that.qs2 = $selectionSearch.quicksearch(selectionSearchString)
                    .on('keydown', function (e) {
                        if (e.which == 40) {
                            that.$selectionUl.focus();
                            return false;
                        }
                    });
            },
            afterSelect: function () {
                this.qs1.cache();
                this.qs2.cache();
            },
            afterDeselect: function () {
                this.qs1.cache();
                this.qs2.cache();
            }
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

        // group user update
        $('#groupUserUpdateModal form').submit(function (event) {
            var $this = $(this);
            event.preventDefault();
            var selected_names = $this.find('.ms-selection li.ms-selected > span').map(
                function(){return $(this).text();}).get().join(' ');
            var data = [];
            $.each($('#group_user_multi_select option'), function (i, item) {
                if (selected_names.indexOf($(item).text()) >= 0) {
                    data.push($(item).val());
                }
            });
            $.addLoadingCover();
            $.ajax({
                url: $this.attr('action'),
                type: $this.attr('method'),
                data: {'user_ids': JSON.stringify(data)},
                success: function (res) {
                    res = $.handleResponse(res);
                    var newElem = '';
                    $.each(res.data, function (i, item) {
                        newElem +=
                            '<tr>\n' +
                            '  <td>{0}</td>\n'.format(item['username']) +
                            '  <td>{0}</td>\n'.format(item['email']) +
                            '  <td>{0}</td>\n'.format(item['is_active']) +
                            '  </tr>';
                    });
                    console.log(newElem);
                    $target = $('#groupUserCard tbody');
                    $target.html('');
                    $(newElem).hide().appendTo($target).fadeIn('slow');
                    $('#groupUserUpdateModal').modal('hide');
                },
                complete: function () {
                    $.removeLoadingCover();
                },
                error: function () {
                }
            });
        });
        //
        // // delete group
        // $('#groupDeleteModal form').submit(function (event) {
        //     var $this = $(this);
        //     event.preventDefault();
        //     $.addLoadingCover();
        //     $.ajax({
        //         url: $this.attr('action'),
        //         type: $this.attr('method'),
        //         success: function (res) {
        //             $.handleResponse(res);
        //             $('#groupDeleteModal').modal('hide');
        //         },
        //         complete: function () {
        //             $.removeLoadingCover();
        //         },
        //         error: function () {
        //         }
        //     });
        // });

    }


});

$(function () {

    // create group
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

});
