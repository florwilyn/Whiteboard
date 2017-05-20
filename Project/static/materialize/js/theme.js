$( document ).ready(function(){
	$(".dropdown-button").dropdown();
    $('.collapsible').collapsible();
	
});

$( document ).ready(function(){
	$(".button-collapse").sideNav();
});

$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
  });

$(document).ready(function(){
    $('#note').click(function() {
    	$(this).toggleClass('clicked');
    	$("#modal-title").fadeOut(function() {
		  $(this).text("Add a note").fadeIn();
		});
    	$('#note').trigger('click');
    }); 
});

$(document).ready(function(){
   document.getElementById('page-load').style.display = 'none';
   // $('.dropify').dropify();
});

$(document).ready(function(){
   $('.dropify').dropify();
});
