let tech_ctnr = document.querySelector('.technologies_ctnr')
if (tech_ctnr){
    imgs = tech_ctnr.querySelectorAll('.tech_img_ctnr')
    for (let img of imgs){
        img.addEventListener('click', alter_tech_interface, false)    
        img.addEventListener('mouseover', alter_tech_interface, false)  
    }
}

let selected = "tech_img1";
let selected_elem = document.querySelector(`#${selected}`)
if (selected_elem){
    // alert('here')
    selected_elem.click()
}
function alter_tech_interface(){
    unselected = tech_ctnr.querySelector(`#${selected}`)
    unselected.classList.remove('selected_img')

    this.classList.add('selected_img')
    selected = this.id

    let caption = this.getAttribute('data-caption')
    let caption_elem = document.querySelector('#caption_text')
    caption_elem.innerText = caption
}