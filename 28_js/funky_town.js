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

var students=['a','b','c','d','e','f','g'];

var randomStudent=function(){
    var num=Math.floor(Math.random() * students.length)
    return students[num];
};
