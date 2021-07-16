var clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]];



function solution(clothes) {
    var answer=0
    
    var arr1 = [];
    var arr2 = [];
    
    for(i=0; i< clothes.length; i++){
        
        arr1 = arr1.concat(clothes[i])
    }
    
    var j=0;
    
    while(j<1+(arr1.length/2)){
        
        arr1.splice(1+2*j,1);    
        
    }
    
    var k=0;
    var a=1;
    
    while(k<arr1.length)
    {
        if(arr1[k]=arr1[a])
        {
            arr1.splice(a,1);
            a=a+1;
            if(arr1[a]="")
            {
                break;
            }
        }
        
    }

   console.log(arr1);
   
