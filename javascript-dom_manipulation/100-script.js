document.addEventListener('DOMContentLoaded', () => {
  const myList = document.querySelector('.my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItem.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearList.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
