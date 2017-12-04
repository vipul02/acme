/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
// function myFunction() {
//     var x = document.getElementById("myTopnav");
//     if (x.className === "topnav") {
//         x.className += " responsive";
//     } else {
//         x.className = "topnav";
//     }
// }


// Get the navbar
var navbar = document.getElementById("myTopnav");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
//   if (window.pageYOffset >= sticky) {
//     navbar.classList.add("sticky")
//   } else {
//     navbar.classList.remove("sticky");
//   }
// }


// sidenav func
function openNav() {
    document.getElementById("mySidenav").style.width = "300px";
    // document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.8)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    // document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}

function openNav1() {
    document.getElementById("mySidenav1").style.width = "300px";
    // document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.8)";
}

function closeNav1() {
    document.getElementById("mySidenav1").style.width = "0";
    // document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}

function openNav2() {
    document.getElementById("mySidenav2").style.width = "300px";
    // document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.8)";
}

function closeNav2() {
    document.getElementById("mySidenav2").style.width = "0";
    // document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}


// function to replace contact box on query submission
function query_submitted(){
    window.alert('Your problem has been received\nWe will get into touch shortly');
}



// Get the modal  modals js
// Get the modal
var modal = [
    document.getElementById('myModal0'), document.getElementById('myModal1'), document.getElementById('myModal2'),
    document.getElementById('myModal3'),document.getElementById('myModal4'),document.getElementById('myModal5'),
    document.getElementById('myModal6'),document.getElementById('myModal7'),document.getElementById('myModal8'),
    document.getElementById('myModal9'),document.getElementById('myModal10'),document.getElementById('myModal11'),
    document.getElementById('myModal12'),document.getElementById('myModal13'),document.getElementById('myModal14'),
    document.getElementById('myModal15'),document.getElementById('myModal16'),document.getElementById('myModal17'),
    document.getElementById('myModal18'),document.getElementById('myModal19'),document.getElementById('myModal20'),
    document.getElementById('myModal21')];

// When the user clicks the button, open the modal
function open_form(n) {
    modal[n].style.display = "block";
    document.getElementsByClassName('dname').innerHTML = document.getElementsByClassName('btn1').innerHTML;
}

// When the user clicks on <span> (x), close the modal
function close_form(n) {
    modal[n].style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	for(var z=0;z<modal.length;z++){
    	if (event.target == modal[z]) {
        	modal[z].style.display = "none";
    	}
    }
};


$(document).ready(function(){
	$("#myBtn").click(function(){
        $("#device").attr("value",$("#myBtn").text());
    });
});
