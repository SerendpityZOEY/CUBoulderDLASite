/**
 * Created by yue on 10/7/16.
 */

// var i = 0;
// var trueArr = Array(6).fill(false)
// var pushed = false
// $(document).ready(function () {
//     $('form').validator().on('submit', function (e) {

//         if (e.isDefaultPrevented()) {
//             // handle the invalid form...
//             console.log('invalid')
//             console.log(e)
//             trueArr[i++] = false
//             console.log(trueArr)
//         } else {
//             console.log('valid')
//             e.preventDefault()
//             trueArr[i++] = true
//             console.log(trueArr)
//             // everything looks good!
//         }
//         if (!trueArr.includes(false) && !pushed) {
//             $.ajax({
//                 url: '/fsubmit',
//                 data: $('form').serialize(),
//                 type: 'POST',
//                 success: function (response) {
//                     console.log(response);
//                     // alert("succesfully added!");
//                     window.location.href = response;
//                 },
//                 error: function (error) {
//                     // console.log($('form').serialize());
//                     console.log(error);
//                     // alert("information miss!");
//                     window.location.href = "error";
//                 }
//             });
//             pushed = true
//         }
//     });
// })
// $(function () {
//     $('#facSubmit').click(function () {
//         i = 0;
//         $('form').submit();
//     });
// });








// /**
//  * Created by yue on 10/7/16.
//  */


bootstrap_alert = function (message, alert, timeout) {
    $('<div id="floating_alert" class="alert alert-' + alert + ' fade in" role="alert">' +
        '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>' + message + '&nbsp;&nbsp;</div>').appendTo('body');
                



    setTimeout(function () {
        $(".alert").alert('close');
    }, timeout);

}


var i = 0;
var trueArr = Array(8).fill(false)
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
        if (trueArr.includes(false)) {
            setTimeout(function(){
                bootstrap_alert('You have some fields not filled correctly, please check the required fields!</strong>', 'danger', 10000);
            }, 1000)
        }
        if (!trueArr.includes(false) && !pushed) {
            $(".alert").alert('close');
            $.ajax({
                url: '/fsubmit',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    // console.log(response);
                    // alert("succesfully added!");
                    window.location.href = response;
                },
                error: function (error) {
                    // console.log($('form').serialize());
                    // console.log(error);
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
        $("html, body").animate({ scrollTop: 0 },"slow");
        i = 0;
        $('form').submit();

    });
});


