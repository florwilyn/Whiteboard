// $('#chat-form').on('submit', function(event){
//     event.preventDefault();

//     $.ajax({
//         url : '/post/',
//         type : 'POST',
//         data : { msgbox : $('#message').val(),
//                  recipient: $('#recipient_id').val()   
//                 },

//         success : function(json){
//             $('#message').val('');
//                 $('#msg-list').append('<li class="other"><a class="user" href="#"><img alt="" src="'+ json.photo +'" /></a><div class="date">'+ json.date_sent +'     <b>'+ json.sender +'</b></div><div class="message" id="you-color"><p>'+ json.msg +'</p></div></li>')

//             var chatlist = document.getElementById('msg-list');
//             chatlist.scrollTop = chatlist.scrollHeight;
//         }
//     });
// });

// $('#add_member').on('submit', function(event){
//     event.preventDefault();
//     $("#memberbutton").html('');
//     // document.getElementByClass('no-text').style.display = 'block';
//     $(".no-text").attr('class', 'fa fa-spinner fa-spin');

//     $.ajax({
//         url : '/add_member/',
//         type : 'POST',
//         data : { user : $('#member').val(),
//                  group: $('#group_id').val()   
//                 },

//         success : function(json){
//             // $('#add_membermodal').modal('hide');
//             $('#members-list').append('<li><img class="member-img" src="'+json.photo+'"><span class="users-list-name">'+json.first_name+'</span></li>');
//             swal(json.first_name, "has been added.", "success")
//             $("#memberbutton").html('Add');
//         }
//     });
// });

// $('#add_note').on('submit', function(event){
//     event.preventDefault();
//     document.getElementById('loading').style.display = 'block';
//     $.ajax({
//         url : '/add_note/',
//         type : 'POST',
//         data : { note : $('#note').val(),
//                  group: $('#group_id').val()   
//                 },

//         success : function(json){
//             // $('#add_membermodal').modal('hide');
//             $('#notes-list').append('<li><div class="collapsible-header">'+json.note+'<span class="new badge amber"></span></div><div class="collapsible-body"><span>'+json.note+'</span></div></li>');
//             var chatlist = document.getElementById('notes-list');
//             chatlist.scrollTop = chatlist.scrollHeight;

//             swal("Noted", "", "success")
//         //     $("#modal-title").fadeOut(function() {
//         //   $(this).text("Noted").fadeIn();
//         // });
//         //     $('#note').val("");
//         //     document.getElementById('loading').style.display = 'none';
//         }
//     });
// });

$('#add_group').on('submit', function(event){
    event.preventDefault();
    // document.getElementById('loading').style.display = 'block';
    $.ajax({
        url : '/add_group/',
        type : 'POST',
        data : { groupname : $('#groupname').val(),
                 user: $('#user').val()   
                },

        success : function(json){
            $('#groups').prepend('<li><a href="/group/' + json.id + '">'+ json.newgroup +'</a></li>');
            swal(json.newgroup, "has been created", "success")
        }
    });
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


var supportsWebSockets = ('WebSocket' in window || 'MozWebSocket' in window) && WebSocket;
            if(!supportsWebSockets){
                $(".very-old-browser-notification").show();
                $(".non-error").hide();
            }else{
                $(".very-old-browser-notification").hide();
                $(".non-error").show();
            }
            var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
            // Calls the websocket connect channel
            var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat/stream/test-chat");

// Code that is called when the socket is succesfully opened
chatsock.onopen = function(message) {
                
                // $('.error-notification').hide();
                // $('.non-error').show();
                // $('#messages-container').html('<div  class="empty-div"></div>');
                message = {}
                message.command= 'start'
                console.log("HERE!!!!");
                chatsock.send(JSON.stringify(message)); // START TALKING!
            }
            chatsock.onmessage = function(message){
                // processAndDisplayChatMessage(message);
            };

            chatsock.onclose = function(message){
                // console.log("connection lost ... ");
            }
            
            chatsock.onerror = function(message){
                console.log("Error reconnecting ... ");
                // $('.error-notification').html("Unable to connect to the yomamabot server. Please try again in a few minutes (by refreshing the page). If the problem persists, please contact yomamabot (contact@yomamabot.com)).")
                // $('.error-notification').show();
                // $('.non-error').hide();
                // $("#body-container").scrollTop( $('#body-container')[0].scrollHeight );   
            }