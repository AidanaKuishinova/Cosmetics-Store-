

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
      if(+nav.children[i].getAttribute('data-price') < min_value_of_price && +nav.children[i].getAttribute('data-price') < max_value_of_price){
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




