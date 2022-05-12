let search = document.querySelector('.search_box')
document.querySelector('#search-icon').onclick = () =>{
	search.classList.toggle('active')
}

const myslide = document.querySelectorAll('.myslide'),
	  dot = document.querySelectorAll('.dot');


function sorting_type(){
    var e = document.getElementById("sort_type");
    var sort_type = e.value;
    if (sort_type == "high"){
        descSort()
    }
    else if(sort_type=="low"){
        sort()
    }
    else if (sort_type == "asc"){
    sortAtoZ()
    }
    sort_by_range()
    brands()
    country()
}
function brands() {
    let nav = document.querySelector('#gallery')
    var values = $('#brands_select').val();
    if (values != null){
     for(let i = 0; i < nav.children.length; i++){
     var isInBrand=false;
        for(let j = 0; j < values.length; j++){
            if(values[j].trim()==nav.children[i].getAttribute('data-brand').trim()){
                isInBrand=true
                break
            }
        }
        if(isInBrand==false){
        nav.children[i].style.display = "none"
        }

     }
    }

}
function country() {
    var values = $('#countries_select').val();
    let nav = document.querySelector('#gallery')
     for(let i = 0; i < nav.children.length; i++){
     var isInBrand=false;
        for(let j = 0; j < values.length; j++){
            if(values[j].trim()==nav.children[i].getAttribute('data-country').trim()){
                isInBrand=true
                break
            }
        }
        if(isInBrand==false){
        nav.children[i].style.display = "none"
        }

     }
}


function sort_by_range(){
     var min_value_of_price = +document.getElementById('min_value_of_price').value
     var max_value_of_price = +document.getElementById('max_value_of_price').value
    console.log(min_value_of_price,max_value_of_price)
    console.log(min_value_of_price+max_value_of_price)

let nav = document.querySelector('#gallery')
  for(let i = 0; i < nav.children.length; i++){
            nav.children[i].style.display = "flex"

}
  for(let i = 0; i < nav.children.length; i++){
      if(+nav.children[i].getAttribute('data-price') < min_value_of_price || +nav.children[i].getAttribute('data-price') > max_value_of_price){
//        replacedNode = nav.removeChild(nav.children[i])

        console.log(+nav.children[i].getAttribute('data-price'))
        nav.children[i].style.display = "none"

//        insertAfter(replacedNode, nav.children[i]);
      }}

}


function sort(){

  let nav = document.querySelector('#gallery')
  for(let i = 0; i < nav.children.length; i++){
    for (let j = i; j < nav.children.length; j++){
      if(+nav.children[i].getAttribute('data-price') > +nav.children[j].getAttribute('data-price') ){
        replacedNode = nav.replaceChild(nav.children[j], nav.children[i])
        insertAfter(replacedNode, nav.children[i]);
      }
    }
  }
}

function descSort(){
  let nav = document.querySelector('#gallery')
  for(let i = 0; i < nav.children.length; i++){
    for (let j = i; j < nav.children.length; j++){
      if(+nav.children[i].getAttribute('data-price') < +nav.children[j].getAttribute('data-price')){
        replacedNode = nav.replaceChild(nav.children[j], nav.children[i])
        insertAfter(replacedNode, nav.children[i]);
      }
    }
  }
}

function sortAtoZ(){
  let nav = document.querySelector('#gallery')
  for(let i = 0; i < nav.children.length; i++){
    for (let j = i; j < nav.children.length; j++){
      if(nav.children[i].getAttribute('data-title') > nav.children[j].getAttribute('data-title')){
        replacedNode = nav.replaceChild(nav.children[j], nav.children[i])
        insertAfter(replacedNode, nav.children[i]);
      }
    }
  }
}

function sortZtoA(){
  let nav = document.querySelector('#gallery')
  for(let i = 0; i < nav.children.length; i++){
    for (let j = i; j < nav.children.length; j++){
      if(nav.children[i].getAttribute('data-title') < nav.children[j].getAttribute('data-title')){
        replacedNode = nav.replaceChild(nav.children[j], nav.children[i])
        insertAfter(replacedNode, nav.children[i]);
      }
    }
  }
}

function insertAfter(elem, refElem){
  return refElem.parentNode.insertBefore(elem, refElem.nextSibling);
}
console.log("hello")

let counter = 1;
slidefun(counter);



let timer = setInterval(autoSlide, 8000);
function autoSlide() {
	counter += 1;
	slidefun(counter);
}
function plusSlides(n) {
	counter += n;
	slidefun(counter);
	resetTimer();
}
function currentSlide(n) {
	counter = n;
	slidefun(counter);
	resetTimer();
}
function resetTimer() {
	clearInterval(timer);
	timer = setInterval(autoSlide, 8000);
}

function slidefun(n) {

	let i;
	for(i = 0;i<myslide.length;i++){
		myslide[i].style.display = "none";
	}
	for(i = 0;i<dot.length;i++) {
		dot[i].className = dot[i].className.replace(' active', '');
	}
	if(n > myslide.length){
	   counter = 1;
	   }
	if(n < 1){
	   counter = myslide.length;
	   }
	myslide[counter - 1].style.display = "block";
	dot[counter - 1].className += " active";
}

var header=document.getElementById("header")

window.addEventListener("scroll", (event) => {
    let scroll = this.scrollY;
    console.log(header)
    if (scroll>650) { header.style.background=" -webkit-linear-gradient(right, #F9D1D9, #A0B9CE)"}
    else {header.style.background="transparent"}
});


