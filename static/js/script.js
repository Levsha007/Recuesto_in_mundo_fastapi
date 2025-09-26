// Добавляем обработчик события прокрутки страницы
window.addEventListener('scroll', e => {
    // Изменяем CSS-переменную --scrollTop в зависимости от текущей позиции прокрутки
    document.body.style.cssText += `--scrollTop: ${this.scrollY}px`;
});

/*
gsap.registerPlugin(ScrollTrigger, ScrollSmoother);  // Регистрируем плагины для GSAP
ScrollSmoother.create({
    wrapper: '.wrapper',  // Обертка для плавной прокрутки
    content: '.content'  // Контент для плавной прокрутки
});
*/

// Добавляем обработчик события для всех элементов с классом "date"
document.querySelectorAll('.date').forEach(function(dateElement) {
    dateElement.addEventListener('mouseenter', function() {
        // Получаем ID даты
        let id = dateElement.getAttribute('data-id');
        // Находим соответствующий скрытый блок с текстом
        let infoText = document.getElementById('info-' + id).innerText;
        // Вставляем текст в псевдоэлемент через стиль
        dateElement.style.setProperty('--info', `'${infoText}'`);
    });
});

const dates = document.querySelectorAll('.left_footer_date, .right_footer_date');  // Получаем все элементы с классами "left_footer_date" и "right_footer_date"
const info = document.querySelector('.info');  // Получаем элемент с классом "info"

// Добавляем обработчик события для всех элементов с классами "left_footer_date" и "right_footer_date"
dates.forEach(date => {
    date.addEventListener('mouseenter', () => {
        info.innerHTML = date.getAttribute('data-info');  // Получаем информацию из атрибута data-info и вставляем её в элемент с классом "info"
        info.style.visibility = 'visible';  // Показываем элемент с классом "info"
    });

    date.addEventListener('mouseleave', () => {
        info.style.visibility = 'hidden';  // Скрываем элемент с классом "info" при уходе курсора
    });
});

// Функция для плавного прокручивания к элементу по его ID
function scrollToCenter(id) {
    event.preventDefault();  // Отменяет стандартное поведение якоря
    const element = document.getElementById(id);  // Получаем элемент по его ID
    
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',  // Плавная прокрутка
            block: 'center',  // Центрирование элемента
            inline: 'center'  // Центрирование по горизонтали (если нужно)
        });
    }
}