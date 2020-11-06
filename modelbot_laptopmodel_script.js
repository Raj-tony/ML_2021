function myFunction1(){
  var x = document.getElementById("fname");
  document.getElementById("GET_MODEL").onclick =models; 


var  choose_models = [ ["4GB SSD VARIANT","1. Dell Inspiron 15 3000 Series"], ["4GB HDD VARIANT", "1. Lenovo Ideapad L340."], ["8GB SSD VARIANT", "1.  Acer nitro 5."], ["8GB HDD VARIANT", "1. Acer Aspire 7."] ]


  function models(){
    var text = "";
    for (var i=0; i<choose_models[0].length;i++){
      text+=choose_models[x.value - 1][i]+ "<br>"+"<br>";

    } 
     document.getElementById("content").innerHTML =text ;
    
  }
 
}
