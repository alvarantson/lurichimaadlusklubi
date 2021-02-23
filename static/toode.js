if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
	$(".main").addClass("phone");
} else {
	$(".main").removeClass("phone");
};