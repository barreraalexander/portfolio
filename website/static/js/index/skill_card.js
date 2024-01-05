const skill_card_tl = gsap.timeline({
    paused: true,
})


skill_card_tl.to(
    $('.skill_card'),
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
        } else {
            skill_card_tl.reverse()
        }
    })
}, skill_card_observer_options)

skill_card_observer.observe($('#skills_ctnr')[0])