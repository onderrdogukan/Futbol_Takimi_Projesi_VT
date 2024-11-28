function togglePopup() {
    var popup = document.getElementById('popup');
    var overlay = document.getElementById('overlay');
    popup.style.display = popup.style.display === 'block' ? 'none' : 'block';
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
}

function togglePopup_update(id) {
    var popup = document.getElementById('popup_guncelle'+id);
    var overlay = document.getElementById('overlay');
    popup.style.display = popup.style.display === 'block' ? 'none' : 'block';
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
}
// Forma numarasını kontrol et
function validateForm() {
    var formaNo = document.getElementById('forma_no').value;
    if (formaNo > 99) {
       /* alert('Forma numarası 99\'dan büyük olamaz!'); */
        return false;
    }
    return true;
}