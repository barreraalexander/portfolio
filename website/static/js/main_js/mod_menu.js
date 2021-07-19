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
        window.addEventListener('click', check_target, true)
        
    } else if (menu_status=='open'){
        alert('here')
        hidden_menu.dataset.menu_status = 'closed'
        hidden_menu.classList.remove('apply_show_menu')
        hidden_menu.classList.add('apply_hide_menu')
        window.removeEventListener('click', check_target, true)
    }
}


function check_target(event){
    var hidden_menu = document.querySelector('#hidden_nav')
    // var menu_status = hidden_menu.dataset.menu_status

    if (event.target != hidden_menu &&
        event.target != nav_button &&
        event.target.parentNode != hidden_menu){

        console.log(hidden_menu)
        mod_menu()


    }
}