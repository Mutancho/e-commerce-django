// static/js/passwords.js

function setupPasswordValidationChecks(password1Id, password2Id) {
    const password1 = document.getElementById(password1Id);
    const password2 = document.getElementById(password2Id);
    const passwordMatchMessage = document.getElementById('password-match-message');

    // Criteria elements
    const lengthCriteria = document.getElementById('length-criteria');
    const uppercaseCriteria = document.getElementById('uppercase-criteria');
    const numberCriteria = document.getElementById('number-criteria');
    const specialCharCriteria = document.getElementById('special-char-criteria');

    function validateCriteria(password) {
        const lengthCriteriaMet = password.length >= 8;
        const uppercaseCriteriaMet = /[A-Z]/.test(password);
        const numberCriteriaMet = /[0-9]/.test(password);
        const specialCharCriteriaMet = /[^A-Za-z0-9]/.test(password);

        // Toggle validation classes based on whether criteria are met
        lengthCriteria.classList.toggle('text-valid', lengthCriteriaMet);
        lengthCriteria.classList.toggle('text-invalid', !lengthCriteriaMet);

        uppercaseCriteria.classList.toggle('text-valid', uppercaseCriteriaMet);
        uppercaseCriteria.classList.toggle('text-invalid', !uppercaseCriteriaMet);

        numberCriteria.classList.toggle('text-valid', numberCriteriaMet);
        numberCriteria.classList.toggle('text-invalid', !numberCriteriaMet);

        specialCharCriteria.classList.toggle('text-valid', specialCharCriteriaMet);
        specialCharCriteria.classList.toggle('text-invalid', !specialCharCriteriaMet);

        // Return true only if all criteria are met
        return lengthCriteriaMet && uppercaseCriteriaMet && numberCriteriaMet && specialCharCriteriaMet;
    }

    function checkPasswordMatch() {
        // Validate individual criteria
        const allCriteriaMet = validateCriteria(password1.value);

        // Check if passwords match and all criteria are met
        if (password1.value === password2.value && allCriteriaMet) {
            password2.classList.add('is-valid');
            password2.classList.remove('is-invalid');
            passwordMatchMessage.textContent = 'Passwords match.';
            passwordMatchMessage.className = 'form-text text-success';
        } else {
            password2.classList.remove('is-valid');
            password2.classList.add('is-invalid');
            passwordMatchMessage.textContent = '';
        }
    }

    // Set up event listeners
    password1.addEventListener('input', checkPasswordMatch);
    password2.addEventListener('input', checkPasswordMatch);
}

// This function should be called on the relevant pages to initialize the validation checks
