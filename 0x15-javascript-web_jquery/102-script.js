$("#btn_translate").bind("click", function(){
	$.ajax({
		type: 'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $("#language_code").val(),
		success: function(data) {
			$("#hello").text(data.hello);
		}
	});
});
