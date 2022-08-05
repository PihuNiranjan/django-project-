var numKeys = [];
var opns = [];
var res = document.querySelector("#resultArea");
var clrBtn = document.querySelector("#clrTxt");
var delBtn = document.querySelector("#del");
var eqBtn = document.querySelector("#eq");
var decPoint = document.querySelector("#decp");
var opnSyms = ["+", "-", "*", "/"];

// for taking input numbers
for(var i=0;i<=9;i++){
	(function(i){
    	qs = "#num" + i;
		numKeys.push(document.querySelector(qs));
		numKeys[i].addEventListener("click", function(){
			res.textContent += i;
		});
  	}(i));
}

// for taking operator symbol 
for(var i=0;i<=3;i++){
	(function(i){
    	qs = "#op" + i;
		opns.push(document.querySelector(qs));
		opns[i].addEventListener("click", function(){
			res.textContent += opnSyms[i];
		});
  	}(i));
}

// for clear text-Area or clear screen

clrBtn.addEventListener("click", function(){
	res.textContent = "";
});

// for delete input 
delBtn.addEventListener("click", function(){
    res.textContent = res.textContent.substring(0, res.textContent.length - 1);
});

// for decimal point 
decPoint.addEventListener("click", function(){
	res.textContent += ".";
});

//  for anoymous input or invalid input 
eqBtn.addEventListener("click", function(){
	try{
		res.textContent = eval(res.textContent);
	}
	catch(e){
		res.textContent = "Invalid Syntax";
	}
});
