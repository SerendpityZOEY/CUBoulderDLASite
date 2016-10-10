/**
 * Created by yue on 10/7/16.
 */
$(function() {
    $('#form1').click(function() {

        $.ajax({
            url: '/submit',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                alert("succesfully added!");
            },
            error: function(error) {
                console.log($('form').serialize());
                console.log(error);
                alert("information miss!");
            }
        });
    });
});
