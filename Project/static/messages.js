function getMessages(){
    if (!scrolling) {
        $.get('/chat/'+ $('#group_id').val(), function(chat){
            $('#msg-list').html(chat);
            var chatlist = document.getElementById('msg-list');
            chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
}

var scrolling = false;
$(function(){
    $('#msg-list').on('scroll', function(){
        scrolling = true;
    });
    refreshTimer = setInterval(getMessages, 500);
});

$(document).ready(function() {
     $('#send').attr('disabled','disabled');
     $('#message').keyup(function() {
        if($(this).val() != '') {
           $('#send').removeAttr('disabled');
        }
        else {
        $('#send').attr('disabled','disabled');
        }
     });
 });