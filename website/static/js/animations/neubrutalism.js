let neu_section = document.querySelector('#neubrutalism_section')
let dec_sqr = neu_section.querySelector('.decorative_sqr')
let neu_cards = neu_section.querySelectorAll('.neu_card')

let neu_section_tl = gsap.timeline({
    repeat: -1,
    yoyo: true,
})

neu_section_tl.to(
    dec_sqr,
    {
        // delay: 0,
        duration: 5,
        clipPath: 'polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%)',
        ease: Sine.easeInOut,
    }
), 0

neu_section_tl.to(
    dec_sqr,
    {
        // delay: 0,
        duration: 5,
        clipPath: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)',
        ease: Sine.easeInOut,
    }
), 1

neu_section_tl.to(
    dec_sqr,
    {
        // delay: 0,
        duration: 5,
        clipPath: 'polygon(20% 0%, 0% 20%, 30% 50%, 0% 80%, 20% 100%, 50% 70%, 80% 100%, 100% 80%, 70% 50%, 100% 20%, 80% 0%, 50% 30%)',
        ease: Sine.easeInOut,
    }
), 2

neu_section_tl.to(
    dec_sqr,
    {
        // delay: 0,
        duration: 5,
        clipPath: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        ease: Sine.easeInOut,
    }
), 3


let neu_section_tl2 = gsap.timeline({
})

neu_section_tl2.to(
    neu_cards,
    {
        duration: 5,
        ease: Sine.easeInOut,
        left: 0,
        right: 0,        
    }
)


console.log(neu_cards)