function previewImage() {
    const file = document.getElementById("imageUpload").files[0];
    const previewContainer = document.getElementById("imagePreview");
    const previewImage = previewContainer.querySelector(".image-preview__image");
    const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");

    const reader = new FileReader();

    reader.addEventListener("load", function () {
        previewImage.setAttribute("src", reader.result);
        previewImage.style.display = "block";
        previewDefaultText.style.display = "none";
    });

    if (file) {
        reader.readAsDataURL(file);
    } else {
        previewImage.style.display = "none";
        previewDefaultText.style.display = "block";
    }
}  