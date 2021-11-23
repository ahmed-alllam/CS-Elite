const nextButton = document.getElementById('next');
const previousButton = document.getElementById('previous');

const list = document.getElementById('categories-list');

nextButton.onclick = function () {
    list.scrollLeft = list.scrollWidth - list.offsetWidth;

    nextButton.style.visibility = "hidden";
    previousButton.style.visibility = "visible";
};

previousButton.onclick = function () {
    list.scrollLeft = 0;

    previousButton.style.visibility = "hidden";
    nextButton.style.visibility = "visible";   
};

list.onscroll = () => {
    if ((list.scrollLeft + list.offsetWidth) >= list.scrollWidth){
        nextButton.style.visibility = "hidden";
        previousButton.style.visibility = "visible";
    } else if (list.scrollLeft <= 0) {
        previousButton.style.visibility = "hidden";
        nextButton.style.visibility = "visible";
    } else {
        previousButton.style.visibility = "visible";
        nextButton.style.visibility = "visible";
    }
}
