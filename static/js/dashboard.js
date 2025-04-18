document.addEventListener("DOMContentLoaded", function() {
    let cards = document.querySelectorAll('.card');

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 200);
    });
});
