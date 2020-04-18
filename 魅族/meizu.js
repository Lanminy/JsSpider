var cryPP = {
    excutePP: function(r, e) {
        for (var n = "", t = 0; t < r.length; t++) {
            var o = e ^ r.charCodeAt(t);
            n += String.fromCharCode(o)
        }
        return encodeURIComponent(n)
    },
    generateMix: function(r) {
        return Math.ceil(1e3 * Math.random())
    }
};

function getpwd(password) {
    var kk = cryPP.generateMix();
    var pwd = cryPP.excutePP(password, kk);
    return pwd;
}



console.log(getpwd("123456"));

/*
* https://login.flyme.cn/
* getpwd("123456")
* */