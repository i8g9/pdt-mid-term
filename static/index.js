function taxCalc(){

    //check input
    if (document.getElementById('mIncome').value.length == 0){
        alert('You have to input your monthly income');
    }else if (document.getElementById('exIncome').value.length == 0){
        alert('You have to input your extra income. If you don\'t have any extra income, leave it as 0')
    }
    
    var mIncome = parseFloat(document.getElementById('mIncome').value);
    var exIncome = parseFloat(document.getElementById('exIncome').value);

    //tahunan
    var annIncome = (mIncome + exIncome)*12;
    //status
    var status = document.getElementById('status').value;
    //NPWP
    var npwp = document.getElementById('npwp').value;

    //console.log(annIncome);
    //console.log(status);
    //console.log(npwp);

    var url = '/taxCalc';

    axios({
        method: "post",
        url: url,
        data: {
            income: annIncome,
            status: status,
            npwp: npwp,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data ;
            console.log(response);
            document.getElementById('result').innerHTML = result['result'];
        },
        (error) => {
            console.log(error);
            console.log(result['status']);
        }
    );
}

