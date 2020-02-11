/**
 * 默认的请求失败处理函数
 * @param data
 */
function errorHandler(data) {

    layer.msg(data.msg, {icon: 5, time: 3000});

}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * 向服务器发生post请求
 * @param data
 * @param url
 * @param success
 * @param error
 * @param dataType
 */
function post(data, url, success, error = errorHandler, dataType = 'json') {

    let csrftoken = $.cookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        dataType: dataType,
        success: success,
        error: error,
    });

}

function get(data, url, success, error=errorHandler, dataType='json') {

    $.ajax({
        type: "GET",
        url: url,
        data: data,
        dataType: dataType,
        success: success,
        error: error,
    });

}

/***
 * 验证电话号码格式是否正确
 * @param phone
 * @returns {boolean}
 */
function checkPhone(phone){
    let reg = /^[1][345789][0-9]{9}$/;
    if(!reg.test(phone)){
        return false;
    }
    return true;
}

function checkEmail(email) {
    let reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
    return reg.test(email);

}

function checkName(name) {
    return name.length <= 32;
}

function checkRemark(remark) {
    return remark.length <= 128;
}
