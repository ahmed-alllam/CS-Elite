const nextButton = document.getElementById('next');
const previousButton = document.getElementById('previous');

const list = document.getElementById('categories-list');

nextButton.onclick = function () {
    list.scrollLeft = list.scrollWidth - list.clientWidth;
};

previousButton.onclick = function () {
    list.scrollLeft = 0;
};
