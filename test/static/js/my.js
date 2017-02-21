
function disableCheckBoxes(bestAnswer) {
    var a = bestAnswer
    if (a != 0) {
       $(':checkbox').not('#best-answer'+a).attr('disabled', true);
       $('#ans'+a).css("border", "4px solid green");
       $('#ans-block'+a).css("margin-left", "-2px");
       $('#ans'+a).css({"margin-top":"-2px", "margin-bottom":"13px"});
    }
}

$(document).ready(function() {
    $('#btn-sbmt').click(function(e) {
          // if ($('#reg-form').bootstrapValidator('validate').has('.has-error').length) {
          //     return false;
          // }
          e.preventDefault();
          var formData = new FormData($('#reg-form')[0]);
          $.ajax({
              url: '/signup/',
              type: 'POST',
              data: formData,
              async: true,
              success: function (data) {
                  if(data.hasOwnProperty('error')) {
                      if( $('#field-error').length ) {
                          $('#field-error').text(data.error);
                      } else {
                          $("#reg-form").append('<br><div class="alert alert-danger" \
                          role ="alert" id="field-error">'+data.error+'</div>');
                      }
                  } else if (data.hasOwnProperty('result')) {
                      $("#reg-form").replaceWith( '<div class="alert alert-success" role="alert"> \
                      '+data.result+'</div><p><a href="/login/" class="btn btn-primary" role="button">'+data.button+'</a></p>');
                  }
              },
              error: function (data) {
                console.log(data)
              },
              cache: false,
              contentType: false,
              processData: false
          });
     });
});

$(document).ready(function() {
    $('#btn-log').click(function(e) {
          e.preventDefault();
          // $('#log-form').bootstrapValidator('validate')
          var formData = new FormData($('#log-form')[0]);
          $.ajax({
              url: '/login/',
              type: 'POST',
              data: formData,
              async: true,
              success: function (data) {
                  if(data.hasOwnProperty('error')) {
                      if( $('#field-error').length ) {
                          $('#field-error').text(data.error);
                      } else {
                          $("#log-form").append('<br><div class="alert alert-danger" \
                          role ="alert" id="field-error">'+data.error+'</div>');
                      }
                  } else if (data.hasOwnProperty('result')) {
                        $("#log-form").replaceWith( '<div class="alert alert-success" role="alert"> \
                        '+data.result+'</div>');
                        $(".not-reg").replaceWith( '<li><img class="navbar-right img-rounded navbar-img" width="120" height="60" src="/uploads/'+data.avatar+'"></li>\
                        <a href="/profile" class="navbar-link navbar-user roboto-font-user">Профиль '+data.user+'</a><br>\
                        <a href="/logout/" class="navbar-link navbar-logout roboto-font-user">\
                        <span class="glyphicon glyphicon-log-out"></span> Logout </a>');
                  }
              },
              error: function (data) {
                console.log(data)
              },
              cache: false,
              contentType: false,
              processData: false
          });
     });
     return false;
});
