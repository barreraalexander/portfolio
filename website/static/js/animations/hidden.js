let hidden_section = document.querySelector('#hidden_section')

let open_navigation = document.querySelector('#hamburger')
let close_navigation = document.querySelector('#close_hidden_menu')

let navigation_buttons = [open_navigation, close_navigation]

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
        zIndex: '3000',
    }
)

for (let menu_button of navigation_buttons){
    menu_button.addEventListener('click', mod_navigation, false)
    // console.log(menu_    button)
    // alert('here ')
}

function mod_navigation(event){
    // console.log(event.target.classList)
    if (event.target==open_navigation){
        // alert('here')
        hidden_navigation_tl.play()
    } else {
        hidden_navigation_tl.reverse()
        // alert('not here')
    }
}