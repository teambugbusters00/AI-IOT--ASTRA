VIDEO  = {  ]
### Frontend (somethingaiiot/)
- **Framework**: React 18 with Vite
- **Routing**: React Router
- **Styling**: Tailwind CSS with custom components
- **State Management**: React Context (Theme)
- **UI Library**: Custom components with animations

### Unified Backend (backend/)
- **Framework**: FastAPI
- **AI Model**: Microsoft Phi-2 (via Transformers)
- **Dataset**: Open Schematics from HuggingFace
- **Features**: Authentication, dashboard data, device simulation, AI code generation
- **Database**: JSON file persistence


This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
# somethingaiiot
****
# AI-IOT-ASTRA Project Structure Diagram

## Overview
AI-IOT-ASTRA is an AI-powered IoT learning platform with a unified backend service and a React frontend. The system allows users to generate IoT code using AI, simulate devices, and manage projects.

## Architecture

```mermaid
graph TB
    subgraph "Frontend (React + Vite)"
        A[App.jsx] --> B[Router]
        B --> C[Layout.jsx]
        B --> D[Pages]
        D --> D1[Landing.jsx]
        D --> D2[Login.jsx]
        D --> D3[Signup.jsx]
        D --> D4[Dashboard.jsx]
        D --> D5[Workspace.jsx]
        D --> D6[Deploy.jsx]
        D --> D7[Examples.jsx]
        D --> D8[Settings.jsx]
        D --> D9[Projects.jsx]

        C --> E[Sidebar.jsx]
        C --> F[ThemeContext.jsx]

        D1 --> G[HeroSection.jsx]
        D1 --> H[Features.jsx]

        I[UI Components] --> I1[flickering-grid.tsx]
        I --> I2[meteors.tsx]
        I --> I3[orbiting-circles.tsx]
        I --> I4[rainbow-button.tsx]
        I --> I5[morphing-text.tsx]
        I --> I6[highlighter.tsx]

        J[Lib] --> J1[utils.ts]
    end

    subgraph "Unified Backend (FastAPI)"
        K[main.py] --> L[auth.py]
        K --> M[dashboard.py]
        K --> N[device.py]
        K --> O[ai.py]

        L --> P[models.py]
        L --> Q[database.py]

        O --> R[model.py]
        O --> S[prompt.py]
        O --> T[dataset.py]

        R --> U[Phi-2 Model]
        S --> T
        T --> V[HuggingFace Datasets]
    end

    A --> W[Backend API]
    W --> K

    U --> X[Transformers]
    X --> Y[CUDA/GPU]
```

## Key Components

### Frontend (somethingaiiot/)
- **Framework**: React 18 with Vite
- **Routing**: React Router
- **Styling**: Tailwind CSS with custom components
- **State Management**: React Context (Theme)
- **UI Library**: Custom components with animations

### Unified Backend (backend/)
- **Framework**: FastAPI
- **AI Model**: Microsoft Phi-2 (via Transformers)
- **Dataset**: Open Schematics from HuggingFace
- **Features**: Authentication, dashboard data, device simulation, AI code generation
- **Database**: JSON file persistence

## Data Flow

1. User interacts with React frontend
2. Frontend calls unified backend API
3. Backend handles authentication, AI code generation, device simulation
4. Phi-2 model generates IoT code with dataset context
5. Results displayed in frontend with real-time updates
6. User data persisted to JSON files

## Dependencies

### Python Backends
- fastapi
- pydantic
- uvicorn
- torch
- transformers
- requests
- passlib[bcrypt]

### Frontend
- react
- react-dom
- react-router-dom
- tailwindcss
- lucide-react
- @theme-toggles/react
- react-theme-switch-animation
- @monaco-editor/react
- clsx
- tailwind-merge

## File Structure

```
ai iot mvp/
├── backend/           # Unified FastAPI backend
│   ├── main.py        # FastAPI app with all routes
│   ├── auth.py        # Authentication with bcrypt
│   ├── dashboard.py   # Dashboard data
│   ├── device.py      # Device simulation
│   ├── ai.py          # AI code generation
│   ├── models.py      # Pydantic models
│   ├── database.py    # Persistent JSON database
│   ├── model.py       # Phi-2 model loading/generation
│   ├── prompt.py      # Prompt building with dataset
│   ├── dataset.py     # HuggingFace dataset fetching
│   ├── requirements.txt
│   └── test_backend.py
├── somethingaiiot/    # React frontend
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── components/
│   │   │   ├── Layout.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Landing/
│   │   │   │   ├── HeroSection.jsx
│   │   │   │   └── Features.jsx
│   │   │   └── ui/     # Custom UI components
│   │   ├── pages/     # Route components
│   │   ├── contexts/  # React contexts
│   │   └── lib/       # Utilities
│   └── package.json
└── plans/             # Documentation
    └── structure.md
