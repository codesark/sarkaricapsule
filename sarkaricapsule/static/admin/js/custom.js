
document.onreadystatechange = function(){

  console.log("Loaded!");
  
  window.onkeydown = function(event) {
      if (event.keyCode == 13 && event.target.nodeName != "TEXTAREA") {
          event.preventDefault();
          return false;
      }
  }
}