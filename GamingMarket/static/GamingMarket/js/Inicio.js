const btnCart = document.querySelector('.container-cart-icon')
const containerCartProducts = document.querySelector('.container-cart-products')

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart')
})


$(window).scroll(function() {
  checkVisibility('#nuevos-juegos-section');
  checkVisibility('#ofertas-section');
});

function checkVisibility(elementId) {
  var scrollTop = $(window).scrollTop();
  var windowHeight = $(window).height();
  var elementOffset = $(elementId).offset().top;
  var activatePosition = elementOffset - (windowHeight * 0.9);

  if (scrollTop >= activatePosition) {
    $(elementId).addClass('active');
  }
}









