/*
Neatle -- Stefan Tan, Emily Lee
SoftDev1 pd6
K#29 -- Sequential Progression II: Electric Boogaloo
2018-12-20  
*/

var fibonacci=function(num){
    if(num==0){
	return 0;
    }
    else if(num==1){
	return 1;
    }
    else{
	return fibonacci(num-1)+fibonacci(num-2);
    }
};

var gcd=function(a,b){
    if(a == 0)
	return b;
    return gcd(b%a,a);
};

var students = ["Bob", "Steve", "Kevin", "Tim", "Wally", "Tom", "Jane"];

var randomStudent=function(){
    var num=Math.floor(Math.random() * students.length)
    return students[num];
};

var ans = document.getElementById("ans");

var fibbut = document.getElementById("a");

var fib7 = function() {
    var result = fibonacci(7);
    console.log(result);
    ans.innerHTML = result;
};

var gcdbut = document.getElementById("b");

var gcd32_24 = function() {
    var result = gcd(32, 24);
    console.log(result);
    ans.innerHTML = result;
};

var rsbut = document.getElementById("c");

var randstud = function() {
    var result = randomStudent();
    console.log(result);
    ans.innerHTML = result;
};

fibbut.addEventListener('click', fib7);
gcdbut.addEventListener('click', gcd32_24);
rsbut.addEventListener('click', randstud);
