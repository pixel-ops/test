$(document).ready(function () {
  count = 0;
  total_score = 0;
  var option = [];

  $(".my").html(`<h1>Start the quiz </h1>`);
  $(".next").click(function (event) {
    count += 1;
    url =window.location.pathname.replace("quiz/", "api/quiz/") + "?page=" + count;

    $.ajax({
      url: url,
      method: "GET",
      timeout: 0,
      headers: {
        Authorization:
        `Bearer ${window.localStorage.getItem('accessToken')}`,
      },
    })

      .done(function quiz(data) {
        console.log(data)
        // Triggered if response status code is 200 (OK)
        if (data) {
          var item = $(`
          <h1>Question- ${data[0].question}</h1>`);
          if (data[0].answer.length == 1) {
            for (i = 0; i < data[0].options.length; i++) {
              if (data[0].current_answer[0]){
              if (data[0].options[i].option == data[0].current_answer[0].answer){
                item.append(
                  `<div><input type="radio" class='btn' id="r1" name="rate" value="${data[0].options[i].option}" checked> ${data[0].options[i].option}<br><hr></div>`
                );
                continue;
              }
            }
              item.append(
                `<div><input type="radio" class='btn' id="r1" name="rate" value="${data[0].options[i].option}"> ${data[0].options[i].option}<br><hr></div>`
              );
            }
          } else {
            for (i = 0; i < data[0].options.length; i++) {
              let optionChecked = false;
            
              if (data[0].current_answer) {
                for (j = 0; j < data[0].current_answer.length; j++) {
                  if (data[0].options[i].option == data[0].current_answer[j].answer) {
                    optionChecked = true;
                    break;
                  }
                }
              }
            
              if (optionChecked) {
                item.append(
                  `<div><input type="checkbox" class='btn' id="r1" name="rate" value="${data[0].options[i].option}" checked> ${data[0].options[i].option}<br><hr></div>`
                );
              } else {
                item.append(
                  `<div><input type="checkbox" class='btn' id="r1" name="rate" value="${data[0].options[i].option}"> ${data[0].options[i].option}<br><hr></div>`
                );
              }
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
                  for (i=0;i<my_data.length;i++){
                    if (my_data[i].question == data[0].id){
                      delete_answer(my_data[i].id);
                    }
                  }
                  add_Answer(option, data);
                }
              } else {
                my_data = await get_answer();
                for (i=0;i<my_data.length;i++){
                  if (my_data[i].question == data[0].id){
                    delete_answer(my_data[i].id);
                  }
                }
                add_Answer(option,data);
                if (total_score) {
                  total_score -= 1;
                }
              }
            } else {
              function getCheckedBoxes(chkboxName,data) {
                var checkboxes = document.getElementsByName(chkboxName);
                var checkboxesChecked = [];
                // loop over them all
               
                for (var i = 0; i < checkboxes.length; i++) {
                  // And stick the checked ones onto an array...
                  if (checkboxes[i].checked) {
                    add_Answer(checkboxes[i].value,data)
                    checkboxesChecked.push(checkboxes[i].value);
                  }
                }
                // Return the array if it is non-empty, or null
                return checkboxesChecked.length > 0 ? checkboxesChecked : null;
              }

              my_data = await get_answer();
              console.log(my_data)
              for (i=0;i<my_data.length;i++){
                if (my_data[i].question == data[0].id){
                  delete_answer(my_data[i].id);
                }
              }

              var checkedBoxes = getCheckedBoxes("rate",data);
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
          });
        }
        setTimeout(async() => {
          my_data = await get_answer();
          console.log(my_data)
          for (i=0;i<my_data.length;i++){
              delete_answer(my_data[i].id);
          }
          $(".my").html(`<h1>Quiz ended <br><br><br>Score- ${total_score}</h1>`          );
          $(".some_div").remove();
          $(".next").remove();
        }, 50000);
      })
      .fail(async function () {
        // Triggered if response status code is NOT 200 (OK)
        my_data = await get_answer();
              console.log(my_data)
              for (i=0;i<my_data.length;i++){
                  delete_answer(my_data[i].id);
              }
        $(".my").html(`<h1>Quiz ended <br><br><br>Score- ${total_score}</h1>`);
        $(".some_div").remove();
        $(".next").remove();
      });
  });

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
      success: function (data) {
      },
      error: function (xhr, textStatus, errorThrown) {
        console.log(xhr.responseText);
      },
    });
  }

  function delete_answer(id){
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    $.ajax({
      url: 'http://127.0.0.1:8000/api/Current_answer/'+id,
      type: 'DELETE',
      data: {},
      contentType:'application/json',
      dataType: 'json',
      headers: {
        "X-CSRFToken": csrfToken,
      },
      error: function(result){},
      success: function(result) {console.log('deleted successfully')}
  });
  }
  async function get_answer(){
    var a = []
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
    await $.ajax({
      url: 'http://127.0.0.1:8000/api/Current_answer/',
      type: 'GET',
      data: {},
      contentType:'application/json',
      dataType: 'json',
      headers: {
        "X-CSRFToken": csrfToken,
      },
      error: function(data){console.log(data)},
      success: function(data) {a = data}
  });
  return a
  }
});
