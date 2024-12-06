
document.addEventListener("DOMContentLoaded", function () {
    
    const tasks = document.querySelectorAll("tr[data-deadline]");
    const currentDate = new Date();  // Getting the current date
    const popup = document.getElementById('taskReminder');
    const message = document.getElementById('body-popup-message');

    const closeHeaderButton = document.getElementById('popup-close-header');
    const closeFooterButton = document.getElementById('popup-close-footer');

    tasks.forEach(function (task) {
        const taskDeadline = new Date(task.getAttribute("data-deadline"));
        const timeDifference = taskDeadline - currentDate;
        const assignedUser = task.getAttribute("task-assigned-user");
        const wasTaskCompleted = task.getAttribute("task-assigned-completed");
        const daysDifference = timeDifference / (1000 * 3600 * 24); // Converting to days

        const message = document.getElementById('body-popup-message');

        // console.log(assignedUser)
        // console.log(loggedUser)
        // console.log(wasTaskCompleted)
        //show only if the task in question is assigned to the logged user and the task wasn't completed
        if(loggedUser == assignedUser && wasTaskCompleted == "False"){
            // Check if deadline is within 2 days or if it has has already passed
            if (daysDifference <= 3 && daysDifference > 0) {
                message.textContent = `Reminder: Task '${task.querySelector("td a").textContent}' assigned to you (${assignedUser}) is due in ${Math.ceil(daysDifference)} days.`;
            } else if (daysDifference < 0) {
                message.textContent = "Task '" + task.querySelector("td a").textContent + "' deadline has passed!";
            }
        }
    });

    if (closeHeaderButton) {
        closeHeaderButton.addEventListener('click', (event) => {
            event.stopPropagation();
            if (popup) {
                popup.style.display = 'none'; 
            }
        });
    }

    if (closeFooterButton) {
        closeFooterButton.addEventListener('click', (event) => {
            event.stopPropagation();
            if (popup) {
                popup.style.display = 'none'; 
            }
        });
    }

});
