// Добавляем обработчик события прокрутки страницы
window.addEventListener('scroll', e => {
    // Изменяем CSS-переменную --scrollTop в зависимости от текущей позиции прокрутки
    document.body.style.cssText += `--scrollTop: ${this.scrollY}px`;
});

// Функция для валидации формы по её ID
function validateForm(formId) {
    const form = document.getElementById(formId);  // Получаем форму по её ID
    const inputs = form.querySelectorAll('input, select');  // Получаем все поля ввода и селекты в форме
    let isValid = true;  // Флаг для проверки валидности формы
    const today = new Date().toISOString().split('T')[0];  // Текущая дата в формате YYYY-MM-DD
    const formData = {};  // Объект для сохранения данных формы

    // Перебор всех полей формы
    inputs.forEach(input => {
        const fieldName = input.previousElementSibling ? input.previousElementSibling.innerText : input.getAttribute('placeholder') || input.name;  // Получаем имя поля

        // Валидация текстовых полей
        if (input.type === 'text') {
            const namePattern = /^[А-ЯЁA-Z][а-яёa-z]+$/;  // Регулярное выражение для имени
        
            if (input.value.trim() === "") {
                alert(`Поле "${fieldName}" обязательно для заполнения.\nПример: Имя должно содержать хотя бы 2 символа и быть написано кириллицей или латиницей.`);
                isValid = false;
            } else if (input.value.length < 2) {
                alert(`Поле "${fieldName}" должно содержать хотя бы 2 символа.\nПример: Иван или John.`);
                isValid = false;
            } else if (!namePattern.test(input.value)) {
                alert(`Поле "${fieldName}" должно начинаться с заглавной буквы, содержать только буквы кириллицы или латиницы, не иметь пробелов, цифр или специальных символов.\nПример: Иван или John.`);
                isValid = false;
            }
        
            formData[input.name] = input.value;  // Сохраняем значение поля в объект formData
        }
        
        // Валидация email
        if (input.type === 'email') {
            const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,6}$/;  // Регулярное выражение для email
            if (!emailPattern.test(input.value)) {
                alert(`Введите корректный адрес электронной почты в поле "${fieldName}".\nПример: example@example.com. Убедитесь, что в адресе нет пробелов и правильное использование символов "@".`);
                isValid = false;
            }
            formData[input.name] = input.value;  // Сохраняем значение поля в объект formData
        }

        // Валидация телефона
        if (input.type === 'tel') {
            const phonePattern = /^[0-9]{10}$/;  // Регулярное выражение для телефона
            if (!phonePattern.test(input.value)) {
                alert(`Введите корректный номер телефона в поле "${fieldName}".\nНомер должен состоять из 10 цифр, например: 1234567890.`);
                isValid = false;
            }
            formData[input.name] = input.value;  // Сохраняем значение поля в объект formData
        }

        // Валидация даты
        if (input.type === 'date') {
            if (input.value < today) {
                alert(`Дата в поле "${fieldName}" не может быть в прошлом.\nПример: выберите дату, начиная с сегодняшнего дня.`);
                isValid = false;
            }
            formData[input.name] = input.value;  // Сохраняем значение поля в объект formData
        }

        // Валидация селектов
        if (input.tagName.toLowerCase() === 'select') {
            if (input.value === "") {
                alert(`Выберите значение в поле "${fieldName}".\nПример: выберите тип номера или место для погружения.`);
                isValid = false;
            }
            formData[input.name] = input.value;  // Сохраняем значение поля в объект formData
        }
    });

    // Если форма валидна, сохраняем данные в localStorage
    if (isValid) {
        localStorage.setItem('formData', JSON.stringify(formData));
    }

    return isValid;  // Возвращаем результат валидации
}