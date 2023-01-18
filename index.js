var a ;
var b ;

function calculator() {

    document.getElementById("one").onclick = write("one");

    // if()
    
}


function add(){    
    a = parseInt(document.getElementById("1").value);
    b = parseInt(document.getElementById("1").value);
    let c = a + b;
    document.getElementById("ans").innerHTML = c;
}

function sub(){    
    a = parseInt(document.getElementById("1").value);
    b = parseInt(document.getElementById("2").value);
    let c = a - b;
    document.getElementById("ans").innerHTML = c;
}

function mul(){    
    a = parseInt(document.getElementById("1").value);
    b = parseInt(document.getElementById("2").value);
    let c = a * b;
    document.getElementById("ans").innerHTML = c;
}

function div(){    
    a = parseInt(document.getElementById("1").value);
    b = parseInt(document.getElementById("2").value);
    let c = Number(a / b);
    document.getElementById("ans").innerHTML = c;
}
