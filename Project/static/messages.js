var scrolling = false;
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


function getNotes(){
    if (!scrolling) {
        $.get('/notes/'+ $('#group_id').val(), function(notes){
            $('#notes-list').html(notes);
            var chatlist = document.getElementById('notes-list');
            chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
}

function getMembers(){
    if (!scrolling) {
        $.get('/members/'+ $('#group_id').val(), function(members){
            $('#members-list').html(members);
            // var chatlist = document.getElementById('members-list');
            // chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
}

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