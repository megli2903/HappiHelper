document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const loginMessage = document.getElementById("loginMessage");
    const signupMessage = document.getElementById("signupMessage");

    // Simulated user database (for demonstration purposes)
    const userDatabase = {
        "sasetrainer": "sasehack123", // Adding a predefined user
    };

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Simulated login logic (replace with your authentication logic)
        if (userDatabase[username] && userDatabase[username] === password) {
            loginMessage.textContent = "Login successful!";
            loginMessage.style.color = "green";
        } else {
            loginMessage.textContent = "Login failed. Please try again.";
            loginMessage.style.color = "red";
        }
    });

    signupForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const signupUsername = document.getElementById("signupUsername").value;
        const signupPassword = document.getElementById("signupPassword").value;
        const confirmPassword = document.getElementById("confirmPassword").value;

        // Simulated signup logic (for demonstration purposes)
        if (userDatabase[signupUsername]) {
            signupMessage.textContent = "Username already exists. Please choose a different one.";
            signupMessage.style.color = "red";
        } else if (signupPassword !== confirmPassword) {
            signupMessage.textContent = "Password and confirm password do not match.";
            signupMessage.style.color = "red";
        } else {
            // Add the new user to the simulated database (replace with actual registration logic)
            userDatabase[signupUsername] = signupPassword;

            // Registration successful
            signupMessage.textContent = "Registration successful!";
            signupMessage.style.color = "green";
        }
    });
});
