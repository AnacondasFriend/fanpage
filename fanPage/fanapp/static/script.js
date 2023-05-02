let replys = document.querySelectorAll(".reply");
const allAdverisments = document.querySelector('.allAdvertisments')


for (reply of replys) {
    reply.addEventListener('click', (e)=>{
        adv_i = e.target
        adv_i.parentNode.insertAdjacentHTML("beforeend", `<input type='text' name='text' placeholder='...' /> <button class='sendform'>Отправить</button>`);
        adv_i.parentNode.removeChild(adv_i);
        
    })
};

