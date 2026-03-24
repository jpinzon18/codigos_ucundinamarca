const boton =
document.getElementById("btn");

boton.addEventListener("click", function(){
    const colores=["red", "blue","green", "yellow", "purple", "gray", "white", "pink", "orange", "brown"];
    const aleatorio = colores[Math.floor(Math.random()*colores.length)];
    document.body.style.backgroundColor=aleatorio;
});