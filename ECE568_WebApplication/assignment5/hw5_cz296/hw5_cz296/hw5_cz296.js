function setUnit(unit){
  //change the sentence in result
  document.getElementById('unit').innerHTML="You select to use "+unit+" units";
  //change the value in table
  if(unit=="SI"){
    document.getElementById('unit_t1').innerHTML="(m)";
    document.getElementById('unit_t2').innerHTML="(m)";
    document.getElementById('unit_t3').innerHTML="(m^3)";
  }else{
    document.getElementById('unit_t1').innerHTML="(ft)";
    document.getElementById('unit_t2').innerHTML="(ft)";
    document.getElementById('unit_t3').innerHTML="(ft^3)";
  }
}

function setShape(shape){
  //change the sentence in result
  document.getElementById('shape').innerHTML="You selected to find the volume of "+shape;
  //change the value in table
  document.getElementById('shape_t').innerHTML=shape;
  //reset volume
  setVolume('');
  //enable or disable the height
  if(shape == 'Sphere'){
    document.getElementById('heightText').disabled = true;
    setHeight('N/A');
  }else{
    document.getElementById('heightText').disabled = false;
    setHeight(document.getElementById('heightText').value);
  }
}

function resetForm(){
  //reset the form
  document.getElementById("myForm").reset();
  //reset the table
  setUnit('English');
  setShape('Cylinder');
  setRadius('');
  setHeight('');
}

//todo check data type
function setRadius(value) {
  //change the value in table
  if(!isNaN(value)){
    document.getElementById('radius').innerHTML=value;
  }else{
    document.getElementById('radius').innerHTML='INVALID';
  }
  setVolume('');
}

function setHeight(value){
  //change the value in table
  if(!isNaN(value)){
      document.getElementById('height').innerHTML=value;
  }else{
    if(value == 'N/A')
      document.getElementById('height').innerHTML=value;
    else
      document.getElementById('height').innerHTML='INVALID';
  }
  setVolume('');
}

function calc(){
  var shape=document.getElementById('shape_t').innerHTML;
  var r = document.getElementById('radius').innerHTML;
  var h = document.getElementById('height').innerHTML;
  var vol = 0;
  var PI = 3.141592653;
  if(isNaN(r) || (isNaN(h) && shape != 'Sphere')){
    setVolume('INVALID');
  }else{
    if(shape == 'Cylinder'){
        vol = PI*r*r*h;
    } else if (shape == 'Sphere') {
        vol = PI*r*r*r*4/3;
    } else if (shape == 'Cone') {
        vol = PI*r*r*h/3;
    }
    setVolume(vol);
  }
}

function setVolume(value){
  document.getElementById('volume').innerHTML=value;
}