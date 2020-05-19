let input = document.getElementById("text");

input.addEventListener('keyup',(e) =>{

    let key = e.keyCode;
    //console.log(key);
    if(key <65 || key>90){
      let input = document.getElementById("text");
      input.value=input.value.replace(e.key,"");
    }

  }

)
