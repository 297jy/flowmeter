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
    });

}