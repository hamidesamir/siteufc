function displayTime() {
						var elt = document.getElementById("clock"); // Find element with id="clock"
						var now = new Date();
						elt.innerHTML = now.toLocaleTimeString(); 
						setTimeout(displayTime, 1000);
}

window.onload = displayTime;
