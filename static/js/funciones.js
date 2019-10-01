
let cine_s=document.querySelector('#cine');
let sala_s=document.querySelector('#sala');
let pantalla_s=document.querySelector('#pantalla');
let contenido=document.querySelector('#contenido')
let semana_s=document.querySelector('#semana')
let pred=document.querySelector("#prede");
// let semana_s=document.querySelector("#semana");
let sello_s=document.querySelector("#productora");
let genero_s=document.querySelector("#genero");
let resultado=document.querySelector("#resultado");
let base=[];



$( document ).ready(function() {
    traer();
});

function traer(){
    fetch(`${window.origin}/cines`)
        .then(res => res.json())
        .then(datos => {
            base=datos;
            cine_s.innerHTML=''; 
            cine_s.innerHTML=`
            <option value="error" selected>Cine...</option>
        `
    
                for(let valor of datos){

        
                    cine_s.innerHTML+=`
                    <option value="${valor.CINE}">${valor.CINE}</option>
                    `
                }
            
        })

        semana();
        
}



function semana(){

    semana_s.innerHTML='';
        semana_s.innerHTML='<option value="error" selected>Semana...</option>';
    

            for(i=1;i<52;i++){

    
                semana_s.innerHTML+='<option value="'+i+'">'+i+'</option>';
                
            }



}

function pantalla(){

    for(let i=0;i < base.length;i++){
         
        
        if (base[i].CINE==cine_s.value){
             cinee=base[i].pantalla;
            //  console.log(cinee[0])
             pantalla_s.innerHTML='';
             pantalla_s.innerHTML='<option value="error" selected>Pantallas...</option>';
             
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
            sala_s.innerHTML=""; 
            sala_s.innerHTML='<option value="error" selected>Salas...</option>';
             
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
    semana();

}   

function enviar(){

    console.log('me diste un click')

}
cine_s.addEventListener('change',iniciar);



pred.addEventListener("submit",function(e){
    e.preventDefault();
    let valores={"week":0,"salas":0,"ARECIBO":0,"ARUBA MEGAPLEX":0,"AUTO CINE SANTANA":0,"BARCELONETA":0,"BELTZ OUTLET":0,"C3TECH":0,"CINEMARK CURACAO":0,"CINEMAS AT PASEO":0,"COLE BAY (MEGAPLEX)":0,"DORADO":0,"E DE VEER ARUBA":0,"FAJARDO":0,"FINE ARTS":0,"FINE ARTS CAFE":0,"GUAYAMA":0,"ISABELA":0,"LAS AMERICAS":0,"LAS CATALINAS":0,"LAS PIEDRAS":0,"LOS COLOBOS":0,"MARKET SQUARE":0,"METRO":0,"MONTEHIEDRA":0,"MOVIE CURACAO":0,"PLAZA CAROLINA":0,"PLAZA CAYEY":0,"PLAZA DEL CARIBE":0,"PLAZA DEL NORTE":0,"PLAZA DEL SOL":0,"PLAZA ESCORIAL":0,"PLAZA GUAYNABO":0,"PONCE TOWNE":0,"RIO HONDO I":0,"RIO HONDO II":0,"SAN GERMAN":0,"SAN PATRICIO":0,"SANTA ISABEL CINEMAS":0,"ST CROIX":0,"ST. KITTS":0,"TEATRO BALLAJA":0,"TEATRO EXCELSIOR CABO ROJO":0,"TEATRO HOLLYWOOD":0,"TEATRO MUNICIPIO GUAYAMA":0,"TEATRO NARANJITO":0,"TEATRO ROOSEVELT":0,"TEATRO SAN RAFAEL":0,"TORTOLA":0,"TOWN CENTER CINEMA CORP":0,"VEGA ALTA":0,"WESTERN PLAZA":0,"YAUCO":0,"FOX":0,"IND":0,"LIO":0,"LOC":0,"OTHERS":0,"PAR":0,"PF":0,"PPI":0,"SPR":0,"UNI":0,"UPI":0,"WB":0,"WDI":0,"WF":0,"3D":0,"4DX":0,"CXC":0,"IMAX":0,"adventure":0,"animation":0,"comedy":0,"drama":0,"horror":0,"romcom":0,"superheroes":0}    
    // let entry={ "cine":cine_s.value,"sala":sala_s.value,"pantalla":pantalla_s.value,"semana":semana_s.value,"sello":sello_s.value,"genero":genero_s.value}
    if (cine_s.value != 'AGUADILLA'){
        valores[cine.value]=1
    }
        
    if (sello_s.value != 'BVI'){
        valores[sello_s.value]=1
    }
        
    valores["week"]=semana_s.value
    
    if(genero_s.value != 'action'){
        valores[genero_s.value]=1
    }
        
    valores["salas"]=sala_s.value
    if(pantalla_s.value != '2D'){
        valores[pantalla_s.value]=1
    }
        
    
    fetch(`${window.origin}/predict`,{
        method:"POST",
        credentials:"include",
        body:JSON.stringify(valores),
        cache:"no-cache",
        headers: new Headers({
            "content-type":"application/json" 
        })
    })
    .then(function(response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          return;
        }
        response.json().then(function(data) {
          console.log(data)
          resultado.innerHTML='';
          resultado.innerHTML=`
            <div class="alert alert-success" role="alert">
                 El valor predecido es: ${data.prediction}
            </div>
          `
        });
      })
      .catch(function(error) {
        console.log("Fetch error: " + error);
    });
})
