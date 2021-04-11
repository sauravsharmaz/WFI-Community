document.body.onload= startup_functions()

function startup_functions(){	
	DarkMode();
}

function DarkMode() {
	var all_Ques_class = document.getElementsByClassName('question-card');
	var all_Comment_class = document.getElementsByClassName('commentBox');
	body_elem= document.querySelector('body');
	nav_el= document.getElementById('Nav-dark');
	if (document.getElementById('DarkToggle').checked== true){
	  	body_elem.style.backgroundColor = 'black';
			body_elem.style.color = 'white';
	    nav_el.className="navbar navbar-expand-lg navbar-dark bg-dark";
			for (var i = 0; i < all_Comment_class.length; i++) {
	    	all_Comment_class[i].style.color= 'red';
	    }
			for (var i = 0; i < all_Ques_class.length; i++) {
	    	all_Ques_class[i].style.color= 'black';
	    }
	    
	}
	else{
	  	body_elem.style.backgroundColor = "";
			body_elem.style.color = "";
	  	nav_el.className="navbar navbar-expand-lg navbar-light bg-light";
	  	for (var i = 0; i < all_Ques_class.length; i++) {
	    	all_Ques_class[i].style.color= 'black';
	    }
	  	for (var i = 0; i < all_Comment_class.length; i++) {
	    	all_Comment_class[i].style.color= 'green';
	    }
	}
}
