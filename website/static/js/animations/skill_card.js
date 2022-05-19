// alert('here')
let skill_cards_ctnr = document.querySelector('#skills_ctnr')
let skill_cards = skill_cards_ctnr.querySelectorAll('.skill_card')
let rocket = skill_cards_ctnr.querySelector('.skills_bg')

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

// skill_card_tl.to(
//     rocket,
//     {
//         duration: 5,
//         rotation: '120deg',
//         // y: '100vh',
//         ease: Sine.easeInOut,
//     }
// ), 1

// skill_card_tl.to(
//     rocket,
//     {
//         duration: 30,
//         // rotation: '90deg',
//         y: '130vh',
//         ease: Sine.easeInOut,
//     }
// ), 1


// skill_card_tl.to(
//     rocket,
//     {
//         duration: 8,
//         rotation: '180deg',
//         y: '20em',
//         x: '0vw',
//         ease: Sine.easeInOut,
//     }
// ), 2


// skill_card_tl.to(
//     rocket,
//     {
//         duration: 8,
//         rotation: '180deg',
//         y: '20em',
//         x: '80vw',
//         ease: Sine.easeInOut,
//     }
// ), 2


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

