$(document).ready(async function () {
  var quiz_data = await get_quiz()
  console.log(quiz_data)
  total_score = quiz_data[0].total_marks;
  if (quiz_data[0].isCompleted == false){
  $(".my").html(`<h1>Start the quiz </h1>`);
  $(".next").click(function (event) {
    count = 0;
    count += 1;
    url =
      window.location.pathname.replace("quiz/", "api/quiz/") + "?page=" + count;

    $.ajax({
      url: url,
      method: "GET",
      timeout: 0,
      headers: {
        Authorization: `Bearer ${window.localStorage.getItem("accessToken")}`,
      },
    })

      .done(async function quiz(data) {
        if (data != 0) {
          var item = $(`
          <h1>Question- ${data[0].question}</h1>`);
          if (data[0].answer.length == 1) {
            for (i = 0; i < data[0].options.length; i++) {
              item.append(
                `<div><input type="radio" class='btn' id="r1" name="rate" value="${data[0].options[i].option}"> ${data[0].options[i].option}<br><hr></div>`
              );
            }
          } else {
            for (i = 0; i < data[0].options.length; i++) {
                item.append(
                  `<div><input type="checkbox" class='btn' id="r1" name="rate" value="${data[0].options[i].option}"> ${data[0].options[i].option}<br><hr></div>`
                );
            }
          }

          $(".my").html(item);
          total_correct_answer = 0;
          $(".btn").click(async function (event) {
            if (data[0].answer.length == 1) {
              var option = $('input[name="rate"]:checked').val();
              if (option == data[0].answer[0].answer) {
                var alreadyClicked = $(".btn").hasClass("clicked");
                if (!alreadyClicked) {
                  $(".btn").addClass("clicked");
                  total_score += 1;
                  my_data = await get_answer();
                  for (i = 0; i < my_data.length; i++) {
                    if (my_data[i].question == data[0].id) {
                      delete_answer(my_data[i].id);
                    }
                  }
                  add_Answer(option, data);
                }
              } else {
                my_data = await get_answer();
                for (i = 0; i < my_data.length; i++) {
                  if (my_data[i].question == data[0].id) {
                    delete_answer(my_data[i].id);
                  }
                }
                add_Answer(option, data);
                if (total_score) {
                  total_score -= 1;
                }
              }
            } else {
              function getCheckedBoxes(chkboxName, data) {
                var checkboxes = document.getElementsByName(chkboxName);
                var checkboxesChecked = [];

                for (var i = 0; i < checkboxes.length; i++) {
                  if (checkboxes[i].checked) {
                    add_Answer(checkboxes[i].value, data);
                    checkboxesChecked.push(checkboxes[i].value);
                  }
                }
                return checkboxesChecked.length > 0 ? checkboxesChecked : null;
              }

              my_data = await get_answer();
              for (i = 0; i < my_data.length; i++) {
                if (my_data[i].question == data[0].id) {
                  delete_answer(my_data[i].id);
                }
              }

              var checkedBoxes = getCheckedBoxes("rate", data);
              answer = data[0].answer;
              answer_list = answer.map((item) => item.answer);
              let allFounded = checkedBoxes.every((ai) =>
                answer_list.includes(ai)
              );
              if (allFounded == true) {
                total_correct_answer += 1;
              }
              if (total_correct_answer == data[0].answer.length) {
                if (allFounded == true) {
                  total_score += 1;
                }
                if (allFounded == false) {
                  total_score -= 1;
                }
              }
            }
            post_score(total_score);
          });
        }
        else{
          post_quiz();
          my_data = await get_answer();
              for (i = 0; i < my_data.length; i++) {
                  delete_answer(my_data[i].id);
              }
        $(".my").html(`<h1>Quiz ended <br><br><br>Score- ${total_score}</h1>`);
        $(".some_div").remove();
        $(".next").remove();
        }
        setTimeout(async () => {
          post_quiz();
          my_data = await get_answer();
              for (i = 0; i < my_data.length; i++) {
                  delete_answer(my_data[i].id);
              }
          $(".my").html(
            `<h1>Quiz ended <br><br><br>Score- ${total_score}</h1>`
          );
          $(".some_div").remove();
          $(".next").remove();
        }, 5000000);
      })
      .fail(async function () {
        post_quiz();
        my_data = await get_answer();
              for (i = 0; i < my_data.length; i++) {
                  delete_answer(my_data[i].id);
              }
        $(".my").html(`<h1>Quiz ended <br><br><br>Score- ${total_score}</h1>`);
        $(".some_div").remove();
        $(".next").remove();
      });
  });
}
else{
    $(".my").html(
      `<h1>You've already completed the quiz with a score of - ${quiz_data[0].total_marks} marks <br><br>Thank You</h1>
      <a href='http://127.0.0.1:8000/'>Home</a>
      `
    );
    $(".some_div").remove();
    $(".next").remove();
}

  function post_quiz() {
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    var my_data = {isCompleted: true };
    url =
    window.location.pathname.replace("quiz/", "api/quiz/")
    $.ajax({
      url: url,
      type: "PATCH",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      data: my_data,
      success: function (data) {},
      error: function (xhr, textStatus, errorThrown) {
        console.log(xhr.responseText);
      },
    });
  }

  function post_score(score) {
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    var my_data = {total_marks: score };
    url =
    window.location.pathname.replace("quiz/", "api/quiz/")
    $.ajax({
      url: url,
      type: "PATCH",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      data: my_data,
      success: function (data) {},
      error: function (xhr, textStatus, errorThrown) {
        console.log(xhr.responseText);
      },
    });
  }
  
  async function get_quiz() {
    var a = [];
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    url =
      window.location.pathname.replace("quiz/", "api/quiz/")
    await $.ajax({
      url: url,
      type: "GET",
      data: {},
      contentType: "application/json",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      error: function (data) {},
      success: function (data) {
        a = data;
      },
    });
    return a;
  }
  function add_Answer(option, data) {
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    var my_data = { question: data[0].id, answer: option };
    $.ajax({
      url: "http://127.0.0.1:8000/api/Current_answer/",
      type: "POST",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      data: my_data,
      success: function (data) {},
      error: function (xhr, textStatus, errorThrown) {
        console.log(xhr.responseText);
      },
    });
  }

  function delete_answer(id,dlt="") {
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    $.ajax({
      url: "http://127.0.0.1:8000/api/Current_answer/" + id,
      type: "DELETE",
      data: {},
      contentType: "application/json",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
        "delete":dlt
      },
      error: function (result) {},
      success: function (result) {
        console.log("deleted successfully");
      },
    });
  }
  async function get_answer() {
    var a = [];
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    await $.ajax({
      url: "http://127.0.0.1:8000/api/Current_answer/",
      type: "GET",
      data: {},
      contentType: "application/json",
      dataType: "json",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      error: function (data) {},
      success: function (data) {
        a = data;
      },
    });
    return a;
  }
});
