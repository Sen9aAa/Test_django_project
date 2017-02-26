var x=[];
var N = 0;
function my_request_history(y){
  for(var i=0;i<y.length;i++){
    if (!(y[i] in x )){
      x.push(y[i]);
      N++;
      console.log(N)}; 
    };
  };



