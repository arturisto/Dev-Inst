function showBanner(){

    let elem = document.getElementById("banner");
    elem.style.marginTop="0px";
    elem.style.transition="margin-top 0.5s linear";

    let cancelInterval = setInterval(banner,1000);
    setTimeout(hideBanner,10000,elem,cancelInterval);

}

function hideBanner(div,c){

  div.style.marginTop="-300px";
  div.style.transition="margin-top 0.5s linear";
   clearInterval(c)

}
function banner(){
  let seconds = document.getElementById("text").textContent;
  seconds--;
  document.getElementById("text").textContent= seconds;

}
