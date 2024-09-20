function validate(){
    names=document.getElementById('firstName').value
    email= document.getElementById('email').value
    password=document.getElementById('password').value
    repassword=document.getElementById('repassword').value

    if (names==''){
        document.getElementById('msg').innerHTML='Please enter your name'
        return false
    }if(email==''){
        document.getElementById('msg1').innerHTML='plzz enter the email'
        return false
    }else if(password==''){
        document.getElementById('msg2').innerHTML='plzz enter the password'
        return false
    }else if(repassword==''){
        document.getElementById('msg3').innerHTML='plzz re-enter the password'
        return false
    }else if(password!=repassword){
        document.getElementById('msg3').innerHTML='Missmatched the password'
        return false
    }
    
    else{
        return true
    }

}