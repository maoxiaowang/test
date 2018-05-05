
$('.side-menu #userLogout').click(function () {
    $.addLoadingCover();
    $.ajax({
        url: logout_url,
        type: 'POST',
        success: function (res) {
            toastr.success('Logout succeeded! Reload after 3s');
            setTimeout(function () {
                window.location.reload();
            }, 3000)
        }

    })
});