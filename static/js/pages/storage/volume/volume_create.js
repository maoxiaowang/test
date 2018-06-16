$(function () {
    var $volumeAddCard = $('#volume-create-card');

    // init TouchSpin
    $("input[name='number']").TouchSpin({
        min: 1,
        max: 100,
        step: 1,
        decimals: 0,
        boostat: 5,
        maxboostedstep: 10,
        buttondown_class: "btn btn-primary",
        buttonup_class: "btn btn-primary",
        postfix: ''
    });
    $("input[name='capacity']").TouchSpin({
        min: 1,
        max: 1024,
        step: 1,
        decimals: 0,
        boostat: 5,
        maxboostedstep: 10,
        buttondown_class: "btn btn-primary",
        buttonup_class: "btn btn-primary",
        postfix: 'GB'
    });
});