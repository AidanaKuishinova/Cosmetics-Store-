const burger = document.querySelector(".burger");
const navBar = document.querySelector(".navbar");

burger.addEventListener("click", () => {
    burger.classList.toggle("active");
    navBar.classList.toggle("active");
})

document.querySelectorAll(".nav-item").forEach(n => n.addEventListener("click", () => {
    burger.classList.remove("active");
    navBar.classList.remove("active")
}))


const btn = document.querySelector(".fltrbtn");
const fltr = document.querySelector(".filter");

burger.addEventListener("click", () => {
    btn.classList.toggle("active");
    fltr.classList.toggle("active");
})

document.querySelectorAll(".filter").forEach(n => n.addEventListener("click", () => {
    btn.classList.remove("active");
    fltr.classList.remove("active")
}))