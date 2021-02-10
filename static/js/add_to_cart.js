
$(document).ready(function() {
    document.querySelectorAll('.update-cart').forEach(item =>{
        item.addEventListener('click', () => {
            var productId = item.dataset.product
            var action = item.dataset.action
            if(user === 'AnonymousUser'){
                console.log('not logged in')
            }else{
                UpdateUserOrder(productId, action)
            }
        })
    })
})

function UpdateUserOrder(productId, action){
    console.log('user logged in')

    var url = '/market/add_to_cart/'

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
