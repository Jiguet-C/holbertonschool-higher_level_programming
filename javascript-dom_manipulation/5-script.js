let update = document.getElementById('update_header');
let header = document.querySelector('header');

    update.addEventListener('click', () => {
        update = header.textContent = 'New Header!!!';
    });
