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
        document.documentElement.style.setProperty('--theme_accent', '#e6e6e6');
    } else {
        html_elem.dataset.main_theme = "dark"        
        hamburger.src = hamburger.dataset.dark_src
        document.documentElement.style.setProperty('--theme_accent', '#111');

    }
}


let color_divs = document.querySelectorAll('.color_div')

for (let elem of color_divs){
    elem.addEventListener('click', mod_light_theme, false)
}

function mod_light_theme(){
    let color = this.dataset.bg_color
    document.documentElement.style.setProperty('--theme_accent', color);
}

