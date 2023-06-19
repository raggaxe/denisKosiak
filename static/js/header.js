function showElement(elementId) {
  var element = document.getElementById(elementId);
  element.style.display = 'block';
  element.style.animationName = 'slideUp';
}

function hideElement(elementId) {
  var element = document.getElementById(elementId);
  element.style.animationName = 'slideDown';
  setTimeout(function() {
      element.style.display = 'none';
  }, 500);
}

function toggleElements() {
  var linkElement = document.getElementById('link');
  var logoElement = document.getElementById('logo');

  if (linkElement.style.display === 'none') {
      showElement('link');
      hideElement('logo');
  } else {
      hideElement('link');
      showElement('logo');
  }
}

setInterval(toggleElements, 5000); // Alternar a visibilidade a cada 3 minutos (180000 milissegundos)
