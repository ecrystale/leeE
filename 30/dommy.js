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

var headingchange=function(word){
    var head=document.getElementById("h");
    head.innerHTML=word;
}


var list = document.getElementsByTagName("li");
for(var i=0;i<list.length;i++){
    list[i].addEventListener('mouseover',function(e){console.log(e);headingchange(list[i]);});
}


