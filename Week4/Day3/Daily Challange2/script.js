let planets=[
    {
      planet:"earth",
      moons:["moon"],
      background:"blue"
    },
    {
      planet:"mercury",
      moons:[],
      background:"grey"
    },
    {
      planet:"jupiter",
      moons:["europa", "io","Castillo"],
      background:"orange"
    }
]

for(x of planets){

  let elem = document.createElement('div');
  elem.classList.add('planet');
  elem.setAttribute("id",x.planet);
  elem.style.backgroundColor= x.background;
  for (y of x.moons){

    elem.appendChild(setMoon(y,x.moons.indexOf(y)))
  }
  document.body.appendChild(elem);
}

function setMoon(obj,y){

  let moon = document.createElement('div');
  moon.classList.add('moon');
  moon.setAttribute("style","background-color:grey");
  moon.setAttribute("id",obj);
  moon.style.right =40*y+"px";
  return moon;
}
