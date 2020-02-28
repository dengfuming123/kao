function name(){
 var pic = document.getElementById('head');
 var member = document.getElementById('appear');

 pic.onmouseover = function(){
 member.style.display = 'block';
 }
 pic.onmouseout = function(){
 member.style.display = 'none';
 }
}();