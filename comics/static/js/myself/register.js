$(document).ready(function(){
    var account = document.getElementById('account')
    var accounterror = document.getElementById('accounterror')
    var checkerr = document.getElementById('checkerr')
    var passwd = document.getElementById('passwd')
    var passwderr = document.getElementById('passwderr')
    var passwdAgain = document.getElementById('passwd1')
    var passwdAgainerr = document.getElementById('passwderr1')

    account.addEventListener('focus', function(){
        accounterror.style.display = 'none'
        checkerr.style.display = 'none'
    }, false)

    account.addEventListener('blur', function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 12){
            accounterror.style.display = 'block'
            return
        }
        $.post('/checkuserid/', {'userid': instr}, function(data){
            if (data.status == 'error'){
                checkerr.style.display = 'block'
            }
        })
    }, false)

    passwd.addEventListener('focus', function(){
        passwderr.style.display = 'none'
    }, false)

    passwd.addEventListener('blur', function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 16){
            passwderr.style.display = 'block'
            return
        }
    }, false)

    passwdAgain.addEventListener('focus', function(){
        passwdAgainerr.style.display = 'none'
    }, false)

    passwdAgain.addEventListener('blur', function(){
        instr = this.value
        if(instr != passwd.value){
            passwdAgainerr.style.display = 'block'
        }
    }, false)
})