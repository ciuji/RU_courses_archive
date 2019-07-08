//change the unit, and use the unit to change the table
function setUnit(unit){
  document.getElementById('unit_show').innerHTML="You select to use "+unit+" units";
  if(unit=="SI"){
    document.getElementById('unit_t1').innerHTML="(m)";
    document.getElementById('unit_t2').innerHTML="(m)";
    document.getElementById('unit_t3').innerHTML="(m^3)";
  }else if(unit=='English'){
    document.getElementById('unit_t1').innerHTML="(ft)";
    document.getElementById('unit_t2').innerHTML="(ft)";
    document.getElementById('unit_t3').innerHTML="(ft^3)";
  }
}

//set shape, and set default value for different shape
function setShape(shape){
  document.getElementById('shape_show').innerHTML="You selected to find the volume of "+shape;
  document.getElementById('shape_t').innerHTML=shape;
  setVolume('');
  if(shape == 'Sphere'){
    document.getElementById('heightText').disabled = true;
    setHeight('N/A');
  }else{
    document.getElementById('heightText').disabled = false;
    setHeight(document.getElementById('heightText').value);
  }
}

//reset the form 
function resetForm(){
  document.getElementById("myForm").reset();
  setUnit('English');
  setShape('Cylinder');
  setRadius('');
  setHeight('');
  setVolume('')
}

function setRadius(value) {
  if(!isNaN(value)){
    document.getElementById('radius').innerHTML=value;
  }else{
    document.getElementById('radius').innerHTML='INVALID';
  }
}

//set height
function setHeight(value){
  if(!isNaN(value)){
      document.getElementById('height').innerHTML=value;
  }else{
    if(value == 'N/A')
      document.getElementById('height').innerHTML=value;
    else
      document.getElementById('height').innerHTML='INVALID';
  }
}

//do calculation
function calculate(){
  var shape=document.getElementById('shape_t').innerHTML;
  var r = document.getElementById('radius').innerHTML;
  var h = document.getElementById('height').innerHTML;
  var res = 0;
  var PI = 3.14159;
  if(isNaN(r) || (isNaN(h) && shape != 'Sphere')){
    setVolume('INVALID');
  }else{
    if(shape == 'Cylinder'){
        res = PI*r*r*h;
    } else if (shape == 'Sphere') {
        res = PI*r*r*r*4/3;
    } else if (shape == 'Cone') {
        res = PI*r*r*h/3;
    }
    res=res.toFixed(5)
    setVolume(res);
  }
}

function setVolume(value){
  document.getElementById('volume').innerHTML=value;
}