// let theme_btn = document.querySelector('#theme_btn')
let theme_btn = document.querySelector('.light_switch_ctnr')
if (theme_btn){
    theme_btn.addEventListener('click', toggle_dark, false)
}

function toggle_dark(){
    let html_elem = document.querySelector('html')
    // let light_switch = html_elem.querySelector('.switch')

    if (html_elem.dataset.main_theme=="dark"){
        html_elem.dataset.main_theme = "light"
    } else {
        html_elem.dataset.main_theme = "dark"
    }

}