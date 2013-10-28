var message = document.getElementById("commentaire");
message.addEventListener("keyup",comment);

function comment(){
							if (message.value.length>6) {
								alert(message.value);
							}
							
						}
window.onload = comment;