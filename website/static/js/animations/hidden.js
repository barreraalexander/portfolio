let hidden_section = document.querySelector('#hidden_section')
let open_menu_buttons = document.querySelectorAll('.open_menu')
let close_menu_buttons = document.querySelectorAll('.close_menu')

let menu_buttons = [...open_menu_buttons, ...close_menu_buttons]

let hidden_menu_tl = gsap.timeline({
    paused: true,
})


hidden_menu_tl.to(
    hidden_section,
    {
        duration: .25,
        opacity: 1,
        filter: 'blur(0px)',
        display: 'flex',
        ease: Sine.easeInOut,
    }
)


for (let menu_button of menu_buttons){
    menu_button.addEventListener('click', mod_hidden, false)
}

function mod_hidden(event){
    if (event.target.classList.contains('open_menu')){
        hidden_menu_tl.play()
    } else {
        hidden_menu_tl.reverse()
        
    }
}