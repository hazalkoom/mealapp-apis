# Users API

This project currently implements the **Users** module, which handles user registration, authentication, profile management, password changes, password resets, and email verification.

## Features implemented for Users so far:

- **User Registration:** Allows users to register with name, email, and password.
- **Email Verification:** Sends a verification email after registration with a tokenized link.
- **User Login:** Token-based authentication using JWT or DRF tokens.
- **User Profile:** Retrieve, update, or delete the user profile. Supports updating fields like avatar and name.
- **Change Password:** Allows logged-in users to change their password by providing the current and new passwords.
- **Password Reset:** Supports password reset via email with token-based confirmation.
- **API Documentation:** Integrated Swagger UI for interactive API exploration and testing.

## To Do

- Additional app modules (to be implemented in the future)
- Frontend integration with the Users API
- Further testing and deployment setup

---

For now, this repository focuses solely on the Users functionality. More features and apps will be added later.
