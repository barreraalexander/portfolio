// let neu_section = document.querySelector('#neubrutalism_section')
// let dec_sqr = neu_section.querySelector('.decorative_sqr')
// let neu_cards = neu_section.querySelectorAll('.neu_card')
// let left_arrow = neu_section.querySelector('.circle_decoration1')
// let right_arrow = neu_section.querySelector('.circle_decoration2')


// let neu_section_tl = gsap.timeline({
//     repeat: -1,
//     yoyo: true,
// })

// neu_section_tl.to(
//     dec_sqr,
//     {
//         duration: 5,
//         clipPath: 'polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%)',
//         ease: Sine.easeInOut,
//     }
// ), 0

// neu_section_tl.to(
//     dec_sqr,
//     {
//         duration: 5,
//         clipPath: 'polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)',
//         ease: Sine.easeInOut,
//     }
// ), 1



// let neu_section_tl2 = gsap.timeline({
//     paused: true,
// })

// neu_section_tl2.to(
//     neu_cards,
//     {
//         duration: 2,
//         ease: Sine.easeInOut,
//         left: 0,
//         right: 0,        
//     }
// ), 0

// neu_section_tl2.to(
//     left_arrow,
//     {
//         duration: 1,
//         ease: Sine.easeInOut,
//         clipPath: 'polygon(75% 0%, 100% 50%, 75% 100%, 0% 100%, 25% 50%, 0% 0%)',
//     }
// ), 1

// neu_section_tl2.to(
//     right_arrow,
//     {
//         duration: 1,
//         ease: Sine.easeInOut,
//         clipPath: 'polygon(100% 0%, 75% 50%, 100% 100%, 25% 100%, 0% 50%, 25% 0%)',
//     }
// ), 1




// const neu_observer_options = {
//     root: null,
//     threshhold: .7,
// }


// const neu_observer = new IntersectionObserver(function(entries, neu_observer){
//     entries.forEach(entry => {
//         if (entry.isIntersecting){
//             neu_section_tl2.play()
//         } else {
//             neu_section_tl2.reverse()
            
//         }
//     })
// }, neu_observer_options)

// neu_observer.observe(neu_section)