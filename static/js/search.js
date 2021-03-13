$(document).ready(function() {
    document.querySelectorAll('.myBtn').forEach(item =>{
        var title = item.parentElement.parentElement.firstElementChild.firstElementChild
        var author = item.parentElement.parentElement.firstElementChild.firstElementChild.nextElementSibling
        var image = item.parentElement.parentElement.parentElement.firstElementChild.firstElementChild.src
        console.log('image:',image)
        item.addEventListener('click', () => {
            document.getElementById('input-image').value = image
            document.getElementById('modal-image').src = image
            document.getElementById('input-title').value = title.innerText
            document.getElementById('input-authors').value = author.innerText
            document.querySelector('.bg-modal').style.display = 'flex';
            })
        });

     document.querySelectorAll(".close").forEach(item => {
        item.addEventListener('click', () => {
            document.querySelector('.bg-modal').style.display = 'none';
            })
        },
    )
})