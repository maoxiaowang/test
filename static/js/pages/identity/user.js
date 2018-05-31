
$('#user-create-modal form').submit(function (event) {
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
                        '  <td scope="row"><a href="{0}">{1}</a></td>\n'.format(
                            '/identity/user/detail/{0}/'.format(item['id']), item['username']) +
                        '  <td>{0}</td>\n'.format(item['email']) +
                        '  <td>{0}</td>\n'.format(dateJoined) +
                        '  <td>{0}</td>\n'.format(lastLogin) +
                        '</tr>';
                });

                var $target = $('#user-list-card tbody');
                $target.html('');
                $(newElem).hide().appendTo($target).fadeIn('slow');

                $('#user-create-modal').modal('hide');
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

$('#user-detail-modal form').submit(function (event) {
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
                var newEmail = res.data['email'];
                $('#userEmail > span').text(newEmail);
                $('#user-detail-modal').modal('hide');
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
    var $gTree = $('#user-perms-tree');
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

        // user resources select
        $('#user-host-multi-select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionFooter: "<div class='text-muted font-13 m-t-10 text-center'>已分配给{0}的资源</div>".format(userName),
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
        $('#user-volume-multi-select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionFooter: "<div class='text-muted font-13 m-t-10 text-center'>已分配给{0}的资源</div>".format(userName),
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
        $('#user-instance-multi-select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionFooter: "<div class='text-muted font-13 m-t-10 text-center'>已分配给{0}的资源</div>".format(userName),
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
        $('#user-perms-update-btn').click(function () {
            var data = $gTree.jstree().get_checked();
            var jsonData = JSON.stringify(data);
            $.addLoadingCover();
            $.ajax({
                url: userGlobalPermsUrl,
                data: {'checked_perms': jsonData},
                type: 'POST',
                success: function (res) {
                    $.handleResponse(res);
                    $('#user-global-perms-modal').modal('hide');
                },
                complete: function () {
                    $.removeLoadingCover();
                }
            });

        });
    }

});
