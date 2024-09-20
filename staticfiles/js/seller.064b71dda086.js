function validate(){
  user=document.getElementById('un').value
  password= document.getElementById('ps').value

  if(user==""){
    document.getElementById('msg').innerHTML='please enter the username'
    return false
  }else if(password==""){
    document.getElementById('msg').innerHTML='please enter the password'
    return false
  }else{
    return true
  }
}