let addItem = document.getElementById('add_item');

addItem.addEventListener('click', () =>{
    let item = document.createElement('li');
        item.textContent = 'Item';

    let myList = document.querySelector('.my_list');
        myList.appendChild(item);
});
