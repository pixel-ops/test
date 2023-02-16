var value = "";
var mem = 0;

//main function that takes input
function myfunction(event){
    value += event.target.value;
    document.getElementById("inp").value = value;
}


//function that evaluates the expression 
function evaluatess(){
    let check = String(eval(value)).includes(".");
    if(value != ""){
        if(check){
           value = eval(value);
           document.getElementById("inp").value = value = Number(value).toFixed(3);
        }
        else{
            value = eval(value);
           document.getElementById("inp").value = value = value;
        }
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
    document.getElementById("inp").value = value = (parseFloat(value)*parseFloat(value)).toPrecision(3);
}
// function for degree function
function DEG(event){
    val = document.getElementById("inp").value
       if(val != ""){
           document.getElementById("inp").value = value = eval((parseInt(value*22)/1260).toPrecision(1));
       }
       else{
           document.getElementById("inp").value = "0.01746";
           value = "0.01746";
       }
}

// function for fixed exponent
function F_E(){
    document.getElementById("inp").value = value = parseFloat(value).toExponential(2);
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
       if(val != 0){
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
    document.getElementById("inp").value = value = eval(1/parseFloat(value)).toPrecision(3);
}
//to get absolute value
function myabs(){
    document.getElementById("inp").value = value = Math.abs(parseFloat(value)).toPrecision(3);
}
//find e^value
function exponent(){
    document.getElementById("inp").value = value = Math.exp(parseFloat(value)).toPrecision(3);
}
//find square root
function squarert(){
    document.getElementById("inp").value = value = Math.sqrt(parseFloat(value)).toPrecision(3);
}
// finds 10^value
function ten_raise_to_x(){
    document.getElementById("inp").value = value = Math.pow(10,parseFloat(value)).toPrecision(3);
}
// finds logarthim
function logarithm(){
    document.getElementById("inp").value = value = Math.log(parseFloat(value)).toPrecision(3);
}
// finds natural log
function natural_log(){
    e = 2.71828182846;
    document.getElementById("inp").value= value = Math.log(e,parseFloat(value));
}

// function to save the value to value to memory
function store_mem(){
    mem = value;
}
//recall memory value
function recall_mem(){
    document.getElementById("inp").value = value = mem;
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
    document.getElementById("inp").value = value = factorialize(parseInt(value));
}
//sin function
function sin(){
    document.getElementById("inp").value = value = Math.sin((parseInt(value)*Math.PI)/180).toPrecision(3);
}
// cos function
function cos(){
    document.getElementById("inp").value = value = Math.cos((parseInt(value)*Math.PI)/180).toPrecision(3);
}
// tan function
function tan(){
    document.getElementById("inp").value = value = Math.tan((parseInt(value)*Math.PI)/180).toPrecision(3);
}
// sec function
function sec(){
    document.getElementById("inp").value = value = 1/(Math.cos((parseInt(value)*Math.PI)/180)).toPrecision(3);
}
// cosec function
function cosec(){
    document.getElementById("inp").value = value = 1/(Math.sin((parseInt(value)*Math.PI)/180)).toPrecision(3);
}
// cot function
function cot(){
    document.getElementById("inp").value = value = 1/(Math.tan((parseInt(value)*Math.PI)/180)).toPrecision(3);
}