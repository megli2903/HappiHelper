document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const loginMessage = document.getElementById("loginMessage");
    const signupMessage = document.getElementById("signupMessage");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Login logic (replace with your authentication logic)
        if (username === "user" && password === "password") {
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

        // Signup logic (replace with your registration logic)
        if (signupPassword !== confirmPassword) {
            signupMessage.textContent = "Password and confirm password do not match.";
            signupMessage.style.color = "red";
        } else {
            // Here, you can add your user registration code.
            // For example, you can call a function like registerUser(signupUsername, signupPassword).
            // Make sure to replace this with your actual registration logic.
            const registrationResult = registerUser(signupUsername, signupPassword);
            
            // Display the registration result
            signupMessage.textContent = registrationResult.message;
            signupMessage.style.color = registrationResult.success ? "green" : "red";
        }
    });
    
    // Function to register a user (replace with your registration logic)
    function registerUser(username, password) {
        // Replace this with your actual registration logic.
        // You can use the example from previous responses or integrate it with a database.
        
        // For now, let's assume a successful registration.
        // In practice, you should add error handling and database integration here.
        return {
            success: true,
            message: "Registration successful!",
        };
    }
});
