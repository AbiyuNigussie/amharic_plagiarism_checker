const fileDropArea = document.getElementById("fileDropArea");
const fileList = document.getElementById("fileList");
const fileForm = document.getElementById("fileForm");
const fileInput = document.createElement("input");
fileInput.type = "file";
fileInput.multiple = true;
fileInput.style.display = "none";

document.body.appendChild(fileInput);

const hiddenFileInput = document.createElement("input");
hiddenFileInput.type = "file";
hiddenFileInput.name = "files[]";
hiddenFileInput.multiple = true;
hiddenFileInput.style.display = "none";

fileForm.appendChild(hiddenFileInput);

let selectedFiles = [];

fileDropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  fileDropArea.classList.add("dragging");
});

fileDropArea.addEventListener("dragleave", () => {
  fileDropArea.classList.remove("dragging");
});

fileDropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  fileDropArea.classList.remove("dragging");
  const files = Array.from(e.dataTransfer.files);
  addFilesToList(files);
});

fileDropArea.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", (e) => {
  const files = Array.from(e.target.files);
  addFilesToList(files);
});

function addFilesToList(files) {
  selectedFiles = [...selectedFiles, ...files];
  updateFileList();
  updateHiddenInput();
}

function updateFileList() {
  fileList.innerHTML = "";
  if (selectedFiles.length > 0) {
    selectedFiles.forEach((file, index) => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span class="file-name">${file.name}</span>
        <button class="delete-btn" data-index="${index}">❌</button>
      `;
      fileList.appendChild(li);

      li.querySelector(".delete-btn").addEventListener("click", () => {
        selectedFiles.splice(index, 1);
        updateFileList();
        updateHiddenInput();
      });
    });
  } else {
    fileList.innerHTML = '<li class="placeholder">No files selected yet.</li>';
  }
}

function updateHiddenInput() {
  hiddenFileInput.value = "";
  selectedFiles.forEach((file) => {
    const fileData = new DataTransfer();
    fileData.items.add(file);
    hiddenFileInput.files = fileData.files;
  });
}

fileForm.addEventListener("submit", (e) => {
  if (selectedFiles.length < 2) {
    e.preventDefault();
    alert("Please attach at least two files before submitting.");
  }
});
