$(document).ready(function() {
    document.querySelectorAll('.myBtn').forEach(item =>{
        item.addEventListener('click', () => {
            document.querySelector('.bg-modal').style.display = 'flex';
            var button_row = item.parentElement
            button_row.childNodes.forEach(child =>{
                if (child.className === 'title-of-book'){
                    document.getElementById('input-title').value = child.innerText
                }
                if (child.className === 'authors-of-book') {
                    document.getElementById('input-authors').value = child.innerText
                }
                if (child.className === 'img-fluid-right') {
                    document.getElementById('modal-image').src = child.src
                    document.getElementById('input-image').value = child.src
                }
            });
            })
        });
    document.querySelector(".close").addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display = 'none';
        });
    });