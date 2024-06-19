// let birthdayList = [];

// document.getElementById('birthday-form').addEventListener('submit', (e) => {
//     e.preventDefault();
//     let name = document.getElementById('name').value;
//     let birthday = document.getElementById('birthday').value;
//     addBirthdayToList(name, birthday);
//     document.getElementById('name').value = '';
//     document.getElementById('birthday').value = '';
// });

// function addBirthdayToList(name, birthday) {
//     birthdayList.push({ name: name, birthday: birthday });
//     displayBirthdayList();
// }

// function displayBirthdayList() {
//     let listHTML = '';
//     birthdayList.forEach((birthday) => {
//         listHTML += `<li>${birthday.name} - ${birthday.birthday}</li>`;
//     });
//     document.getElementById('birthday-list').innerHTML = listHTML;
// }

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });