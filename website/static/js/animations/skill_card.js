// alert('here')
let skill_cards_ctnr = document.querySelector('#skills_ctnr')
let skill_cards = document.querySelectorAll('.skill_card')


const skill_card_tl = gsap.timeline({
    paused: true,
})


skill_card_tl.to(
    skill_cards,
    {
        // delay: .25,
        duration: 2,
        left: '0em',
        right: '0em',
        ease: Sine.easeInOut,
    }
), 0


const skill_card_observer_options = {
    root: null,
    threshold: .1,
}

const skill_card_observer = new IntersectionObserver(function(entries, skill_card_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            skill_card_tl.play()
            // alert('here')
        } else {
            skill_card_tl.reverse()
            // alert('not here')
        }
    })
}, skill_card_observer_options)


skill_card_observer.observe(skill_cards_ctnr)


// for (let card of skill_cards){
//     skill_card_observer.observe(card)
// }

