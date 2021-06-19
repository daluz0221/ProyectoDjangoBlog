var nums = [-3, -2, -1, -1, 2, 3]


function closestToZero(numbers) {
    
    let num1 = Math.abs(numbers[0])
    let resu;
    for (let i = 0; i < numbers.length; i++) {
        let element = Math.abs(numbers[i]);
        // console.log(element);
        if (element < num1 ) {
            resu = element
            num1 = resu
            console.log(resu);
        }

    }

    return resu
}


console.log(closestToZero(nums));
// console.log();
  