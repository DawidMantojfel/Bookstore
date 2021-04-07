
$(document).ready(function() {
    document.querySelectorAll('.myBtn').forEach(item =>{
        item.addEventListener('click', () => {
            var author = item.dataset.author
            var title = item.dataset.title
            var description = item.dataset.description
            var image = item.dataset.image
            var infolink = item.dataset.infolink

            document.getElementById('modal-image').src = image
            document.getElementById('input-title').value = title
            document.getElementById('input-authors').value = author
            var sell_submit = document.getElementById('sell_button')
            sell_submit.value = JSON.stringify({
                'description':description,
                'image':image,
                'infolink':infolink
            })
            document.querySelector('.bg-modal').style.display = 'flex';

        });
    document.querySelectorAll(".close").forEach(item => {
        item.addEventListener('click', () => {
            document.querySelector('.bg-modal').style.display = 'none';
            })
        }
    )}
    )
});




// function sell(){
//     var button = document.getElementById('book_id')
//     var book_id = button.dataset.product
//     var action = button.dataset.action
//     var url = '/market/search/'
//     fetch(url, {
//         method: 'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body:JSON.stringify({'book_id':book_id,'action':action})
//         })
//         .then((response)=>{
//             return response.json()
//         })
//         .then((data) =>{
//             console.log('data', data)
//         })
//     }
