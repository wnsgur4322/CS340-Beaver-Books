//function for login identification
var username = ["kimchi@gmail.com"];
var password = ["taco"];

function redirect(){
    window.location ="http://web.engr.oregonstate.edu/~jeongju/beaver-books/index.html";
    return false;
}

  function check(){
    var redirect_true = 0;
    console.log(username.length)
    for(var i = 0; i < username.length; i++){
      username[i] = username[i].toLowerCase();
      console.log(document.getElementById('useremail').value)
      console.log(document.getElementById('pswrd').value)
  
      if(document.getElementById('useremail').value == username[i] && document.getElementById('pswrd').value == password[i]){
        redirect_true = 1;
        console.log("yes")
      }
    }
    if(redirect_true == 1){
       
      //window.open(document.getElementById('userid').value); <- for interaction with js node
      alert("login successful with admin account");
      window.open("http://web.engr.oregonstate.edu/~jeongju/beaver-books/index.html");
      redirect()
    }
    if(redirect_true == 0){
      alert("Check your email or password!");
    }
  }

  var login_button = document.getElementById("login_button");
  login_button.addEventListener('click', check);
