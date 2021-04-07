
$(document).ready(function() {
    document.querySelectorAll('.update-cart').forEach(item =>{
        item.addEventListener('click', () => {
            var url = item.dataset.url
            var productId = item.dataset.product
            var action = item.dataset.action
            if(user === 'AnonymousUser'){
                console.log('not logged in')
            }else{
                UpdateUserOrder(productId, action, url)
            }
        })
    })
})

function UpdateUserOrder(productId, action, url){
    console.log('user logged in')
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data', data)
    })
}
