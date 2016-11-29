/**
 * Created by pepe on 11/18/16.
 */
$(document).ready(function() {
		// this is ugly, threw it together to make it work.
		var state = true;

		$('.redo').click(function() {
				reanimate();
		});

		$('.error').hide().removeClass('animate');

		var reanimate = function() {
				if (state === false) {
						state = true;
						$('.success').show().addClass('animate');
						$('.error').hide().removeClass('animate');
				} else {
						state = false;
						$('.success').hide().removeClass('animate');
						$('.error').show().addClass('animate');
				}
		};

});