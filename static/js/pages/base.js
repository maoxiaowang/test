
/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        // CommonJS
        factory(require('jquery'));
    } else {
        // Browser globals
        factory(jQuery);
    }
}(function ($) {

    var pluses = /\+/g;

    function encode(s) {
        return config.raw ? s : encodeURIComponent(s);
    }

    function decode(s) {
        return config.raw ? s : decodeURIComponent(s);
    }

    function stringifyCookieValue(value) {
        return encode(config.json ? JSON.stringify(value) : String(value));
    }

    function parseCookieValue(s) {
        if (s.indexOf('"') === 0) {
            // This is a quoted cookie as according to RFC2068, unescape...
            s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
        }

        try {
            // Replace server-side written pluses with spaces.
            // If we can't decode the cookie, ignore it, it's unusable.
            // If we can't parse the cookie, ignore it, it's unusable.
            s = decodeURIComponent(s.replace(pluses, ' '));
            return config.json ? JSON.parse(s) : s;
        } catch(e) {}
    }

    function read(s, converter) {
        var value = config.raw ? s : parseCookieValue(s);
        return $.isFunction(converter) ? converter(value) : value;
    }

    var config = $.cookie = function (key, value, options) {

        // Write

        if (value !== undefined && !$.isFunction(value)) {
            options = $.extend({}, config.defaults, options);

            if (typeof options.expires === 'number') {
                var days = options.expires, t = options.expires = new Date();
                t.setTime(+t + days * 864e+5);
            }

            return (document.cookie = [
                encode(key), '=', stringifyCookieValue(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path    ? '; path=' + options.path : '',
                options.domain  ? '; domain=' + options.domain : '',
                options.secure  ? '; secure' : ''
            ].join(''));
        }

        // Read

        var result = key ? undefined : {};

        // To prevent the for loop in the first place assign an empty array
        // in case there are no cookies at all. Also prevents odd result when
        // calling $.cookie().
        var cookies = document.cookie ? document.cookie.split('; ') : [];

        for (var i = 0, l = cookies.length; i < l; i++) {
            var parts = cookies[i].split('=');
            var name = decode(parts.shift());
            var cookie = parts.join('=');

            if (key && key === name) {
                // If second argument (value) is a function it's a converter...
                result = read(cookie, value);
                break;
            }

            // Prevent storing a cookie that we couldn't decode.
            if (!key && (cookie = read(cookie)) !== undefined) {
                result[name] = cookie;
            }
        }

        return result;
    };

    config.defaults = {};

    $.removeCookie = function (key, options) {
        if ($.cookie(key) === undefined) {
            return false;
        }

        // Must not alter options, thus extending a fresh object...
        $.cookie(key, '', $.extend({}, options, { expires: -1 }));
        return !$.cookie(key);
    };

}));


// CSRF for ajax
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = $.cookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// dom及jquery对象
function isDomObject(obj){
    return ( typeof HTMLElement === 'object' ) ?
        function(obj){
            return obj instanceof HTMLElement;
        } :
        function(obj){
            return obj && typeof obj === 'object'
                && obj.nodeType === 1
                && typeof obj.nodeName === 'string';
        };
}

function isJQueryObject(obj){
    return obj instanceof jQuery;
}

function getJQueryObject(obj){
    obj = typeof obj === 'string' ? $(obj) : obj;
    if(isDomObject(obj)) {
        return  $(obj);
    } else if (isJQueryObject(obj)) {
        return obj;
    }
    return null;
}

function getDomObject(obj){
    // Only support id, class, tag name
    if (typeof obj === 'string') {
        if (obj.split(' ').length === 1) {
            if (obj.indexOf('#') === 0) {
                return document.getElementById(obj);
            } else if (obj.indexOf('.')) {
                return document.getElementsByClassName(obj);
            } else {
                // TODO: other situation
                document.getElementsByTagName(obj);
            }
        }
    } else if (isDomObject(obj)) {
        return  obj;
    } else if (isJQueryObject(obj)) {
        return obj.get(0);
    }
    return null;
}

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

// string format
String.prototype.format = function () {
    var values = arguments;
    return this.replace(/{(\d+)}/g, function (match, index) {
        if (values.length > index) {
            return values[index];
        } else {
            return "";
        }
    });
};

// jQuery def
(function ($) {
    $.addLoadingCover = function (obj) {
        var loadingHtml =
            '<div id="loadingCover">\n' +
            '  <div>\n' +
            '    <div class="col align-self-center">\n' +
            '      <img src="{0}">\n'.format(loadingImageUrl) +
            '    </div>\n' +
            '  </div>\n' +
            '</div>';
        var _obj = obj || 'body';
        var $parent_elem = getJQueryObject(_obj);
        $(loadingHtml).hide().appendTo($parent_elem).fadeIn('slow');
    };
    $.removeLoadingCover = function (obj) {
        var _obj = obj ? obj : 'body';
        var $parent_elem = getJQueryObject(_obj);
        $parent_elem.children('#loadingCover').fadeOut('fast').remove();
    };

    $.cleanFormInput = function ($form) {
        $.each(($form.find('input')), function (i, item) {
            if ($(item).val()) {
                $(item).val('');
            }
        });
    };

    $.handleResponse = function (res, reload) {
        if (res) {
            console.log(res);
            if (!(res instanceof Object)) {
                try {
                    res = $.parseJSON(res);
                } catch (e) {return res;}
            }

            if (res.result && reload) {
                // reload page
                console.log('reload');
                window.location.reload();

            } else {
                $.each(res.messages, function (i, item) {
                    switch (res.level) {
                        case 'success':
                            toastr.success(item);
                            break;
                        case 'info':
                            toastr.info(item);
                            break;
                        case 'warning':
                            toastr.warning(item);
                            break;
                        case 'error':
                            toastr.error(item);
                            break;
                    }
                });
                return res;
            }

        }

    };

    $.getUrlParams = function () {
        var pat = /^https?:\/\/.*\/\?(.*)$/;
        var l = pat.exec(window.location.href);
        if (l !== null) return decodeURI(l[1]); return null;
    };
    $.getUrlParam = function (name) {
        var params = $.getUrlParams();
        if (params) {
            var result = null;
            $.each(params.split('&'), function (i, item) {
                var s = item.split('=');
                if (s.length > 1 && name === s[0]) {
                    result = decodeURI(s[1]);
                    return false;
                }
            });
            return result;
        }
        return null;
    }
})(jQuery);


// ready to load
$(function () {
        // handle django messages
        var $messages = $('ul.messages');
        if ($messages.length > 0) {
            $.each($messages.find('li.message'), function (i, item) {
                var level = $(item).attr('data-message-level');
                var msg = $(item).text();
                switch (level) {
                    case 'success':
                        toastr.success(msg);
                        break;
                    case 'info':case 'debug':
                    toastr.info(msg);
                    break;
                    case 'warning':
                        toastr.warning(msg);
                        break;
                    case 'error':
                        toastr.error(msg);
                        break;
                }
            });
            $messages.remove();
        }
    }
);


