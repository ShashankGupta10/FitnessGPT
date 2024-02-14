# FitnessGPT 🏋

FitnessGPT is an innovative web application designed to revolutionize your fitness journey. Powered by cutting-edge technology, FitnessGPT combines the latest advancements in artificial intelligence with expert knowledge in fitness and health to provide you with personalized guidance and support.

**Introduction:**
Are you looking to kickstart your fitness routine but don't know where to begin? Do you struggle to stay motivated and accountable? Look no further than FitnessGPT. Our platform offers a comprehensive suite of features to help you achieve your fitness goals effectively and efficiently.

## Setup

### Frontend (React)

1. Clone the repository containing the React frontend.
2. Navigate to the project directory.
3. Install dependencies by running `npm install`.
4. Start the development server with `npm start`.
5. The React app should now be running on `http://localhost:3000`.

### Backend (Flask with LangChain)

1. Clone the repository and open the cloned repo.
2. Navigate to the server directory.
3. Create a virtual environment: `python -m venv environment`.
4. Activate the virtual environment:
   - On Windows: `environment\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies with `pip install -r requirements.txt`.
6. Configure the `.env` file with the `COHERE_API_KEY` and the `OPENAI_API_KEY`.
7. Start the Flask server: `flask run`.
8. The Flask app should now be running on `http://localhost:5000`.

## Deployment on Cloud

### Frontend (React)

1. Build the React app for production: `npm run build`.
2. The build files will be generated in the `build` directory.
3. Deploy the contents of the `build` directory to a static hosting service like Netlify, Vercel, or AWS S3.

### Backend (Flask with LangChain)

1. Choose a cloud platform for deployment (e.g., AWS, GCP, Azure).
2. Set up a virtual server instance (e.g., EC2 on AWS, Compute Engine on GCP).
3. Install required dependencies on the server (Python, Flask, LangChain).
4. Transfer your Flask project files to the server.
5. Configure the server to run Flask app as a WSGI application.
6. Ensure LangChain is properly configured and installed on the server.
7. Start the Flask app on the server.
8. Set up a domain name and configure DNS settings to point to your server's IP address.

## Conclusion

This concludes the setup and deployment process for the React and Flask web app with LangChain integration. Ensure to follow security best practices during deployment and consider using SSL certificates for secure communication.
