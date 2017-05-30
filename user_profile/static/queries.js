// $('#register').on('submit', function(event){
//     event.preventDefault();

//     // if ($('#password').val() != $('#password')){
//     //     document.getElementById('mismatch').style.display = 'block';
//     //     return false;
//     // }
//     // document.getElementById('loading').style.display = 'block';
//     $.ajax({
//         url : '/signup/',
//         type : 'POST',
//         data : { fname : $('#fname').val(),
//                 lname: $('#lname').val(),
//                 username: $('#username').val(),
//                 password: $('#password').val()   
//                 },

//         success : function(json){
//             // $('#groups').prepend('<li><a href="/group/' + json.id + '">'+ json.newgroup +'</a></li>');
//             // swal(json.newgroup, "has been created", "success")
//             alert(json.error);
//         }
//     });
// });

// // using jQuery
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');

// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });
