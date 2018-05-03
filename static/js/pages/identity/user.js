
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
            }
        },
        complete: function () {
            $.cleanFormInput($this);
            $.removeLoadingCover();
        },
        error: function () {
        }
    });
});
