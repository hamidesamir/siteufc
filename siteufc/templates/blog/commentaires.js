var commentaires = document.getElementById("commentaire");
commentaires.addEventListener("keyup",comment);

function comment(){
							if (commentaires.value.length>6) {
								alert("time to comment");
							}
							
						}
window.onload = commentaires;

/*
var champMotDePass = document.getElementById("champPassword");
var inputMotDePass = document.getElementById("user_password");



inputMotDePass.addEventListener("keyup",confirmation);

function confirmation()
{
	if (inputMotDePass.value.length<6) {
		champMotDePass.style.color="bleu";
	}

	else{
		champMotDePass.style.color="green";
		document.body.style.background="red";
	}
}
*/