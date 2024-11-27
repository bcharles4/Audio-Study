document.addEventListener('DOMContentLoaded', function () {
  const tl = gsap.timeline();
  tl.from(".navbar", {
    y: -200,
    duration: .7,
    opacity: 0
  });
});



document.addEventListener('DOMContentLoaded', function () {
  const tl = gsap.timeline();

  tl.from(".logo", {
    x: -500,
    duration: 1,
    opacity: 0
  });

});


document.addEventListener('DOMContentLoaded', function () {
  const tl = gsap.timeline();
  tl.from("li", {
    y: -400,
    duration: 1,
    opacity: 0
  });


});


document.addEventListener('DOMContentLoaded', function() {
  const tl = gsap.timeline();
  tl.from (".head-con", {
      x: -2300 ,
      duration: 0.8,
      opacity: 0,
      
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const paragraphs = document.querySelectorAll("p");
  const readBtn = document.getElementById("readBtn");
  let currentParagraphIndex = 0;

  // Web Speech API setup for Text-to-Speech
  const synth = window.speechSynthesis;
  let utterance;

  readBtn.addEventListener("click", function () {
    if (synth.speaking) {
      // If already speaking, stop the current utterance
      synth.cancel();
      return;
    }

    currentParagraphIndex = 0;  // Reset to the first paragraph
    speakParagraph(paragraphs[currentParagraphIndex]);
  });

  function speakParagraph(paragraph) {
    // Create a new speech utterance
    utterance = new SpeechSynthesisUtterance(paragraph.textContent);

    // Highlight the current paragraph
    highlightParagraph(paragraph);

    // Event triggered when the utterance finishes speaking
    utterance.onend = function () {
      // Move to the next paragraph if available
      currentParagraphIndex++;
      if (currentParagraphIndex < paragraphs.length) {
        speakParagraph(paragraphs[currentParagraphIndex]);
      } else {
        clearHighlight();
      }
    };

    // Start speaking the paragraph
    synth.speak(utterance);
  }

  function highlightParagraph(paragraph) {
    // Clear any existing highlights
    clearHighlight();

    // Apply a highlight to the current paragraph
    paragraph.style.backgroundColor = "#ffff99";
  }

  function clearHighlight() {
    paragraphs.forEach(function (para) {
      para.style.backgroundColor = "";  // Reset background color
    });
  }
});










// document.getElementById('uploadForm').addEventListener('submit', async function (e) {
//     e.preventDefault();

//     const fileInput = document.getElementById('fileInput');
//     if (!fileInput.files.length) {
//         alert("Please select a file.");
//         return;
//     }

//     const formData = new FormData();
//     formData.append('file', fileInput.files[0]);

//     const response = await fetch('/convert', {
//         method: 'POST',
//         body: formData,
//     });

//     const data = await response.json();
//     if (response.ok) {
//         document.getElementById('result').style.display = 'block';
//         document.getElementById('downloadLink').href = `/download/${data.fileId}`;
//     } else {
//         alert(data.error);
//     }
// });


// document.getElementById('uploadForm').addEventListener('submit', function (e) {
//     e.preventDefault();

//     const fileInput = document.getElementById('fileInput');
//     const formData = new FormData();
//     formData.append('file', fileInput.files[0]);

//     fetch('/upload', {
//         method: 'POST',
//         body: formData,
//     })
//         .then(response => response.blob())
//         .then(blob => {
//             const url = window.URL.createObjectURL(blob);
//             const downloadLink = document.getElementById('downloadLink');
//             downloadLink.href = url;
//             document.getElementById('result').style.display = 'block';
//         })
//         .catch(error => {
//             console.error('Error during file upload:', error);
//         });
// });




// Trigger the file input when the "UPLOAD" button is clicked
document.getElementById('uploadBtn').addEventListener('click', function () {
  document.getElementById('fileInput').click();
});

// Display the file name when a file is selected
document.getElementById('fileInput').addEventListener('change', function () {
  const file = this.files[0];
  if (file) {
    document.getElementById('fileName').style.display = 'block';
    document.getElementById('fileDisplay').textContent = file.name;
  }
});

// Form submission handler with progress functionality
document.getElementById('uploadForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const fileInput = document.getElementById('fileInput');
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  // Show progress bar
  document.getElementById('progressContainer').style.display = 'block';

  // Custom fetch request using XMLHttpRequest to track progress
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/upload', true);

  // Update progress bar
  xhr.upload.addEventListener('progress', function (event) {
    if (event.lengthComputable) {
      const percentComplete = (event.loaded / event.total) * 100;
      document.getElementById('progressBar').value = percentComplete;
      document.getElementById('progressText').textContent = Math.round(percentComplete) + '%';
    }
  });

  xhr.onload = function () {
    if (xhr.status === 200) {
      // Use Fetch API to handle the blob response after the file is uploaded
      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
        .then(response => response.blob())
        .then(blob => {
          const url = window.URL.createObjectURL(blob);
          const downloadLink = document.getElementById('downloadLink');
          downloadLink.href = url;
          document.getElementById('result').style.display = 'block';
        })
        .catch(error => {
          console.error('Error during file upload:', error);
        });
    } else {
      alert('File upload failed.');
    }
  };

  xhr.send(formData);
});