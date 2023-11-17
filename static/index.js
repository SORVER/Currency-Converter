document.addEventListener('DOMContentLoaded', () => {


   document.querySelector('#form').onsubmit = () => {


    // initialize new request
    const request = new XMLHttpRequest(); // making request like request libariry in python
    const currency = document.querySelector('#currency').value;
    request.open('POST', '/convert');
    
    request.onload = () => {
       
        const data = JSON.parse(request.responseText);

        if(data.success){
            const contents = `1 USD is equal to ${data.rate} ${currency}.`;
            document.querySelector('#result').innerHTML = contents;


        }else {
            document.querySelector('#result').innerHTML = "There was an error";


        }

    } 
    // it will get the data from index.html and send it to /convert then it will take the respone as JSON from /convert
    const data = new FormData();
    data.append('currency' , currency);
    request.send(data);
    return false;

   }







})