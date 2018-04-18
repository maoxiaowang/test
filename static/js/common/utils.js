/**
不常用工具集
 */


// 判断字符串长度，非ASCII算两个长度
function getStringLen(str) {
    if (str === null) return 0;
    if (typeof str !== "string"){
        str += "";
    }
    return str.replace(/[^\x00-\xff]/g,"01").length;
}


/*
给任意元素添加Material tooltip
只有鼠标指向的时候才会显示
showTooltip({
            target: $usernameOrEmail,
            tooltip: '用户名/邮箱不能为空'
        })
 */
function showTooltip(settings) {
    console.log(settings);
    var defaultSetting={
        target: null,
        tooltip: '',
        position: 'bottom',
        html: false,
        delay: 350
    };
    var _properties = ['target', 'tooltip', 'position', 'html', 'delay'];
    $.each(Object.keys(settings), function (i, item) {
        if ($.inArray(item, _properties) < 0) {
            throw 'Invalid settings key "' + item + '"';
        }
    });
    $.extend(defaultSetting, settings);
    var $obj = getJQueryObject(settings.target);
    if (!$obj) {
        throw 'target is unknown';
    }
    $obj.tooltip({
        tooltip: settings.tooltip,
        delay: settings.delay,
        position: settings.position,
        html: settings.html
    });

    // remove
    // $obj.tooltip('remove');", 2000);
}

function getRelativeUrl(url, params) {
    var _url = url ? url : window.location.href;
    var _params = params ? params : false;
    var resUrl;
    var res = /^https?:\/\/.*?(\/[^?]*\/)(.*)$/.exec(_url);
    if (res.length == 3) {
        if (_params) {
            resUrl = res[1] + res[2];
        } else {
            resUrl = res[1];
        }

    }
    return resUrl;
}
