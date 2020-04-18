window = this;
navigator = {
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
};

function base64encode(e) {
    var a, c, r, o, t, n;
    for (r = e.length - 1, c = 0, a = ""; c < r;) {
        if (o = 255 & e.charCodeAt(c++), c == r) {
            a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4), a += "==";
            break
        }
        if (t = e.charCodeAt(c++), c == r) {
            a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4 | (240 & t) >> 4), a += base64EncodeChars.charAt((15 & t) << 2), a += "=";
            break
        }
        n = e.charCodeAt(c++), a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4 | (240 & t) >> 4), a += base64EncodeChars.charAt((15 & t) << 2 | (192 & n) >> 6), a += base64EncodeChars.charAt(63 & n)
    }
    return a
}

function base64encode2(e) {
    var a, c, r, o, t, n;
    for (r = e.length, c = 0, a = ""; c < r;) {
        if (o = 255 & e.charCodeAt(c++), c == r) {
            a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4), a += "==";
            break
        }
        if (t = e.charCodeAt(c++), c == r) {
            a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4 | (240 & t) >> 4), a += base64EncodeChars.charAt((15 & t) << 2), a += "=";
            break
        }
        n = e.charCodeAt(c++), a += base64EncodeChars.charAt(o >> 2), a += base64EncodeChars.charAt((3 & o) << 4 | (240 & t) >> 4), a += base64EncodeChars.charAt((15 & t) << 2 | (192 & n) >> 6), a += base64EncodeChars.charAt(63 & n)
    }
    return a
}

function base64decode(e) {
    var a, c, r, o, t, n, i;
    for (n = e.length, t = 0, i = ""; t < n;) {
        do
        a = base64DecodeChars[255 & e.charCodeAt(t++)];
        while (t < n && a == -1);
        if (a == -1) break;
        do
        c = base64DecodeChars[255 & e.charCodeAt(t++)];
        while (t < n && c == -1);
        if (c == -1) break;
        i += String.fromCharCode(a << 2 | (48 & c) >> 4);
        do {
            if (r = 255 & e.charCodeAt(t++), 61 == r) return i;
            r = base64DecodeChars[r]
        } while (t < n && r == -1);
        if (r == -1) break;
        i += String.fromCharCode((15 & c) << 4 | (60 & r) >> 2);
        do {
            if (o = 255 & e.charCodeAt(t++), 61 == o) return i;
            o = base64DecodeChars[o]
        } while (t < n && o == -1);
        if (o == -1) break;
        i += String.fromCharCode((3 & r) << 6 | o)
    }
    return i
}

function utf16to8(e) {
    var a, c, r, o;
    for (a = "", r = e.length, c = 0; c < r; c++)
    o = e.charCodeAt(c), o >= 1 && o <= 127 ? a += e.charAt(c) : o > 2047 ? (a += String.fromCharCode(224 | o >> 12 & 15), a += String.fromCharCode(128 | o >> 6 & 63), a += String.fromCharCode(128 | o >> 0 & 63)) : (a += String.fromCharCode(192 | o >> 6 & 31), a += String.fromCharCode(128 | o >> 0 & 63));
    return a
}

function utf8to16(e) {
    var a, c, r, o, t, n;
    for (a = "", r = e.length, c = 0; c < r;)
    switch (o = e.charCodeAt(c++), o >> 4) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
            a += e.charAt(c - 1);
            break;
        case 12:
        case 13:
            t = e.charCodeAt(c++), a += String.fromCharCode((31 & o) << 6 | 63 & t);
            break;
        case 14:
            t = e.charCodeAt(c++), n = e.charCodeAt(c++), a += String.fromCharCode((15 & o) << 12 | (63 & t) << 6 | (63 & n) << 0)
    }
    return a
}

function isHQMInstalled() {
    var e = null;
    try {
        return e = new ActiveXObject("HqtChat.HqtChatDlg"), null != e && (e = null, !0)
    } catch (a) {
        return !1
    }
}

function isHQM2011InstalledOld() {
    var e = null;
    try {
        return e = new ActiveXObject("hqRun.hqtmRun"), null != e && (e = null, !0)
    } catch (a) {
        return !1
    }
}

function isHQM2011Installed() {
    var e = null;
    try {
        return e = new ActiveXObject("HqmTalk.HqmPlugin"), null != e && (e = null, !0)
    } catch (a) {
        return !1
    }
}

function HQMCheck() {
    return !activex_hqm || !! (isHQMInstalled() || isHQM2011Installed() || isHQM2011InstalledOld())
}

function HqmWeb(e) {
    var a = document.getElementsByTagName("head")[0],
        c = null,
        r = function() {
            e.success && e.success(), c.loaded = !0, void 0 !== e.cache && a.removeChild(c)
        };
    void 0 === e.cache && Q("head script").each(function() {
        if (this.src == (e.url.indexOf("http://") > -1 ? e.url : "http://" + location.host + e.url)) return c = this, !1
    }), c || (c = document.createElement("script"), c.type = "text/javascript", c.src = e.url + (e.cache === !1 ? (e.url.indexOf("?") > -1 ? "&_=" : "?_=") + (new Date).getTime() : ""), c.charset = e.charset || "utf-8"), c.loaded ? r() : isFF ? c.addEventListener("load", r, !1) : c.attachEvent("onreadystatechange", function() {
        /loaded|complete/.test(c.readyState) && r()
    }), a.appendChild(c)
}

function HqmService(e, a, c, r, o) {
    if (HqmClientEntUrl = "hqew://?uid=" + e + "&uname=" + a + "&entuid=" + r + "&roid=" + o, HqmClientDefUrl = "hqew://?uid=" + e + "&uname=" + a, HQMCheck()) try {
        HqmWeb({
            url: "http://hqmim.hqew.com/ajax/services.aspx?uid=" + e + "&ug=" + a + "&type=" + c + "&entuid=" + r + "&roid=" + o,
            cache: !0,
            success: function() {
                if (void 0 != HqmServiceObj) {
                    var e = 9;
                    void 0 != HqmServiceObj.ResultCode && (e = HqmServiceObj.ResultCode.toString()), "0" == e && ("0" == HqmServiceObj.Data.EntID ? window.location.href = HqmClientDefUrl : void 0 != HqmServiceObj.Data.ServiceID && (window.location.href = "hqew://?uid=" + HqmServiceObj.Data.ServiceID + "&uname=" + HqmServiceObj.Data.Guid + "&entuid=" + HqmServiceObj.Data.EntID + "&roid=" + HqmServiceObj.Data.RoID))
                } else window.location.href = HqmClientDefUrl;
                HqmServiceObj = null
            }
        })
    } catch (t) {} else window.open(hqDomain.IBS + "/Web/Hqen/Imrfq/Imrfqidic.aspx?uguid=" + a + "&pguid=", target = "_blank")
}

function gotoEmail(e) {
    var a = $.trim(e.split("@")[1]);
    return "" != a ? (a = a.toLowerCase(), "163.com" == a ? "mail.163.com" : "vip.163.com" == a ? "vip.163.com" : "126.com" == a ? "mail.126.com" : "qq.com" == a || "vip.qq.com" == a || "foxmail.com" == a ? "mail.qq.com" : "gmail.com" == a ? "mail.google.com" : "sohu.com" == a ? "mail.sohu.com" : "tom.com" == a ? "mail.tom.com" : "vip.sina.com" == a ? "vip.sina.com" : "sina.com.cn" == a || "sina.com" == a ? "mail.sina.com.cn" : "tom.com" == a ? "mail.tom.com" : "yahoo.com.cn" == a || "yahoo.cn" == a ? "mail.cn.yahoo.com" : "tom.com" == a ? "mail.tom.com" : "yeah.net" == a ? "www.yeah.net" : "21cn.com" == a ? "mail.21cn.com" : "hotmail.com" == a ? "www.hotmail.com" : "sogou.com" == a ? "mail.sogou.com" : "188.com" == a ? "www.188.com" : "139.com" == a ? "mail.10086.cn" : "189.cn" == a ? "webmail15.189.cn/webmail" : "wo.com.cn" == a ? "mail.wo.com.cn/smsmail" : "139.com" == a ? "mail.10086.cn" : "") : ""
}

function weixincode_show() {
    $("#weixincode").removeClass("hid")
}

function weixincode_close() {
    $("#weixincode").addClass("hid")
}
var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
    base64DecodeChars = new Array((-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), 62, (-1), (-1), (-1), 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, (-1), (-1), (-1), (-1), (-1), (-1), (-1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, (-1), (-1), (-1), (-1), (-1), (-1), 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, (-1), (-1), (-1), (-1), (-1)),
    activex_hqm = navigator.userAgent.indexOf("Win") != -1 && navigator.userAgent.indexOf("MSIE") != -1 && parseInt(navigator.appVersion) >= 4,
    isFF = !! window.addEventListener,
    HqmServiceObj = null,
    HqmClientEntUrl = "",
    HqmClientDefUrl = "";

function getpwd(password) {
    return base64encode2(password)
}



console.log(getpwd("123456"));
/*
* https://passport.hqew.com/login
* */