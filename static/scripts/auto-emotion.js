// Function to automate the microsoft api call

const interval = 5;

var timer;
var timer_flag = 0;

// Counting function
function timedCount(func) {
    timer = setTimeout(function () {
        func(); timedCount(function () { func(); });
        } , interval * 1000);
    };

// Starts the counting
function startCount(func) {
    console.log("Recording started");
    if (!timer_flag) {
        timer_flag = 1;
        timedCount(function () { func(); });
    }
}

// Stops the counting
function stopCount() {
    clearTimeout(timer);
    timer_flag = 0;
    console.log("Recording terminated");
}