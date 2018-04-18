/**
所有页面或很多页面都会用到
 */

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


function addLoadingCover(obj) {
    /*
     Append a loading cover to an object
     */
    var loading_html = '<div class="row loading-cover center valign-wrapper">\n' +
        '  <div class="col s12">' +
        '    <div class="preloader-wrapper active">\n' +
        '      <div class="spinner-layer spinner-red-only">\n' +
        '        <div class="circle-clipper left">\n' +
        '          <div class="circle"></div>\n' +
        '        </div><div class="gap-patch">\n' +
        '          <div class="circle"></div>\n' +
        '        </div><div class="circle-clipper right">\n' +
        '          <div class="circle"></div>\n' +
        '        </div>\n' +
        '      </div>\n' +
        '    </div>\n' +
        '  </div>\n' +
        '</div>';
    var _obj = obj || 'body';
    var $parent_elem = getJQueryObject(_obj);
    $(loading_html).hide().appendTo($parent_elem).fadeIn('slow');
}

function removeLoadingCover(obj) {
    var _obj = obj ? obj : 'body';
    var $parent_elem = getJQueryObject(_obj);
    $parent_elem.children('.loading-cover').fadeOut('fast').remove();
}


// url parameters
(function ($) {
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
