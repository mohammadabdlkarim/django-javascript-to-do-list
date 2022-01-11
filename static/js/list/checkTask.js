const tasksElement = document.getElementById('tasks');
const tasksList = tasksElement.children;



for (element of tasksList) {
  if (element.nodeName == "DIV") {
    for (taskChildElement of element.children) {
      let taskId = taskChildElement.getAttribute("name");
      // div element contains the checkbox
      if (taskChildElement.nodeName == "DIV") {
        for (divChild of taskChildElement.children) {
          if (taskId !== null)
            divChild.addEventListener('click', () => {
              changeTaskStatus(taskId);
            })
        }
      }
      // input element is the content of the task
      else if (taskChildElement.nodeName == "INPUT") {
        
        taskChildElement.addEventListener('change', () => {
        taskToChange = document.getElementsByName(taskId);
        /*
          every task have two elements of its is as their names
          the input is always at id=1 since it's the second element
          as listed in the html file "list.html"
        */
        taskToChange = taskToChange[1];
          content = taskToChange.value;
        changeTaskContent(taskId, content);
        })
      }
    }
  }
}

function changeTaskContent(taskId, content) {
  let url = "change-task-content/1234556789012345/" + content;
    url = url.replace("1234556789012345", taskId);
  $.ajax({
    type: "GET",
    dataType: "json",
    url: url,
    timeout: 5000,
    error: (data) => {
      alert("Something Went Wrong: " + data["response"]);
    },
  });
}

function changeTaskStatus(taskId) {
  let url = "check-task/12345566776543459879458".replace(
    "12345566776543459879458",
    taskId
  );
  $.ajax({
    type: "GET",
    dataType: "json",
    url: url,
    timeout: 5000,
    error: (data) => {
      alert("Something Went Wrong: " + data["response"]);
    },
  });
}
