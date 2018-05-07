

// logout
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


// WebSocket

var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);



function initSocket(option) {
    //服务器地址
    var locate = window.location;
    var url = option.url ? option.url : "ws://" + locate.hostname + ":" + locate.port + _get_basepath() + "/websocket";
    //回调函数
    var callback = option.callback;
    if (typeof callback !== "function") {
        console.log('callback must be a function');
        return false;
    }
    //一些对浏览器的兼容已经在插件里面完成
    var websocket = new ReconnectingWebSocket(url);
    //var websocket = new WebSocket(url);

    //连接发生错误的回调方法
    websocket.onerror = function () {
        console.log("WebSocket error");
    };

    //连接成功建立的回调方法
    websocket.onopen = function (event) {
        console.log("onopen");
        var param = {
            id: $("#UserID").val(),
            name: $("#UserName").val(),
            act: "produceNewUser",
            msg: ""
        };
        websocket.send(JSON.stringify(param));
    };

    //接收到消息的回调方法
    websocket.onmessage = function (event) {
        callback(event.data);
    };

    //连接关闭的回调方法
    websocket.onclose = function () {
        websocket.close();
        console.log("websocket.onclose");
    };

    //监听窗口关闭事件，当窗口关闭时，主动去关闭websocket连接，防止连接还没断开就关闭窗口，server端会抛异常。
    window.onbeforeunload = function () {
        websocket.close();
    };
    return websocket;
}

$(function () {
    var option = {
        url: $("#socketAddress").val(),
        callback: function (data) {
            console.log(data);
            //处理业务逻辑
            var a = $.parseJSON(data);
            if (a.code !== 10) {
                return;
            }
            var b = $.parseJSON(a.content);

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
