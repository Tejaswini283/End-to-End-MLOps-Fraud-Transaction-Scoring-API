
# End-to-End MLOps Fraud Transaction Scoring API 🚀

A production-grade API for real-time fraud detection, built with a complete MLOps pipeline using Docker, GitHub Actions, and Render for cloud deployment.

**Live API Endpoint:** `[YOUR RENDER URL HERE]`

-----

## Project Overview

This project demonstrates a full, end-to-end MLOps workflow for deploying a machine learning model as a robust, scalable web service. The core of the project is a transaction scoring API that classifies financial transactions as fraudulent or legitimate in real-time.

The emphasis is not just on the model's accuracy, but on the engineering practices required to serve it in a production environment. The entire pipeline, from code commit to cloud deployment, is fully automated, ensuring reliability and reproducibility.

-----

## MLOps Architecture

The project follows a modern CI/CD (Continuous Integration/Continuous Deployment) architecture to automate the entire lifecycle of the machine learning application.

The workflow is as follows:

1.  **Code Commit:** A developer pushes new code to the `main` branch on GitHub.
2.  **CI/CD Pipeline:** **GitHub Actions** automatically triggers a workflow.
3.  **Build & Push:** The action builds a new **Docker** image of the FastAPI application.
4.  **Container Registry:** The new image is pushed to a container registry (like Docker Hub).
5.  **Deployment:** **Render** detects the new image, pulls it, and automatically deploys the updated container, resulting in zero-downtime updates.

-----

## 🛠️ Tech Stack

  * **Model:** LightGBM
  * **Backend:** FastAPI, Uvicorn
  * **Data Processing:** Pandas, Scikit-learn
  * **Containerization:** Docker
  * **CI/CD:** GitHub Actions
  * **Cloud Hosting:** Render

-----

## ✨ Features

  * **Real-Time Predictions:** An API endpoint (`/predict`) that scores transactions in milliseconds.
  * **Automated Deployment:** A fully automated CI/CD pipeline ensures that any push to the `main` branch is automatically built and deployed.
  * **Containerized & Portable:** The entire application is packaged with Docker, making it easy to run consistently in any environment.
  * **Scalable:** Hosted on Render's serverless infrastructure, capable of handling variable traffic loads.

-----

## 💻 Running Locally

To run this project on your local machine, follow these steps:

**Prerequisites:**

  * Python 3.9+
  * Git
  * Docker Desktop

**1. Clone the repository:**

```bash
git clone https://github.com/YourUsername/End-to-End-MLOps-Fraud-Transaction-Scoring-API.git
cd End-to-End-MLOps-Fraud-Transaction-Scoring-API
```

**2. Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install the dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the API server:**

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

-----

## 🚀 API Usage

You can interact with the deployed API via the interactive documentation at `[YOUR RENDER URL HERE]/docs` or by sending a `POST` request to the `/predict` endpoint.

### Endpoint: `/predict`

  * **Method:** `POST`
  * **Body:** A JSON object containing a single key `features`, which is a list of 30 float values representing the transaction data.

**Example `curl` Request:**

```bash
curl -X POST "YOUR_RENDER_URL_HERE/predict" \
-H "Content-Type: application/json" \
-d '{
  "features": [0, -1.35, 1.2, 2.5, 1.3, -0.4, 0.4, -0.9, -2.2, -3.2, 1.0, -0.6, -2.8, -0.1, -1.7, 0.7, -0.3, 0.4, 0.9, 0.3, -0.2, 0.2, 0.7, 0.2, 0.1, -0.5, 0.3, 0.2, 0.1, 250.0]
}'
```

**Example Success Response:**

```json
{
  "prediction": "Not Fraud",
  "fraud_probability": 0.00012345
}
```

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
