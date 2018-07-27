$("#comment-form").on('submit', function(event){
  let data_post = $("#comment-form").serialize();
  event.preventDefault();
  console.log("form_submit");
  create_comment(data_post);
})
function create_comment(data_post){
  $.ajax({
    url: '',
    method: "POST",
    data : data_post,
    success: function(data){
      $('#comment-text').val('');
      $('#comments').prepend("<li>"+data.text+'</li>');
    },
    error: function(xhr,errmsg,err){
      $('#results').html("Error");
    }
  });
}

// ДЛЯ ИЗУЧЕНИЯ
// headers: { "X-CSRFToken": $.cookie("csrftoken") },

//РАБОЧИЙ ВАРИАНТ
// test3.html
// <script type='text/javascript'>
//   var jsurl="{% url 'create_comment' %}";
// </script>
// $('#comment-form').submit(function(e){
//   var data_text = $("#comment-text").val();
//   console.log(jsurl+"            "+data_text);
//   console.log($(this).serialize());
//   $.post(jsurl,$(this).serialize(),function(data){
//     $('#comment-text').val('');
//     $('#comments').prepend("<li>"+data.text+'</li>');
//   });
//   e.preventDefault();
// });
