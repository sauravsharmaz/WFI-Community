window.onload= DarkMode()

function DarkMode() {
	body_elem= document.querySelector('body');
	nav_el= document.getElementById('Nav-dark');
	if (document.getElementById('DarkToggle').checked== true){
	  	body_elem.style.backgroundColor = 'black';
	    body_elem.style.color = 'white';
	    nav_el.className="navbar navbar-expand-lg navbar-dark bg-dark";
	    }
	else{
	  	body_elem.style.backgroundColor = "";
	    body_elem.style.color = "";
	  	nav_el.className="navbar navbar-expand-lg navbar-light bg-light";
	}
}
