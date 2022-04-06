let arr = [5,7,9,2,66,55,2,1];
let temp


function buuble_sort(arr) {
    for(let i=0; i < arr.length; i++) {
        for(let j=0; j < arr.length - i; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j]; 
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}

console.log(buuble_sort(arr));