$(function () {
    $('#order_btn').click(function() {
            // 获取收货地址的id, 支付方式，用户购买的商品id
            addr_id = $('input[name="addr_id"]').val()
            pay_method = $('input[name="pay_style"]:checked').val()
            books_ids = $(this).attr('books_ids')
            csrf = $('input[name="csrfmiddlewaretoken"]').val()
            // alert(addr_id+':'+pay_method+':'+books_ids)
            // 发起post请求， 访问/order/commit/
            params = {
                'addr_id': addr_id,
                'pay_method': pay_method,
                'books_ids': books_ids,
                'csrfmiddlewaretoken': csrf
            }
            $.post('/order/commit/', params, function (data) {
                // 根据json进行处理
                if (data.res == 6){
                    localStorage.setItem('order_finish',2);
                    $('.popup_con').fadeIn('fast', function() {
                        setTimeout(function(){
                            $('.popup_con').fadeOut('fast',function(){
                                window.location.href = '/user/order/';
                            });
                        },3000)

                    });
                }
                else {
                    alert(data.errmsg)
                }
            })

        });
})