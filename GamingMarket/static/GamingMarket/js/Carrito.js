const cartInfo = document.querySelector('.container-cart-product');
const rowProduct = document.querySelector('.row-product');
const productList = document.querySelector('.container-items');
let allProducts = [];
const valorTotal = document.querySelector('.cart-total .total-a-pagar');
const countProducts = document.querySelector('#contador-productos');
const containerItems = document.querySelector('.container-items');




containerItems.addEventListener('click', e => {
  if (e.target.classList.contains('btn-add-cart')) {
    const product = e.target.parentElement;
    console.log(product);

    const infoProduct = {
      quantity: 1,
      title: product.querySelector('h5').textContent,
      price: product.querySelector('p.precio').textContent,
    };
    console.log(infoProduct);

    const exist = allProducts.some(product => product.title === infoProduct.title);
    if (exist) {
      const products = allProducts.map(product => {
        if (product.title === infoProduct.title) {
          product.quantity++;
          return product;
        } else {
          return product;
        }
      });
      allProducts = [...products];
    } else {
      allProducts = [...allProducts, infoProduct];
    }

    showHTML();
    saveProductsToCookie();
  }
});

rowProduct.addEventListener('click', e => {
  if (e.target.classList.contains('icon-close')) {
    const product = e.target.parentElement;
    const title = product.querySelector('p').textContent;
    allProducts = allProducts.filter(product => product.title !== title);
    console.log(allProducts);
    showHTML();
    saveProductsToCookie();
  }
});

const showHTML = () => {
  rowProduct.innerHTML = '';
  let total = 0;
  let totalOfProducts = 0;

  allProducts.forEach(product => {
    const containerProduct = document.createElement('div');
    containerProduct.classList.add('cart-product');

    containerProduct.innerHTML = `
      <div class="info-cart-products">
        <span class="cantidad-producto-carrito">Cantidad: ${product.quantity}</span>
        <p class="titulo-producto-carrito">${product.title}</p>
        <span class="carrito-producto-precio">${product.price}</span>
      </div>
      
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="icon-close">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
    `;
    rowProduct.append(containerProduct);

    total += parseFloat(product.quantity) * parseFloat(product.price.slice(9));
    totalOfProducts += product.quantity;
  });
  if (totalOfProducts === 0) {
    rowProduct.innerHTML = `
      <div class="cart-product">
        <h4 class="empty-cart text-center font-weight-bolder">No hay productos en el carrito</h4>
      </div>
    `;

  } 
    valorTotal.innerText = `$${total.toFixed(3)}`;
    countProducts.innerText = totalOfProducts;
  
  
};

const saveProductsToCookie = () => {
  const expirationDate = new Date();
  expirationDate.setFullYear(expirationDate.getFullYear() + 1); // Cookie expira en 1 año
  const encodedProducts = encodeURIComponent(JSON.stringify(allProducts));
  document.cookie = `cartProducts=${encodedProducts}; expires=${expirationDate.toUTCString()}; path=/`;
};

const loadProductsFromCookie = () => {
  const cookies = document.cookie.split(';');
  const cartCookie = cookies.find(cookie => cookie.trim().startsWith('cartProducts='));
  if (cartCookie) {
    const encodedProducts = cartCookie.split('=')[1];
    const decodedProducts = decodeURIComponent(encodedProducts);
    allProducts = JSON.parse(decodedProducts);
    showHTML();
  }
};

loadProductsFromCookie();
