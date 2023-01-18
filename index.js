let ans = document.getElementById('inp').value;  
var value = "";
function myfunction(event){
    value += event.target.value;
    document.getElementById("inp").value = value;
    

}

function evaluatess(){
    ans = eval(value);
    console.log(ans,value);
    document.getElementById("inp").value = ans;
}


