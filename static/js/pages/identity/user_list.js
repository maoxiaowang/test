$(function () {

    $('#user-create-modal').on('shown.bs.modal', function () {
        $(this).find('#user-create-input-name').focus();
    });

    $('#user-create-modal form').submit(function (event) {
        var $this = $(this);
        event.preventDefault();
        $.addLoadingCover();
        $.ajax({
            url: $this.attr('action'),
            data: $this.serialize(),
            type: $this.attr('method'),
            success: function (res) {
                res = $.handleResponse(res, true);
            },
            complete: function () {
                $.removeLoadingCover();
            },
            error: function () {
            }
        });
    });
});