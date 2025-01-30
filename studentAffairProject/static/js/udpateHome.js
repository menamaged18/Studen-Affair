// let Students;
// //if there is a data in localStorage put it in students else create an empty array
// if (localStorage.Students != null) {
//     Students = JSON.parse(localStorage.Students);
// }else{
//     Students = []; 
// }

// document.addEventListener('DOMContentLoaded', function () {
    
//     // Get the Add button element
//     const EditButton = document.querySelector('#editButton');


//     // Add click event listener to the Add button
//     EditButton.addEventListener('click', function () {
//         alert("edit button clicked");
//         // Get the input field values
//         const id = document.querySelector('#inputid').value;
//         for(let i = 0 ; i < Students.length ; i++){
//             if (id === Students[i].id) {
//                 localStorage.setItem("Index",JSON.stringify(i));
//                 location.href = "{% url 'updatehomepage' %} ";
//                 return;
//             }
//         }
//         alert("Id not found");
//     });
// });
