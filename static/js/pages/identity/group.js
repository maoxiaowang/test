
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
    // detail page
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


        // group users
        $('#group_user_multi_select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectableFooter: "<div class='text-muted font-13 m-t-10 text-center'>可选用户</div>",
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
    }

});
