/**
 * Created by yue on 10/7/16.
 */
$(function() {
    $('#form1').click(function() {
/*
        $('#checkboxForm').validate({
            rules: {
                'race': {
                    required: true,
                    minlength: 1,
                    maxlength: 2
                }
            },
            messages: {
                'race': {
                  required: "Please check at least 1 option.",
                  minlength: "Please check at least {0} option."
                }
            }
        });
*/
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

$(function() {
    $('#form2').click(function() {

        $.ajax({
            url: '/fsubmit',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                alert("succesfully added!");
                window.location = "/";
            },
            error: function(error) {
                console.log($('form').serialize());
                console.log(error);
                alert("information miss!");
            }
        });
    });
});
