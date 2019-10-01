
let cine_s=document.querySelector('#cine');
let sala_s=document.querySelector('#sala');
let pantalla_s=document.querySelector('#pantalla');
let contenido=document.querySelector('#contenido')
let semana_s=document.querySelector('#semana')
let predecir=document.querySelector("#prede");
// let semana_s=document.querySelector("#semana");
let sello_s=document.querySelector("#productora");
let genero_s=document.querySelector("#genero");
let resultado=document.querySelector("#resultado");
let base=[];



$( document ).ready(function() {
    traer();
});

function traer(){
    fetch('http://localhost:1234/cines')
        .then(res => res.json())
        .then(datos => {
            base=datos;
             
            cine_s.innerHTML=`
            <option selected>Cine...</option>
        `
    
                for(let valor of datos){

        
                    cine_s.innerHTML+=`
                    <option value="${valor.CINE}">${valor.CINE}</option>
                    `
                }
            
        })
       
        semana_s.innerHTML='<option selected>Semana...</option>';
    

            for(i=1;i<38;i++){

    
                semana_s.innerHTML+='<option value="'+i+'">'+i+'</option>';
                
            }
}


function pantalla(){

    for(let i=0;i < base.length;i++){
         
        
        if (base[i].CINE==cine_s.value){
             cinee=base[i].pantalla;
            //  console.log(cinee[0])
             pantalla_s.innerHTML='<option selected>Pantallas...</option>';
             
            for(let j=0; j<cinee.length;j++){
                // console.log(cinee[j]);
                pantalla_s.innerHTML+='<option value="'+cinee[j]+'">'+cinee[j]+'</option>';
            }
            break;

         }

    }


}






function salas() {
    
    
    // console.log(valor);
    for(let i=0;i < base.length;i++){
         
        
        if (base[i].CINE==cine_s.value){
             cinee=base[i].salas;
            //  console.log(cinee[0])
             sala_s.innerHTML='<option selected>Salas...</option>';
             
            for(let j=0; j<cinee.length;j++){
                // console.log(cinee[j]);
                sala_s.innerHTML+='<option value="'+cinee[j]+'">'+cinee[j]+'</option>';
            }
            break;

         }

    }
}  


    
function iniciar(){

    salas();
    pantalla();

}   

function enviar(){

    console.log('me diste un click')

}
cine_s.addEventListener('change',iniciar);
predecir.addEventListener("submit",function(e){
    e.preventDefault();
 if(cine_s===null||sala_s===null||pantalla_s===null||semana_s===null||semana_s===null||sello_s===null||genero_s===null){
    
    let datos=new FormData(predecir);
    console.log(datos.get('cine'))
    fetch('http://localhost:1234/ver',{
        method: 'POST',
        body: datos

    })
        .then(res => res.json())
        .then(data => {
            console.log(data.prediction)
            resultado.innerHTML='';
            resultado.innerHTML= `
            <h1>La cantidad de entradas predecida es: ${data.prediction}</h1>
            
            `
        

        })

 }else{

    resultado.innerHTML='';
            resultado.innerHTML= `
            <h1>Complete todos los campos</h1>
            
            `
 }

});