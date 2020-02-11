
function getDate(){
var date = new Date();
var date1 = date.toLocaleString();
var div1 = document.getElementById("times");
div1.innerHTML = date1;
 }
setInterval("getDate()",1000);
