let hidden_section = document.querySelector('#hidden_section')

let open_navigation_buttons = document.querySelectorAll('.open_navigation_menu')
let close_navigation_buttons = document.querySelectorAll('.close_navigation_menu')

let navigation_buttons = [...open_navigation_buttons, ...close_navigation_buttons]

let hidden_navigation_tl = gsap.timeline({
    paused: true,
})


hidden_navigation_tl.to(
    hidden_section,
    {
        duration: .25,
        opacity: 1,
        filter: 'blur(0px)',
        display: 'flex',
        ease: Sine.easeInOut,
    }
)

for (let menu_button of navigation_buttons){
    menu_button.addEventListener('click', mod_navigation, false)
    // alert('here ')
}

function mod_navigation(event){
    if (event.target.classList.contains('.open_navigation_menu')){
        alert('here')
        // hidden_navigation_tl.play()
    } else {
        // hidden_navigation_tl.reverse()
        
    }
}