// alert('here')

let experience_section = document.querySelector('#experience_section')

if (experience_section){
    const count_wait = (ms) => new Promise(resolve => setTimeout(resolve, ms))
    
    const loop = async () => {
        let experience_divs = experience_section.querySelectorAll('.experience')
        for (let elem of experience_divs) {
            let max_count = elem.dataset.max_count
            let elem_number = elem.querySelector('h3')
            for (let i = 0; i < max_count; i++){
                elem_number.innerHTML = i;
                await count_wait(10)
            }
        }
    }
    
    const experience_observer_options = {
        root: null,
        threshold: .5,
    }
    
    const experience_section_observer = new IntersectionObserver(function(entries, experience_section_observer){
        entries.forEach(entry => {
            if (entry.isIntersecting){
                loop()
                // console.log(entry.target)
            } else {
                let experience_h3 = experience_section.querySelectorAll('.experience h3')
                for (let elem of experience_h3){
                    elem.innerHTML = 0
                }                
            }
        })
    }, experience_observer_options)
    
    experience_section_observer.observe(experience_section)



    const experience_canvas = experience_section.querySelector('#skills_chart')

    console.log(experience_canvas)    


}



// loop()



