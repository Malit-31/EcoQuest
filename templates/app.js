function myFunction(){
    fetch(IP, {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({"password":69420,"username":"harharhar"})
     }).then(response => response.json()).then(data => {
         //do tanning with data
     })
    if (document.getElementById("username").value!=="" && document.getElementById("password").value!=="") {
        window.location.href="questclaim.html"
    }
    else{
        alert("Please fill out all fields")
    }
 }
