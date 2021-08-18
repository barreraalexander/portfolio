let open_modal_elems = document.querySelectorAll('.open_modal')
let modal_section = document.querySelector('#contact_modal_section')
let modal = document.querySelector('.modal_ctnr')
let close_modal = document.querySelector('#cancel_ctnr')

if (open_modal_elems){
    for (let elem of open_modal_elems){
        elem.addEventListener('click', mod_modal, false)
    }
    close_modal.addEventListener('click', mod_modal, false)
}

function mod_modal(){
    if (this.id == close_modal.id){
        modal_section.dataset.status = 'closed' 
        modal_section.removeEventListener('click', listen_clickaway)
        return
    }
    modal_section.dataset.status = 'open'
    modal_section.addEventListener('click', listen_clickaway, false)
}


function listen_clickaway(event){
    if (event.target.parentNode == modal_section ||
        event.target == modal_section
        ){
        close_modal.click()
        modal_section.removeEventListener('click', listen_clickaway)
    }    
}