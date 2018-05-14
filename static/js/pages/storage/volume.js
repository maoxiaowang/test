// WebSocket

function initSocket(option) {

    var locate = window.location;
    var url = option.url ? option.url : "ws://" + locate.hostname + ":" + locate.port + '/ws' + locate.pathname;

    var callback = option.callback;
    if (typeof callback !== "function") {
        console.log('callback must be a function');
        return false;
    }

    var websocket = new ReconnectingWebSocket(url);

    websocket.onerror = function () {
        console.log("websocket.onerror");
    };

    websocket.onopen = function (event) {
        console.log("websocket.onopen");
        // var param = {
        //     id: $("#UserID").val(),
        //     name: $("#UserName").val(),
        //     act: "produceNewUser",
        //     msg: ""
        // };
        // websocket.send(JSON.stringify(param));
    };

    websocket.onmessage = function (event) {
        console.log('websocket.onmessage');
        callback(event.data);


    };

    websocket.onclose = function () {
        console.log("websocket.onclose");
        websocket.close();

    };

    //监听窗口关闭事件，当窗口关闭时，主动去关闭websocket连接，防止连接还没断开就关闭窗口，server端会抛异常。
    window.onbeforeunload = function () {
        websocket.close();
    };
    return websocket;
}

$(function () {
    var option = {
        // url: $("#socketAddress").val(),
        callback: function (res) {
            console.log(res);
            res = JSON.parse(res);
            if (res['result'] === true) {
                var data = res['data'];

                $('#volumeListCard');
            }
            var html = '';

            html += ('<tr class="tableCont bgcWhite bgcHover">');
            html += ('<td class="lef2 serial">' + b.ProduceSort + '</td>');
            html += ('<td class="mid">' + b.Color + '</td><td>' + b.WidthCloth + '</td><td>' + b.Weight + '</td><td>' + b.RollLength + '</td><td>' + b.Number + '</td>');
            html += ('<td class="mid">' + b.Comp + '</td>');
            html += ('<td><div class="nowProduce clearfix" onclick="UpProduction(' + b.ID + ',this)" sake="Up">上移生产</div> </td></tr>');

            $('#List').append(html);

        }
    };
    var socket = initSocket(option);

});