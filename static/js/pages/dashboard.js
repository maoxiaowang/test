

// logout
// $('.side-menu #user-logout').click(function () {
//     $.addLoadingCover();
//     $.ajax({
//         url: logout_url,
//         type: 'POST',
//         success: function (res) {
//             toastr.success('Logout succeeded! Reload after 3s');
//             setTimeout(function () {
//                 window.location.reload();
//             }, 3000)
//         }
//
//     })
// });

// SweetAlert
!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    SweetAlert.prototype.init = function () {

        //Warning Message
        $('.side-menu #user-logout').click(function () {
            Swal({
                title: 'Are you sure?',
                text: "You will log out from the system",
                type: 'warning',
                showCancelButton: true,
                // confirmButtonColor: '#4fa7f3',
                // cancelButtonColor: '#d57171',
                confirmButtonText: 'Yes, log out',
                confirmButtonClass: 'btn btn-danger m-l-10',
                cancelButtonClass: 'btn btn-success'
            }).then(function (result) {
                if (result.value) {
                    $.addLoadingCover();
                    $.ajax({
                        url: logoutUrl,
                        type: 'POST',
                        success: function (res) {
                            if (res.messages.length > 0) {
                                $.handleResponse(res);
                            } else {window.location.reload();}
                        }
                    });
                } else if (result.dismiss === Swal.DismissReason.cancel) {}

            });
        });
    };
    //init
    $.SweetAlert = new SweetAlert;
    $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);