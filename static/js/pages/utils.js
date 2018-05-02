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


function getRelativeUrl(url, params) {
    var _url = url ? url : window.location.href;
    var _params = params ? params : false;
    var resUrl;
    var res = /^https?:\/\/.*?(\/[^?]*\/)(.*)$/.exec(_url);
    if (res.length === 3) {
        if (_params) {
            resUrl = res[1] + res[2];
        } else {
            resUrl = res[1];
        }

    }
    return resUrl;
}
