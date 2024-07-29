function myFunction(){
    if (document.getElementById("username").value!=="" && document.getElementById("password").value!=="") {
        window.location.href="questclaim.html"
    }
    else{
        alert("Please fill out all fields")
    }
 }
