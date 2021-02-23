if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
	$(".navbar-desktop").toggleClass("hidden");
	$(".footer-desktop").toggleClass("hidden");
	$('.navbar-phone__closer').toggleClass('hidden');
} else {
	$(".navbar-phone").toggleClass("hidden");
	$(".footer-phone").toggleClass("hidden");
	$('.navbar-phone__closer').toggleClass('hidden');
	$('.navbar-phone__burger').toggleClass('hidden');
	$('body').addClass('phone-body');
	$('sisu').addClass('phone-body');
	$('main').addClass('phone-body');
};


$('.navbar-phone__burger').click(function(){
	// phone nav open
	$('.navbar-phone__closer').toggleClass('hidden');
	$('.navbar-phone__burger').toggleClass('hidden');
	$('.navbar-phone__content').slideDown(50);
});
$('.navbar-phone__closer').click(function(){
	// phone nav close
	$('.navbar-phone__burger').toggleClass('hidden');
	$('.navbar-phone__closer').toggleClass('hidden');
	$('.navbar-phone__content').slideUp(50);
});


$( document ).ready(function() {
    $('.loader').fadeOut(1000);
});