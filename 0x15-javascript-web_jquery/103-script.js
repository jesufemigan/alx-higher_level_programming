function fetchData() {
	$.ajax({
		type: 'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $("#language_code").val(),
		success: function(data) {
			$("#hello").text(data.hello);
		}
	});
}

$("#btn_translate").bind("click", fetchData);
$("#language_code").on("keypress", function(event){
	if (event.which == 13) {
		fetchData();
	}
});
