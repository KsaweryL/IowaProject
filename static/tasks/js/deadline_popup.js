
document.addEventListener("DOMContentLoaded", function () {
    const tasks = document.querySelectorAll("tr[data-deadline]");
    const currentDate = new Date();  // Getting the current date
    const modalElement = document.getElementById('taskReminderModal');
    const modalMessage = document.getElementById('modal-message');
    const modal = new bootstrap.Modal(modalElement);

    const closeHeaderButton = document.getElementById('closeHeaderButton');
    const closeFooterButton = document.getElementById('closeFooterButton');

    tasks.forEach(function (task) {
        const taskDeadline = new Date(task.getAttribute("data-deadline"));
        const timeDifference = taskDeadline - currentDate;
        const assignedUser = task.getAttribute("task-assigned-user");
        const daysDifference = timeDifference / (1000 * 3600 * 24); // Converting to days

        const modalMessage = document.getElementById('modal-message');
        const modal = new bootstrap.Modal(document.getElementById('taskReminderModal'));

        //show only if the task in question is assigned to the logged user
        if(loggedUser == assignedUser){
            // Check if deadline is within 2 days or if it has has already passed
            if (daysDifference <= 3 && daysDifference > 0) {
                modalMessage.textContent = `Reminder: Task '${task.querySelector("td a").textContent}' assigned to you (${assignedUser}) is due in ${Math.ceil(daysDifference)} days.`;
                modal.show();
            } else if (daysDifference < 0) {
                modalMessage.textContent = "Task '" + task.querySelector("td a").textContent + "' deadline has passed!";
                modal.show();
            }
        }
    });

    // console.log(closeHeaderButton)
    closeHeaderButton.addEventListener('click', function () {
        modal.hide();
    });

    closeFooterButton.addEventListener('click', function () {
        modal.hide();
    });

});
