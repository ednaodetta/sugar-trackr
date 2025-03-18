    document.querySelectorAll('select').forEach(select => {
        select.addEventListener('focus', () => {
            select.closest('.form-group').classList.add('expanded');
        });

        select.addEventListener('blur', () => {
        select.closest('.form-group').classList.remove('expanded');
        });
    });

    function calculateBMI() {
        const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);
        
        if (height > 0 && weight > 0) {
            const bmi = weight / (height * height);
    document.getElementById("bmiResult").value = bmi.toFixed(2);
        } else {
        alert("Please enter valid height and weight values.");
        }
    }
