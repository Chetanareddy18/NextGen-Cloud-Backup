document.addEventListener("DOMContentLoaded", () => {
  const uploadForm = document.getElementById("uploadForm");
  const uploadBtn = document.querySelector(".upload-btn");

  if (uploadForm) {
    uploadForm.addEventListener("submit", () => {
      uploadBtn.disabled = true;
      uploadBtn.innerText = "Uploading...";
      uploadBtn.style.background = "#94a3b8";
    });
  }
});
