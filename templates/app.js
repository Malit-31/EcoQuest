function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username !== "" && password !== "") {
        fetch("http://127.0.0.1:5000/savedata")
            .then(response => response.json())
            .then(users => {
                const user = users.find(user => user.username === username && user.password === password);
                if (user) {
                    window.location.href = "questclaim.html";
                } else {
                    alert("wrong username and password");
                }
            })
            .catch(error => console.error('Error fetching users:', error));
    } else {
        alert("Please fill out all fields");
    }
}
function createacc(){
    
}