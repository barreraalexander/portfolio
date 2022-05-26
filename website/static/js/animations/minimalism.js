let minimalism_section = document.querySelector('#minimalism_section')
let slider = minimalism_section.querySelector('.slider_ctnr')
let slide = minimalism_section.querySelector('.slide')
let min_cards = minimalism_section.querySelectorAll('.min_card')
let min_cards_p = minimalism_section.querySelectorAll('.min_card p')
let min_cards_imgs = minimalism_section.querySelectorAll('.min_card img')


let minimalism_tl = gsap.timeline({
    paused: true,
})

minimalism_tl.to(
    slide,
    {
        duration: .25,
        ease: Sine.easeInOut,
        left: '90%',
        filter: 'invert(1)',
    }
), 0


minimalism_tl.to(
    min_cards_imgs,
    {
        duration: .25,
        ease: Sine.easeInOut,
        filter: 'invert(1)',
    }
), 0



minimalism_tl.to(
    min_cards,
    {
        duration: .25,
        backgroundColor: '#000',
        ease: Sine.easeInOut,
    }
), 0


minimalism_tl.to(
    min_cards_p,
    {
        duration: .25,
        color: '#fff',
        ease: Sine.easeInOut,
    }
), 0


var has_played = false
slider.addEventListener('click', function(){
    if (has_played){
        minimalism_tl.reverse()
        has_played = false
        return
    }
    minimalism_tl.play()
    has_played = true
})