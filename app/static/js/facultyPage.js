/**
 * Created by yue on 10/7/16.
 */

var i = 0;
var trueArr = Array(6).fill(false)
var pushed = false
$(document).ready(function () {
    $('form').validator().on('submit', function (e) {

        if (e.isDefaultPrevented()) {
            // handle the invalid form...
            console.log('invalid')
            console.log(e)
            trueArr[i++] = false
            console.log(trueArr)
        } else {
            console.log('valid')
            e.preventDefault()
            trueArr[i++] = true
            console.log(trueArr)
            // everything looks good!
        }
        if (!trueArr.includes(false) && !pushed) {
            $.ajax({
                url: '/fsubmit',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    console.log(response);
                    // alert("succesfully added!");
                    window.location.href = response;
                },
                error: function (error) {
                    // console.log($('form').serialize());
                    console.log(error);
                    // alert("information miss!");
                    window.location.href = "error";
                }
            });
            pushed = true
        }
    });
})
$(function () {
    $('#facSubmit').click(function () {
        i = 0;
        $('form').submit();
    });
});
