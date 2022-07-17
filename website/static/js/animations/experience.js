// alert('here')

let experience_section = document.querySelector('#experience_section')

if (experience_section){
    let experience_divs = experience_section.querySelectorAll('.experience')
    for (let elem of experience_divs){
        let max_count = elem.dataset.max_count
        let elem_number = elem.querySelector('h3')
        // console.log()
        for (let i = 0; i < max_count; i++){
            setTimeout(function(){
                elem_number.innerHTML = i;
                // sleep for a bit
            }, 6000)
        }
    }

}