$(document).ready(function() {
    var total = 0
    var subtotalSum = document.getElementsByClassName('subtotal')
    for (let i = 0 ; i < subtotalSum.length; i++){
        let subtotal = parseFloat(subtotalSum[i].innerHTML.replace('$',''))
        total += subtotal
    }
    document.getElementById('total').innerText ='$ '+ total
    var QuantityButtons = document.getElementsByName('quantity')
    for (let i = 0; i < QuantityButtons.length; i++) {
        var button = QuantityButtons[i]
        button.addEventListener('change', function(){
            quantityChanged(i)
            totalSumChanged()
        })
    }
})
function totalSumChanged(){
    var total = 0
    var subtotalSum = document.getElementsByClassName('subtotal')
    for (let i = 0 ; i < subtotalSum.length; i++){
        let subtotal = parseFloat(subtotalSum[i].innerHTML.replace('$',''))
        total += subtotal
    }
    document.getElementById('total').innerText = '$ ' + total
}

function quantityChanged(i){
    var input = event.target
    console.log('quantity: ',input.value)
    console.log('max value',input.max)
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    if (input.value >= input.max){
        input.value = input.max
    }
    var input_value = input.value
    updateSubtotal(input_value, i)
}
function updateSubtotal(quantity, i){
    var num = 0
    var productPrice = document.getElementsByClassName('product-price')[i].value
    var subtotal = (num + (productPrice * quantity)).toFixed(1)
    document.getElementsByClassName('subtotal')[i].innerHTML = '$' + subtotal
}