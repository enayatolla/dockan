async function likeByMeHandler() {
   let article_id = +document.getElementById("article_id_value").innerHTML;

   // $.get(`/like/${article_id}`).then((res) => {
   //    like(response.like_by_me);
   // });

   function likeByMe(result) {
      let tag = document.getElementById("like_by_me_icon");
      let counter = document.getElementById("like_by_me_counter");

      if (result) {
         tag.className = "fas fa-heart";
         counter.innerHTML = parseInt(counter.innerHTML) + 1;
      } else {
         tag.className = "far fa-heart";
         counter.innerHTML = parseInt(counter.innerHTML) - 1;
      }
   }

   $.ajax({
      type: "POST",
      url: "/like/",
      data: {
         article_id: article_id,
      },
      beforeSend: function (xhr, settings) {
         function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== "") {
               var cookies = document.cookie.split(";");
               for (var i = 0; i < cookies.length; i++) {
                  var cookie = jQuery.trim(cookies[i]);
                  // Does this cookie string begin with the name we want?
                  if (cookie.substring(0, name.length + 1) === name + "=") {
                     cookieValue = decodeURIComponent(
                        cookie.substring(name.length + 1)
                     );
                     break;
                  }
               }
            }
            return cookieValue;
         }
         if (
            !(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))
         ) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
         }
      },
      success: function (response) {
         likeByMe(response.like_by_me);
      },
      error: function (xhr, errmsg, err) {
         // برای پردازش خطاهای احتمالی
         console.log(xhr, errmsg, err);
      },
   });
}

async function addToCart() {}
