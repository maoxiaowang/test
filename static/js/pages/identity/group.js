
$(function () {

    var $groupListCardBox = $('#group-list-card-box');
    var $groupDetailCardBox = $('#group-detail-card-box');
    if ($groupListCardBox.length > 0) {

        $('#group-create-modal').on('shown.bs.modal', function () {
            $(this).find('#group-create-input-name').focus();
        });

        // create group
        $('#group-create-modal form').submit(function (event) {
            var $this = $(this);
            event.preventDefault();
            $.addLoadingCover();
            $.ajax({
                url: $this.attr('action'),
                data: $this.serialize(),
                type: $this.attr('method'),
                success: function (res) {
                    $.handleResponse(res, true);
                    // $('#group-create-modal').modal('hide');
                },
                complete: function () {
                    $.cleanFormInput($this);
                    $.removeLoadingCover();
                },
                error: function () {
                }
            });
        });
    } else if ($groupDetailCardBox.length > 0) {
        var $gTree = $('#group-perms-tree');
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

        // group users select
        $('#group-user-multi-select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionFooter: "<div class='text-muted font-13 m-t-10 text-center'>已加入{0}组的用户</div>".format(groupName),
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
                        if (e.which === 40) {
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
        $('#group-perms-update-btn').click(function () {
            var data = $gTree.jstree().get_checked();
            var jsonData = JSON.stringify(data);
            $.addLoadingCover();
            $.ajax({
                url: groupPermsUpdateUrl,
                data: {'checked_perms': jsonData},
                type: 'POST',
                success: function (res) {
                    $.handleResponse(res, true);
                },
                complete: function () {
                    $.removeLoadingCover();
                }
            })

        });

        // group user update
        $('#group-user-update-modal form').submit(function (event) {
            var $this = $(this);
            event.preventDefault();
            var selected_names = $this.find('.ms-selection li.ms-selected > span').map(
                function(){return $(this).text();}).get().join(' ');
            var data = [];
            $.each($('#group-user-multi-select option'), function (i, item) {
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
                    res = $.handleResponse(res, true);
                    // var newElem = '';
                    // $.each(res.data, function (i, item) {
                    //     newElem +=
                    //         '<tr>\n' +
                    //         '  <td>{0}</td>\n'.format(item['username']) +
                    //         '  <td>{0}</td>\n'.format(item['email']) +
                    //         '  <td>{0}</td>\n'.format(item['is_active']) +
                    //         '</tr>';
                    // });
                    //
                    // $target = $('#group-user-card tbody');
                    // $target.html('');
                    // $(newElem).hide().appendTo($target).fadeIn('slow');
                    if (res.result) {
                        $('#group-user-update-modal').modal('hide');
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

        // delete group
        // $('#group-delete-modal form').submit(function (event) {
        //     var $this = $(this);
        //     event.preventDefault();
        //     $.addLoadingCover();
        //     $.ajax({
        //         url: $this.attr('action'),
        //         type: $this.attr('method'),
        //         success: function (res) {
        //             $.handleResponse(res, groupListUrl);
        //             // $('#group-delete-modal').modal('hide');
        //         },
        //         complete: function () {
        //             $.removeLoadingCover();
        //         },
        //         error: function () {
        //         }
        //     });
        // });
        $('#delete-group').click(function (event) {
            Swal({
                title: 'Are you sure?',
                text: "Group {0} will be deleted, and all users will be removed out of the group!".format(userName),
                type: 'warning',
                showCancelButton: true,
                // confirmButtonColor: '#4fa7f3',
                // cancelButtonColor: '#d57171',
                confirmButtonText: 'Yes, delete it.',
                confirmButtonClass: 'btn btn-danger m-l-10',
                cancelButtonClass: 'btn btn-success'
            }).then(function (result) {
                if (result.value) {
                    $.addLoadingCover();
                    $.ajax({
                        url: userDeleteUrl,
                        type: 'POST',
                        success: function (res) {
                            $.handleResponse(res, userListUrl);
                        }
                    });
                } else if (result.dismiss === Swal.DismissReason.cancel) {}

            });
        });
    }

});
