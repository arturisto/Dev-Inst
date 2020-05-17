let libButton = document.getElementById('lib-button');
let libIt = function() {
      let noun = document.forms[0].elements[0].value;
      let adjective= document.forms[0].elements[1].value;
      let someonesName = document.forms[0].elements[2].value;





    let storyDiv = document.getElementById("story");
    let str =  "Why do the say "+someonesName+"'s name in vain? </br> There is nothing like "+ noun+", it is so "+adjective;
    storyDiv.innerHTML =str;
};
libButton.addEventListener('click', libIt);
