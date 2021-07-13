let nav_button = document.querySelector('.menu_flexi')
if (nav_button){
    nav_button.addEventListener('click', mod_menu, false)
}


function mod_menu(){
    var hidden_menu = document.querySelector('#hidden_nav')
    var menu_status = hidden_menu.dataset.menu_status

    if (menu_status=='closed'){
        hidden_menu.classList.remove('apply_hide_menu')
        hidden_menu.classList.add('apply_show_menu')
        hidden_menu.dataset.menu_status = 'open'
        window.addEventListener('click', check_target, false)

    } else if (menu_status=='open'){
        window.removeEventListener('click', check_target, false)
        menu_status = 'closed' 
    }
}


function check_target(event){
    if (event.target != hidden_menu &&
        event.target != nav_button &&
        event.target.parentNode != hidden_menu){

        hidden_menu.dataset.menu_status = 'closed'
        
        hidden_menu.classList.remove('apply_show_menu')
        hidden_menu.classList.add('apply_hide_menu')
        menu_status = 'closed'
        window.removeEventListener('click', check_target)

    }
}