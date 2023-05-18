if (window.localStorage.getItem('accessToken') == null){
$("#submit").click(function(event) {
    event.preventDefault();
    var form = new FormData();
    form.append('email', $('#email').val().trim());
    form.append('password', $('#password').val().trim());
  
    $.ajax({
      url: "http://127.0.0.1:8000/account/token/",
      type: "POST",
      data: form,
      cache: false,
      processData: false,
      contentType: false,
      success: function(data) {
        console.log(data);
        window.localStorage.setItem('refreshToken', data['refresh']);
        window.localStorage.setItem('accessToken', data['access']);
  
        // Retrieve CSRF token from cookies
        const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
        console.log(csrfToken);
  
        // Make second AJAX request with the CSRF token included in the headers
        $.ajax({
          url: "http://127.0.0.1:8000/login",
          type: "POST",
          headers: {
            'X-CSRFToken': csrfToken
          },
          data: null,
          cache: false,
          processData: false,
          contentType: false,
          success: function() {
            window.location = "http://127.0.0.1:8000"
          },
          error: function(rs, e) {
            console.error(rs.responseText);
          }
        });
      },
      error: function(rs, e) {
        console.error(rs.responseText);
      }
    });
  });
}
else{
    window.location = "http://127.0.0.1:8000"
}