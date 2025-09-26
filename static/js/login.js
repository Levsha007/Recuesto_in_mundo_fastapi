// Добавляем обработчик события прокрутки страницы
window.addEventListener('scroll', e => {
    // Изменяем CSS-переменную --scrollTop в зависимости от текущей позиции прокрутки
    document.body.style.cssText += `--scrollTop: ${this.scrollY}px`;
});

/*
const container = document.getElementById('container');  // Получаем элемент с ID "container"
const registerBtn = document.getElementById('register');  // Получаем кнопку регистрации
const loginBtn = document.getElementById('login');  // Получаем кнопку входа

// Обработчик события для кнопки регистрации
registerBtn.addEventListener('click', () => {
    container.classList.add("active");  // Добавляем класс "active" к контейнеру
});

// Обработчик события для кнопки входа
loginBtn.addEventListener('click', () => {
    container.classList.remove("active");  // Удаляем класс "active" у контейнера
});
*/