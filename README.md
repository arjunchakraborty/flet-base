# Flet-Base

This repository contains a basic Flet application built using the Flet-model module. It demonstrates core functionalities like:
![Flet-base app preview screenshots](https://github.com/TonyXdZ/flet-base/blob/434bb2d59aa2f96b3758f5cc4e8252d16b5a9d51/flet-base-preview.png)
- **User Authentication:**

    - Login page with username and password input fields.
    - Signup page with email, username, password, and confirm password fields.
    - Basic user authentication logic (replace with your own implementation).
    
    ***The app does not send any requests you will be redirected to Home page after you enter random username and password in Login page or random info in Sign up page***
    
- **Navigation in home page:**
 
    - Bottom navigation bar with Home, Messages, and Profile views.


**Getting Started**

1. **Clone the repository:**
   ```bash
   git clone git@github.com:TonyXdZ/flet-base.git
   ```

2. **Install dependencies:**

After activating your virtual environment :
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   flet run app.py 
   ```

**Project Structure**

```
flet-base/
├── app.py             # Main application file
├── pages/
│   ├── login.py       # Login page view
│   ├── signup.py      # Signup page view
│   ├── home.py        # Home page view
└── ...                 # Other files 
```

**Contributing**

Contributions are welcome! Please feel free to fork this repository and submit pull requests.

**License**

This project is licensed under the [MIT License](https://tlo.mit.edu/resources/open-source-initiative).

**Note:**

This is a basic example. You should adapt and extend it to fit your specific needs. Consider adding features like:

- **Sending requests:** Requests using requests python module to your api enpoint to get data like JWT token for user and user data.
- **Error handling and user feedback:** Check if server is alive and user is connected and provide human readable errors.
- **Improved UI/UX:** Enhance the visual appeal and user experience.
- **Security measures:** Implement robust security measures to protect user data by using client encrypt and decrypt from flet.security before saving it to client storage.
