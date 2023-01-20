let ans = document.getElementById('inp').value;  
var value = "";
var mem = 0;

// let reg = /^\s*([-+]?)(\d+)(?:\s*([-+*\/])\s*((?:\s[-+])?\d+)\s*)+$/;
// from other website let reg = /^(?!\.)(?!.*\.$)(?!.*\.\.)[a-zA-Z0-9_.]+$/;
// let reg = /^[\d()+\-*/\s]*(\*\*[\d()+\-*/\s]*)*$/;
// let reg = /^(?:\d+\.\d*|\.\d+|\d+|[+\-*/^()]|\*\*)+$/;
// let reg = /^(-?\d+.?\d*)([/+-**])(-?\d+.?\d*)$/;
// let reg =/^\d+((\.\d+)?[\+\-×÷]\d+(\.\d+)?)+$/
let reg = /^[\d\+\-\*\/\(\)\.]*(\*\*[\d\+\-\*\/\(\)\.]+)*$/;

//main function that takes input
function myfunction(event){
    value += event.target.value;
    document.getElementById("inp").value = value;
}
// function to check string for input validation using regex
function check_str(){
    console.log("in check_str");
    if(value.match(reg)){
        return true;
    }
    else{
        return false;
    }
}

//function that evaluates the expression 
function evaluatess(){
    if(value != ""){
        // if(check_str()){
            ans = eval(value);
            document.getElementById("inp").value = ans.toPrecision(13);
            value = ans.toPrecision(13); 

        // }
        // else{
        //     document.getElementById('inp').value = "Error";
        // }
    }
}
//clear the input field
function clear_me(){
    document.getElementById("inp").value = 0;
    value = ""; 
}
//delete the last element in input field
function delete_last(){
    document.getElementById("inp").value = value.slice(0,value.length-1);
    value = value.slice(0,value.length-1);
    if(value == ""){
        document.getElementById("inp").value = 0;
        value = "";
    }
}
//square function
function sqr(){
    document.getElementById("inp").value = (parseFloat(value)*parseFloat(value)).toPrecision(13);
    value = (parseFloat(value)*parseFloat(value)).toPrecision(13);
}
// function for degree function
function DEG(event){
    val = document.getElementById("inp").value
       if(val != ""){
           document.getElementById("inp").value = eval((parseInt(value*22)/1260).toPrecision(13));
           value = eval((parseInt(value*22)/1260).toPrecision(13));
       }
       else{
           document.getElementById("inp").value = "0.01746";
           value = "0.01746";
       }
}

// function for fixed exponent
function F_E(){
    document.getElementById("inp").value = parseFloat(value).toExponential(2);
    value = parseFloat(value).toExponential(2);
}


// check value of input and accordingly put value of pi
function pi_check(event){
    val = document.getElementById("inp").value
    console.log(val);
       if(val != 0){
           document.getElementById("PI").value = "*3.14";
           myfunction(event);
       }
       else{
           document.getElementById("PI").value = "3.14";
           myfunction(event);
       }
}
// check value of input and accordingly put value of e
function e_check(event){
    val = document.getElementById("inp").value
       if(val != 0  ){
           document.getElementById("e").value = "*2.71";
           myfunction(event);
       }
       else{
           document.getElementById("e").value = "2.71";
           myfunction(event);
       }
}


//reciprocal function
function reciprocal(){
    document.getElementById("inp").value = eval(1/parseFloat(value)).toPrecision(13);
    value = eval(1/parseFloat(value)).toPrecision(13);
}
//to get absolute value
function myabs(){
    document.getElementById("inp").value = Math.abs(parseFloat(value)).toPrecision(13);
    value = Math.abs(parseFloat(value)).toPrecision(13);
}
//find e^value
function exponent(){
    document.getElementById("inp").value = Math.exp(parseFloat(value)).toPrecision(13);
    value = Math.exp(parseFloat(value)).toPrecision(13);
}
//find square root
function squarert(){
    document.getElementById("inp").value = Math.sqrt(parseFloat(value)).toPrecision(13);
    value = Math.sqrt(parseFloat(value)).toPrecision(13);
}
// finds 10^value
function ten_raise_to_x(){
    document.getElementById("inp").value = Math.pow(10,parseFloat(value)).toPrecision(13);
    value = Math.pow(10,value).toPrecision(13);
}
// finds logarthim
function logarithm(){
    document.getElementById("inp").value = Math.log(parseFloat(value)).toPrecision(13);
    value = Math.log(parseFloat(value)).toPrecision(13);
}
// finds natural log
function natural_log(){
    e = 2.71828182846;
    document.getElementById("inp").value = Math.log(e,parseFloat(value));
}

// function to save the value to value to memory
function store_mem(){
    mem = value;
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
    value = factorialize(parseInt(value)).toPrecision(13);
}
//sin function
function sin(){
    document.getElementById("inp").value = Math.sin((parseInt(value)*Math.PI)/180).toPrecision(13);
    value = Math.sin((parseInt(value)*Math.PI)/180).toPrecision(13);
}
// cos function
function cos(){
    document.getElementById("inp").value = Math.cos((parseInt(value)*Math.PI)/180).toPrecision(13);
    value = Math.cos((parseInt(value)*Math.PI)/180).toPrecision(13);
}
// tan function
function tan(){
    document.getElementById("inp").value = Math.tan((parseInt(value)*Math.PI)/180).toPrecision(13);
    value = Math.tan((parseInt(value)*Math.PI)/180).toPrecision(13);
}
// sec function
function sec(){
    document.getElementById("inp").value = 1/(Math.cos((parseInt(value)*Math.PI)/180)).toPrecision(13);
    value = 1/(Math.cos((parseInt(value)*Math.PI)/180)).toPrecision(13);
}
// cosec function
function cosec(){
    document.getElementById("inp").value = 1/(Math.sin((parseInt(value)*Math.PI)/180)).toPrecision(13);
    value = 1/(Math.sin((parseInt(value)*Math.PI)/180)).toPrecision(13);
}
// cot function
function cot(){
    document.getElementById("inp").value = 1/(Math.tan((parseInt(value)*Math.PI)/180)).toPrecision(13);
    value = 1/(Math.tan((parseInt(value)*Math.PI)/180)).toPrecision(13);
}