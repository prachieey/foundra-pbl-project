# 🍀 Foundra AI

**AI-Powered Networking & Collaboration Platform**

Connect with like-minded people based on skills, goals, interests, and industry. Discover cofounders, teammates, mentors, collaborators, and opportunities — all powered by intelligent matching.

---

## 📋 Overview

Foundra AI is an intelligent networking platform that helps professionals build meaningful connections through smart profile matching and AI-powered search. Whether you're looking for a cofounder, hiring teammates, seeking mentorship, or exploring collaboration opportunities, Foundra leverages advanced algorithms to connect you with the right people.

---

## ✨ Features

- **🤖 Smart Matching System** – AI-powered recommendations based on skills, goals, interests, and industry
- **👤 Profile Builder** – Create detailed profiles with skills, experience, and aspirations
- **🔍 Intelligent Search** – Find people using natural language queries and advanced filters
- **🎯 Claim Unique Handle** – Secure your unique identity on the platform
- **📊 Dashboard** – Personalized dashboard to track connections, matches, and activity
- **🌐 Responsive Design** – Modern, mobile-first UI that works seamlessly across devices
- **🔐 Secure Authentication** – Built-in user authentication with Clerk
- **💾 Local Storage** – Efficient data management using browser LocalStorage

---

## 🛠 Tech Stack

### Frontend
- **React** – UI framework
- **Vite** – Build tool and dev server
- **Framer Motion** – Smooth animations and transitions
- **TailwindCSS** – Utility-first CSS framework
- **React Router** – Client-side routing
- **Clerk** – Authentication
- **Sonner** – Toast notifications

### Backend
- **Flask** – Python web framework
- **Python** – Core backend logic

---

## 📁 Folder Structure

```
pbl/
├── frontend/                 # React + Vite frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── App.jsx          # Main app component
│   │   └── main.jsx         # Entry point
│   ├── public/              # Static assets
│   └── package.json         # Frontend dependencies
├── backend/                 # Flask backend
│   ├── app.py              # Main Flask application
│   └── venv/               # Python virtual environment
├── api/                     # API-related files
│   ├── app.py              # API endpoints
│   └── model.py            # ML models
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Clone the Repository
```bash
git clone https://github.com/prachieey/foundra-pbl-project.git
cd pbl
```

### Install Frontend Dependencies
```bash
cd frontend
npm install
```

### Setup Backend
```bash
cd ../backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install flask
```

---

## 💻 Running the Application

### Frontend
```bash
cd frontend
npm run dev
```
The frontend will be available at `http://localhost:5173`

### Backend
```bash
cd backend
# Activate virtual environment (if not already active)
python app.py
```
The backend will run on `http://localhost:5000`

---

## 🔮 Future Improvements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Real-time messaging system
- [ ] Advanced ML-based matching algorithms
- [ ] Mobile app (React Native)
- [ ] Group collaboration features
- [ ] Event scheduling and management
- [ ] Integration with LinkedIn, GitHub, and other platforms
- [ ] Analytics dashboard for admins
- [ ] API for third-party integrations
- [ ] Video call integration

---

## 📸 Screenshots

<!-- Add screenshots here -->
<!-- 
![Screenshot 1](path/to/screenshot1.png)
![Screenshot 2](path/to/screenshot2.png)
-->

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to Foundra AI, please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Team

- **Prachi Behal** – Project Lead

---

## 📞 Contact

For questions or feedback, please reach out via the project repository issues or contact the team directly.

---

**Built with ❤️ for the community**
