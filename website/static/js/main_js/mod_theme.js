let theme_btn = document.querySelector('.light_switch_ctnr')
if (theme_btn){
    theme_btn.addEventListener('click', toggle_dark, false)
}

function toggle_dark(){
    let html_elem = document.querySelector('html')
    let hamburger = document.querySelector('#hamburger')

    if (html_elem.dataset.main_theme=="dark"){
        html_elem.dataset.main_theme = "light"

        hamburger.src = hamburger.dataset.light_src
                
    } else {
        html_elem.dataset.main_theme = "dark"
        
        hamburger.src = hamburger.dataset.dark_src

    }

}