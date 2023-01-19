const form = document.querySelector('.form')

form.addEventListener('submit',(e)=>e.preventDefault())

const nav = document.querySelector('.header')
window.addEventListener('scroll',fixNav)

function fixNav() {
    if(window.scrollY > nav.offsetHeight + 150) {
        nav.classList.add('active')
    }else {
        nav.classList.remove('active')
    }
}




const aleert = document.querySelector('.aleert')
const aleert_btn = document.querySelector('.aleert-btn')
aleert_btn.addEventListener('click',()=>aleert.remove())
setTimeout(()=>{
   aleert.remove()
},3000)

