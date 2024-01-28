
// // Function to set the mode in localStorage
// function setMode(mode) {
//     localStorage.setItem('mode', mode);
// }

// // Function to get the mode from localStorage
// function getMode() {
//     return localStorage.getItem('mode');
// }

// // Function to apply the mode
// function applyMode(mode) {
//     let body = document.querySelector("body");
//     let textElements = document.querySelectorAll(".text-content"); // Adjust the selector based on your structure
//     let h1element = document.querySelector("h1")

//     if (mode === "dark") {
//         body.style.background =  "#343a40";
//         body.style.color = "black";
//         h1element.style.color = "white";

//         // Apply white text color to text elements in dark mode
//         textElements.forEach(element => {
//             element.style.color = "white";
//         });
//     } else {
//         body.style.background = "white";
//         body.style.color = "black";
//         h1element.style.color = "black";

//         // Apply black text color to text elements in light mode
//         textElements.forEach(element => {
//             element.style.color = "black";
//         });
//     }
// }

// // Check if the mode is stored in localStorage
// let storedMode = getMode();

// // If the mode is stored, apply it; otherwise, set the default mode
// if (storedMode) {
//     applyMode(storedMode);
// } else {
//     setMode("light"); // Set the default mode if not stored
// }

// let modebtn = document.querySelector("#mode");
// let currmode = storedMode || "light"; // Use stored mode or default

// modebtn.addEventListener("click", () => {
//     if (currmode === "light") {
//         currmode = "dark";
//         setMode(currmode); // Save the mode in localStorage
//     } else {
//         currmode = "light";
//         setMode(currmode);
//     }
//     applyMode(currmode);
// });
