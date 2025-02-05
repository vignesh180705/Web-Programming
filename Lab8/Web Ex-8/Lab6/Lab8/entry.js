function calc(){
    a=parseInt(document.getElementById("adult").value);
    c=parseInt(document.getElementById("children").value);
    t=a*10+c*5
    document.getElementById("total").value=t;
}