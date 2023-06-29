window.addEventListener('DOMContentLoaded', (event) => {
  // Obtiene la referencia a la sección de destino por su ID
  const seccionDestino = document.getElementById('contenido');

  // Comprueba si se encontró la sección
  if (seccionDestino) {
     // Hace scroll suave hasta la sección de destino
     seccionDestino.scrollIntoView({ behavior: 'smooth' });
  }
});


const btnCart = document.querySelector('.container-cart-icon')
const containerCartProducts = document.querySelector('.container-cart-products')

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart')
})

// validaciones created by Jonathan and internet

window.addEventListener('load', () => {
  const formulario = document.getElementById('form');
  const nombre = document.getElementById('name');
  const correo = document.getElementById('email');
  const alias = document.getElementById('username');
  const contraseña = document.getElementById('password');
  const match = document.getElementById('matchpass');

  formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    validaCampos();
  });


  const showAlert = (message) => {
    const alertModal = document.getElementById('alertModal');
    const alertMessage = document.getElementById('alertMessage');

    alertMessage.textContent = message;
    $(alertModal).modal('show');
    throw new Error(message);
  };

  const showAlertv2 = (message) => {
    const alertModal = document.getElementById('alertModalv2');
    const alertMessage = document.getElementById('alertMessagev2');

    alertMessage.textContent = message;
    $(alertModal).modal('show');
    throw new Error(message);
  };

  const validaCampos = () => {
    const nombreValor = nombre.value.trim();
    const correoValor = correo.value.trim();
    const aliasValor = alias.value.trim();
    const contraseñaValor = contraseña.value.trim();
    const matchValor = match.value.trim();

    if (nombreValor === '') {
      showAlert('Su Nombre esta vacio, por favor ingrese su Nombre');
    } else if (nombreValor.length < 3) {
      showAlert('Su Nombre debe tener al menos 3 caracteres');
    } 

    if (correoValor === '') {
      showAlert('Su correo electronico esta vacio.');
    } else if (!/^([a-zA-Z0-9_\.-]+)@([\da-zA-Z\.-]+)\.([a-zA-Z\.]{2,6})$/.test(correoValor)) {
      showAlert('Por favor Ingrese un Correo Electronico Valido');
    } 

    if (aliasValor === '') {
      showAlert('Su alias esta vacio, por favor ingrese un alias');
    } else if (aliasValor.length < 6) {
      showAlert('Su nombre de usuario debe tener al menos 6 caracteres');
    } 

    if (contraseñaValor === '') {
      showAlert('Su contraseña esta vacia, por favor ingrese una contraseña');
    } else if (contraseñaValor.length < 8) {
      showAlert('Su contraseña debe tener al menos 8 caracteres');
    } else if (!/(?=.*[A-Z])(?=.*\W)/.test(contraseñaValor)) {
      showAlert('Su contraseña debe tener al menos una mayúscula y un carácter especial');
    } 

    if (matchValor === '') {
      showAlert('El apartado de confirmar contraseña esta vacio');
    } else if (matchValor !== contraseñaValor) {
      showAlert('Por favor ingrese la misma contraseña que ingreso en el apartado anterior');
    }
    showAlertv2('Cuenta creada con exito, por favor revise su correo electronico para confirmar su cuenta');
    
  };
  
  

});

