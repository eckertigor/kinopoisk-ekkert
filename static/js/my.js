
        $.ajaxSetup({
             beforeSend: function(xhr, settings) {
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
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         }
    });

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
                      '+data.result+'</div><p><a href="/login/" class="btn btn-primary btn-back" role="button">'+data.button+'</a></p>');
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
                        $(".not-reg").replaceWith( '<li><img class="navbar-right img-rounded navbar-img avatar" src="/uploads/'+data.avatar+'"></li>\
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

$(document).on("submit","#film-form", function (e) {
          e.preventDefault();
          var formData = new FormData($('#film-form')[0]);
          $.ajax({
              url: '/control/add/',
              type: 'POST',
              data: formData,
              async: true,
              success: function (data) {
                  if(data.hasOwnProperty('error')) {
                      if( $('#field-error').length ) {
                          $('#field-error').text(data.error);
                      } else {
                          $("#film-form").append('<br><div class="alert alert-danger" \
                          role ="alert" id="field-error">'+data.error+'</div>');
                      }
                  } else if (data.hasOwnProperty('result')) {
                      $("#film-form").replaceWith( '<div class="alert alert-success" role="alert"> \
                      '+data.result+'</div><p><a href="/control/" class="btn btn-primary btn-back" role="button">'+data.button+'</a></p>');
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

$(document).on("submit","#film-edit-form", function (e) {
          e.preventDefault();
          var formData = new FormData($('#film-edit-form')[0]);
          var film_id = $('#film_id').val();
          $.ajax({
              url: '/control/edit/'+film_id+'',
              type: 'POST',
              data: formData,
              async: true,
              success: function (data) {
                  if(data.hasOwnProperty('error')) {
                      if( $('#field-error').length ) {
                          $('#field-error').text(data.error);
                      } else {
                          $("#film-edit-form").append('<br><div class="alert alert-danger" \
                          role ="alert" id="field-error">'+data.error+'</div>');
                      }
                  } else if (data.hasOwnProperty('result')) {
                      $("#film-edit-form").replaceWith( '<div class="alert alert-success" role="alert"> \
                      '+data.result+'</div><p><a href="/control/" class="btn btn-primary btn-back" role="button">'+data.button+'</a></p>');
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

$(document).on("click", "#film-delete", function(e){
           e.preventDefault();
           var film_id = $('#film_id').val();
           var film_title = $('#hide-title').val();
           $.ajax({
               url: '/control/delete/'+film_id+'',
               type: 'POST',
               data: {'film_id' : $('#film_id').val()},
               async: false,
               success: function (data) {
                   if(data.hasOwnProperty('result')) {
                     $("#title").replaceWith('<h2><b>(Удален)'+film_title+'</b></h2>');
                     $("#film-delete").replaceWith('<a href="/control/restore/" \
                                class="btn btn-success admin-edit" role="button" \
                                id="film-restore">Восстановить</a>');
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


 $(document).on("click", "#film-restore", function(e){
           e.preventDefault();
           var film_id = $('#film_id').val();
           var film_title = $('#hide-title').val();
           $.ajax({
               url: '/control/restore/'+film_id+'',
               type: 'POST',
               data: {'film_id' : $('#film_id').val()},
               async: false,
               success: function (data) {
                   if(data.hasOwnProperty('result')) {
                     $("#title").replaceWith('<h2><b>'+film_title+'</b></h2>');
                     $("#film-restore").replaceWith('<a href="/control/delete/" \
                                class="btn btn-danger admin-edit" role="button" \
                                id="film-delete">Удалить</a>');
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

$(function() {
  $("#rating_star").codexworld_rating_widget({
      starLength: '10',
      initialValue: $('#my_rating').val(),
      callbackFunctionName: 'processRating',
      imageDirectory: '../uploads',
      inputAttr: 'postID'
  });
});

function processRating(val, attrVal) {
    var film_id = $('#film_id').val();
    $.ajax({
        type: 'POST',
        url: '/vote/',
        data: {'film_id' : film_id, 'value': val},
        success : function(data) {
            if (data.status == 'ok') {
                $('#avgrat').text(data.rating);
            }else{
                alert('Some problem occured, please try again.');
            }
        }
    });
}

$(document).on("click", "#review-send", function(e){
          e.preventDefault();
          // $('#log-form').bootstrapValidator('validate')
          var formData = new FormData($('#review-form')[0]);
          var text = $('#id_text').val();
          var user = $('#user_name').val();
          var $avatar = $('.navbar-right.img-rounded.navbar-img.avatar').clone();
          $avatar.attr('class','navbar-left img-rounded question-author-avatar avatar-small');
          formData.append('film_id', $('#film_id_form').val())
          $.ajax({
              url: '/review/',
              type: 'POST',
              data: formData,
              async: true,
              success: function (data) {
                  if(data.status == 'ok') {
                    $("#id_text").val('');
                    $("#reviews").append('<div class="row question-answers"> \
                        <div class="col-md-2 col-sm-2">                      \
                            <div class="row">               \
                              <div id="replace"> </div> \
                            </div>  \
                            <h4>'+user+'</h4><br>   \
                        </div>    \
                        <div id="ans-text{{ r.id }}"    \
                        class="col-md-10 col-sm-10 review-text">  \
                            <div class="review-block">  \
                              <P>'+text+'</P>  \
                            </div>   \
                        </div>   \
                    </div>');
                    $("#replace").replaceWith($avatar);
                    $(window).scrollTop($(document).height());



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

$(document).on("click", ".btn.btn-danger.hide-review", function(e){
           e.preventDefault();
           var href = $(this).attr('href');
           $.ajax({
               url: href,
               type: 'POST',
               data: { },
               async: false,
               success: function (data) {
                   if(data.hasOwnProperty('result')) {
                       $('#hide_review_'+data.review+'').replaceWith('<a href="/control/hide/'+data.review+'/0/" \
                                  class="btn btn-success hide-review" role="button" \
                                  id="show_review_'+data.review+'">Показать</a>');
                       $('#'+data.review+'').attr("class", "row question-answers hide-block");
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

$(document).on("click", ".btn.btn-success.hide-review", function(e){
           e.preventDefault();
           var href = $(this).attr('href');
           $.ajax({
               url: href,
               type: 'POST',
               data: { },
               async: false,
               success: function (data) {
                   if(data.hasOwnProperty('result')) {
                       $('#show_review_'+data.review+'').replaceWith('<a href="/control/hide/'+data.review+'/1/" \
                                  class="btn btn-danger hide-review" role="button" \
                                  id="hide_review_'+data.review+'">Скрыть</a>');
                       $('#'+data.review+'').attr("class", "row question-answers");
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

  $(document).on("click", "#film-delete-control", function(e){
             e.preventDefault();
             var href = $(this).attr('href');
             $.ajax({
                 url: href,
                 type: 'POST',
                 data: { },
                 async: false,
                 success: function (data) {
                     if(data.hasOwnProperty('result')) {
                       $('#'+data.film_id+'').remove();
                       $('.removed').prepend('<ul class="list-group list-all-films" \
                           id="'+data.film_id+'"> \
                 			  <li class="list-group-item">  \
                 					<a href="/film/'+data.film_id+'"><b>'+data.film_title+'<b></a>  \
                 					<a href="/control/edit/'+data.film_id+'"  \
                            class="btn btn-warning admin-edit control-item"  \
                 						        role="button">Редактировать</a>  \
                 					<a href="/control/restore/'+data.film_id+'"    \
                             class="btn btn-success admin-edit control-item" \
                 										role="button" id="film-restore-control">Восстановить</a>  \
                 			  </li> </ul>');
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

  $(document).on("click", "#film-restore-control", function(e){
             e.preventDefault();
             var href = $(this).attr('href');
             $.ajax({
                 url: href,
                 type: 'POST',
                 data: { },
                 async: false,
                 success: function (data) {
                     if(data.hasOwnProperty('result')) {
                       $('#'+data.film_id+'').remove();
                       $('.active').prepend('<ul class="list-group list-all-films" \
                           id="'+data.film_id+'"> \
                 			  <li class="list-group-item">  \
                 					<a href="/film/'+data.film_id+'"><b>'+data.film_title+'<b></a>  \
                 					<a href="/control/edit/'+data.film_id+'"  \
                            class="btn btn-warning admin-edit control-item"  \
                 						        role="button">Редактировать</a>  \
                 					<a href="/control/delete/'+data.film_id+'"    \
                             class="btn btn-danger admin-edit control-item" \
                 										role="button" id="film-restore-control">Удалить</a>  \
                 			  </li> </ul>');
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

$(document).ready(function() {
var height_film = $('.film-logo-full').height();
var height_text= $('#film-text').height();
var res = Number(height_film)-Number(height_text)-40;
if (!$("#user_name").val() == undefined) {
  if ($("#user_name").val().length > 0) {
    res = 0;
  } else {
    $('.reviews-title.s').attr('style', 'margin-top: '+res+'px');
  }
}
$('.reviews-title.s').attr('style', 'margin-top: '+res+'px');var data = [[0, $("#s_1").val()],[1, $("#s_2").val()],[2, $("#s_3").val()],
      [3, $("#s_4").val()],[4, $("#s_5").val()],[5, $("#s_6").val()],
        [6, $("#s_7").val()], [7, $("#s_8").val()], [8, $("#s_9").val()],
          [9, [$("#s_10").val()]]];

var dataset = [{ label: $("#stat_title").val() , data: data, color: "#5482FF" }];
var ticks = [[0, "1"], [1, "2"], [2, "3"], [3, "4"], [4, "5"], [5, "6"],
                [6, "7"], [7, "8"], [8, "9"], [9, "10"]];

     var options = {
         series: {
             bars: {
                 show: true
             }
         },
         bars: {
             align: "center",
             barWidth: 0.7
         },
         xaxis: {
             axisLabel: "Оценка",
             axisLabelUseCanvas: true,
             axisLabelFontSizePixels: 12,
             axisLabelFontFamily: 'Verdana, Arial',
             axisLabelPadding: 10,
             ticks: ticks
         },
         yaxis: {
             axisLabel: "Количество оценок",
             axisLabelUseCanvas: true,
             axisLabelFontSizePixels: 12,
             axisLabelFontFamily: 'Verdana, Arial',
             axisLabelPadding: 3,
             tickFormatter: function (v, axis) {
                 return v + "";
             }
         },
         legend: {
             noColumns: 0,
             labelBoxBorderColor: "#000000",
             position: "nw"
         },
         grid: {
             hoverable: true,
             borderWidth: 2,
             backgroundColor: { colors: ["#ffffff", "#EDF5FF"] }
         }
     };

     $(document).ready(function () {
         $.plot($("#flot-placeholder"), dataset, options);
         $("#flot-placeholder").UseTooltip();
     });

     function gd(year, month, day) {
         return new Date(year, month, day).getTime();
     }

     var previousPoint = null, previousLabel = null;

     $.fn.UseTooltip = function () {
         $(this).bind("plothover", function (event, pos, item) {
             if (item) {
                 if ((previousLabel != item.series.label) || (previousPoint != item.dataIndex)) {
                     previousPoint = item.dataIndex;
                     previousLabel = item.series.label;
                     $("#tooltip").remove();

                     var x = item.datapoint[0];
                     var y = item.datapoint[1];

                     var color = item.series.color;

                     //console.log(item.series.xaxis.ticks[x].label);

                     showTooltip(item.pageX,
                     item.pageY,
                     color,
                     "<strong>" + item.series.label + "</strong><br>" + item.series.xaxis.ticks[x].label + " : <strong>" + y + "</strong> ");
                 }
             } else {
                 $("#tooltip").remove();
                 previousPoint = null;
             }
         });
     };

     function showTooltip(x, y, color, contents) {
         $('<div id="tooltip">' + contents + '</div>').css({
             position: 'absolute',
             display: 'none',
             top: y - 40,
             left: x - 120,
             border: '2px solid ' + color,
             padding: '3px',
             'font-size': '9px',
             'border-radius': '5px',
             'background-color': '#fff',
             'font-family': 'Verdana, Arial, Helvetica, Tahoma, sans-serif',
             opacity: 0.9
         }).appendTo("body").fadeIn(200);
     }
});
