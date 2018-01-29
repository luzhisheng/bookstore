$(function () {
    var $add_x = $('#add_cart').offset().top;
    var $add_y = $('#add_cart').offset().left;
    var $to_x = $('#show_count').offset().top;
    var $to_y = $('#show_count').offset().left;

    $('#add_cart').click(function(){
        // 获取商品的id和商品数量
        books_id = $(this).attr('books_id')//获取当前节点 books_id元素的值
        books_count = $('.num_show').val()
        csrf = $('input[name="csrfmiddlewaretoken"]').val()
        // 发起请求，访问/cart/add/, 进行购物车数据的添加
        params = {
            'books_id': books_id,
            'books_count': books_count,
            'csrfmiddlewaretoken': csrf
        }
        $.post('/cart/add/', params, function (data) {
            if (data.res == 5){
                // 添加成功
                $(".add_jump").css({'left':$add_y+80,'top':$add_x+10,'display':'block'})//80，10是校正起点和终点的位置
                $(".add_jump").stop().animate({//动画效果
                    'left': $to_y+7,
                    'top': $to_x+7},
                    "fast",
                    function() {//
                        $(".add_jump").fadeOut('fast',function(){//fadeOut淡如淡出
                            // 获取原有 show_count 的值
                            count = $('#show_count').html()
                            count = parseInt(count) + parseInt(books_count)
                            $('#show_count').html(count);
                        });
                });
            }
            else {
                // 添加失败
                alert(data.errmsg)
            }
        })
    })

        update_total_price()
    // 计算总价
    function update_total_price() {
        // 获取商品的价格和数量
        books_price = $('.show_pirze').children('em').text()
        books_count = $('.num_show').val()
        // 计算商品的总价
        books_price = parseFloat(books_price)
        books_count = parseInt(books_count)
        total_price = books_price * books_count
        // 设置商品总价
        $('.total').children('em').text(total_price.toFixed(2) + '元')
    }

    // 商品增加
    $('.add').click(function () {
        // 获取商品的数量
        books_count = $('.num_show').val()
        // 加1
        books_count = parseInt(books_count) + 1
        // 重新设置值
        $('.num_show').val(books_count)
        // 计算总价
        update_total_price()
    })

    // 商品减少
    $('.minus').click(function () {
        // 获取商品的数量
        books_count = $('.num_show').val()
        // 加1
        books_count = parseInt(books_count) - 1
        if (books_count == 0){
            books_count = 1
        }
        // 重新设置值
        $('.num_show').val(books_count)
        // 计算总价
        update_total_price()
    })

    // 手动输入
    $('.num_show').blur(function () {
        // 获取商品的数量
        books_count = $(this).val()
        // 数据校验
        if (isNaN(books_count) || books_count.trim().length == 0 || parseInt(books_count) <= 0 ){
            books_count = 1
        }
        // 重新设置值
        $('.num_show').val(parseInt(books_count))
        // 计算总价
        update_total_price()
    })

})