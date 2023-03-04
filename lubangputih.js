const urlParams = new URLSearchParams(window.location.search);
const file = urlParams.get('file');
document.getElementById('file').innerText = file;