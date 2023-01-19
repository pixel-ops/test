let ans = document.getElementById('inp').value;  
var value = "";
var mem = 0;

//from stack overflow let reg = /^\s*([-+]?)(\d+)(?:\s*([-+*\/])\s*((?:\s[-+])?\d+)\s*)+$/;
//from other website let reg = /^(?!\.)(?!.*\.$)(?!.*\.\.)[a-zA-Z0-9_.]+$/;
// from chatgpt let reg = /^[\d()+\-*/\s]*(\*\*[\d()+\-*/\s]*)*$/;

//main function that takes input
function myfunction(event){
    value += event.target.value;
    document.getElementById("inp").value = value;
}
//function that evaluates the expression 
function evaluatess(){
    if(value != ""){
        // if(value.match(reg)){
            ans = eval(value);
            document.getElementById("inp").value = ans;
            value = ans;
        // }
        // else{
        //     document.getElementById('inp').value = "Error";
        // }
    }
}
//clear the input field
function clear_me(){
    document.getElementById("inp").value = "";
    value = ""; 
}
//delete the last element in input field
function delete_last(){
    document.getElementById("inp").value = value.slice(0,value.length-1);
    value = value.slice(0,value.length-1);
}
//square function
function sqr(){
    console.log(value);
    document.getElementById("inp").value = parseFloat(value)*parseFloat(value);
    value = parseFloat(value)*parseFloat(value);
}
//reciprocal function
function reciprocal(){
    document.getElementById("inp").value = eval(1/parseFloat(value));
    value = eval(1/parseFloat(value));
}
//to get absolute value
function myabs(){
    document.getElementById("inp").value = Math.abs(parseFloat(value));
    value = Math.abs(parseFloat(value));
}
//find e^value
function exponent(){
    document.getElementById("inp").value = Math.exp(parseFloat(value));
    value = Math.exp(parseFloat(value));
}
//find square root
function squarert(){
    document.getElementById("inp").value = Math.sqrt(parseFloat(value));
    value = Math.sqrt(parseFloat(value));
    console.log(eval(2**3));
}
// finds 10^value
function ten_raise_to_x(){
    document.getElementById("inp").value = Math.pow(10,parseFloat(value));
    value = Math.pow(10,value);
}
// finds logarthim
function logarithm(){
    document.getElementById("inp").value = Math.log(parseFloat(value));
    value = Math.log(parseFloat(value));
}
// finds natural log
function natural_log(){
    e = 2.71828182846
    document.getElementById("inp").value = Math.log(e,parseFloat(value));
}

// function to save the value to value to memory
function store_mem(){
    mem = value;
    console.log(mem);
}
//recall memory value
function recall_mem(){
    document.getElementById("inp").value = mem;
    value = mem;
}
//clear memory value
function clear_mem(){
    mem = 0;
}
// memory add 
function add_mem(){
    mem = parseInt(value) + parseInt(mem);
    document.getElementById("inp").value = mem;
}
// memory sub 
function add_sub(){
    mem = parseInt(mem)-parseInt(value); 
    document.getElementById("inp").value = mem;
    
}
// factorial function
function factorialize(num) {
    if (num < 0) 
          return -1;
    else if (num == 0) 
        return 1;
    else {
        return (num * factorialize(num - 1));
    }
  }
// factorial calling function
function fact(){
    document.getElementById("inp").value = factorialize(parseInt(value));
}

function sin(){
    document.getElementById("inp").value = Math.sin((parseInt(value)*Math.PI)/180);
}
function cos(){
    document.getElementById("inp").value = Math.cos((parseInt(value)*Math.PI)/180);
}
function tan(){
    document.getElementById("inp").value = Math.tan((parseInt(value)*Math.PI)/180);
}
function sec(){
    document.getElementById("inp").value = 1/(Math.cos((parseInt(value)*Math.PI)/180));
}
function cosec(){
    document.getElementById("inp").value = 1/(Math.sin((parseInt(value)*Math.PI)/180));
}
function cot(){
    document.getElementById("inp").value = 1/(Math.tan((parseInt(value)*Math.PI)/180));
}