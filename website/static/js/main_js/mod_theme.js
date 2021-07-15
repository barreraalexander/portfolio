// let theme_btn = document.querySelector('#theme_btn')
let theme_btn = document.querySelector('.light_switch_ctnr')
if (theme_btn){
    theme_btn.addEventListener('click', toggle_dark, false)
}

function toggle_dark(){
    let html_elem = document.querySelector('html')
    let hamburger = document.querySelector('#hamburger')
    // let alt_src = hamburger.dataset.alt_src

    if (html_elem.dataset.main_theme=="dark"){
        html_elem.dataset.main_theme = "light"

        // let holder = hamburger.src
        hamburger.src = hamburger.dataset.light_src
        // console.log(hamburger)
        // hamburger.dataset.alt_src = holder
        
        
    } else {
        html_elem.dataset.main_theme = "dark"
        
        // let holder = hamburger.src
        hamburger.src = hamburger.dataset.dark_src
        // hamburger.src = alt_src
        // console.log(hamburger)
        // hamburger.dataset.alt_src = holder
    }

}