$(function () {
    var $add_x = $('#add_cart').offset().top;
    var $add_y = $('#add_cart').offset().left;
    var $to_x = $('#show_count').offset().top;
    var $to_y = $('#show_count').offset().left;

    $(".add_jump").css({'left': $add_y + 80, 'top': $add_x + 10, 'display': 'block'})
    $('#add_cart').click(function () {
        $(".add_jump").stop().animate({
                'left': $to_y + 7,
                'top': $to_x + 7
            },
            "fast", function () {
                $(".add_jump").fadeOut('fast', function () {
                    $('#show_count').html(2);
                });
            });
    })
})