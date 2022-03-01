let crns=[22970,22904,22901,22910,25150];
let inputs = document.querySelectorAll("input[type=number]");
for (let i = 0; i < crns.length; i++) {
    inputs[i].value = crns[i];
    inputs[i].dispatchEvent(new Event('input'));
}
let form = document.querySelector('form');
form.dispatchEvent(new Event('submit'));
new Promise((resolve) => setTimeout(resolve, 100)).then(() => {
    let button = document.querySelector('.card-footer button.btn-success');
    button.dispatchEvent(new Event('click'));
})
