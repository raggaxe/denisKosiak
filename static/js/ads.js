function showAd(adContainer) {
    adContainer.style.display = 'block';
    adContainer.style.animationName = 'slideUp';
    setTimeout(function() {
        hideAd(adContainer);
    }, 30000); // Exibir durante 30 segundos
}

function hideAd(adContainer) {
    adContainer.style.animationName = 'slideDown';
    setTimeout(function() {
        adContainer.style.display = 'none';
    }, 500);
    setTimeout(function() {
        showAd(adContainer);
    }, 180000); // Esperar 3 minutos antes de exibir novamente
}

var ads = document.querySelectorAll('.ads');
ads.forEach(function(adContainer) {
    hideAd(adContainer); // Começar oculto e esperar antes de exibir
});