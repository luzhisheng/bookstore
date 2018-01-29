$(function () {
    $('.oper_btn').click(function () {
        //獲取订单id和订单的状态
        order_id = $(this).attr('order_id')
        order_status = $(this).attr('order_status')
        csrf = $('input[name="csrfmiddlewaretoken"]').val()
        params = {
            'order_id':order_id,
            'csrfmiddlewaretoken':csrf
        }
        if (order_status == 1){
            $.post('/order/pay/',params,function (data) {
                if (date.res == 3){
                    //把用户引导支付页面
                    window.open(data.pay_url)
                    //查询用户的结果
                    $.post('/order/check_pay',params,function (data) {
                        if (data.res == 3){
                            alert('支付成功')
                            //重新刷新页面
                            location.reload()
                        }
                        else {
                            alert(data.errmsg)
                        }
                    })
                }else {
                    alert(data.errmsg)
                }
            })
        }
    })
})