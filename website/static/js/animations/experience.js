// alert('here')

let experience_section = document.querySelector('#experience_section')

const count_wait = (ms) => new Promise(resolve => setTimeout(resolve, ms))


if (experience_section){
    let experience_divs = experience_section.querySelectorAll('.experience')
    for (let elem of experience_divs){
        let max_count = elem.dataset.max_count
        let elem_number = elem.querySelector('h3')
        // console.log()
        for (let i = 0; i < max_count; i++){
            elem_number.innerHTML = i;
            await count_wait(2000)

            // setTimeout(function(){
            //     // sleep for a bit
            
            // }, 6000)
        }
    }

}


async function loop_experience(elems){
    
}


