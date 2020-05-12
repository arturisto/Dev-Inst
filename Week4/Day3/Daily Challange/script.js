let books =[
  {
    title:"Harry Potter",
    author:"JKR",
    cover_image:"https://prodimage.images-bn.com/pimages/9780439358071_p0_v4_s1200x630.jpg",
    has_read:true
  },
  {
    title:"Name of the Rose",
    author:"Umberto Eco",
    cover_image:"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1415375471l/119073.jpg",
    has_read:false
  }
]
let elem = document.createElement('div');
document.body.appendChild(elem);
elem = document.createElement('ul');
document.body.getElementsByTagName('div')[0].appendChild(elem);

for(x of books){
  console.log(x);
    elem = document.createElement('tr');
    var text = document.createTextNode(x.title+" written by "+x.author);
    if (x.has_read){
      elem.setAttribute("style","color:red");
    }
    elem.appendChild(text);
    document.body.getElementsByTagName('ul')[0].appendChild(elem)

    var img = document.createElement("img");
    img.setAttribute("src",x.cover_image);
    img.setAttribute("style","width:100px; height:100px;");
    document.body.getElementsByTagName('ul')[0].appendChild(img)
}
