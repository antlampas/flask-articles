const quill = new Quill('#editor',{theme:'snow',modules:'#toolbar'});
const c = document.getElementById('content').value;
quill.setText(c);
document.getElementById('content').value = '';
