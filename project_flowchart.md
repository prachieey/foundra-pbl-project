# Project Flowchart Diagram

## Overall Architecture

```mermaid
graph TB
    subgraph "Project Root"
        PBL[pbl/]
    end
    
    subgraph "HappySense Application"
        HS[happysense/]
        subgraph "Backend API"
            BE[backend/]
            APP[app.py - Flask Server]
            MODEL[model.py - Pathfinding Logic]
            DATA[Data Files]
        end
        
        subgraph "Foundra Frontend"
            FD[foundra/]
            FDAPP[App.jsx - React App]
        end
    end
    
    subgraph "Main Frontend"
        FE[frontend/]
        MAINAPP[App.jsx - Main React App]
        COMP[Components/]
    end
    
    PBL --> HS
    PBL --> FE
    HS --> BE
    HS --> FD
    FE --> MAINAPP
    MAINAPP --> COMP
    BE --> APP
    BE --> MODEL
    MODEL --> DATA
    FD --> FDAPP
```

## Data Flow Architecture

```mermaid
flowchart LR
    subgraph "Data Sources"
        CSV[profiles.csv<br/>Company Profiles]
        NPY[embeddings.npy<br/>Vector Embeddings]
        PKL[graph.pkl<br/>Network Graph]
    end
    
    subgraph "Backend Processing"
        LOAD[load_assets()<br/>Initialize Data]
        FIND[find_path()<br/>Shortest Path Algorithm]
    end
    
    subgraph "API Layer"
        FLASK[Flask App]
        ROUTE[/find-path POST]
    end
    
    subgraph "Frontend Applications"
        HAPPY[HappySense Frontend]
        FOUNDRA[Foundra App]
        MAIN[Main Frontend]
    end
    
    CSV --> LOAD
    NPY --> LOAD
    PKL --> LOAD
    LOAD --> FIND
    FIND --> FLASK
    FLASK --> ROUTE
    ROUTE --> HAPPY
    ROUTE --> FOUNDRA
    ROUTE --> MAIN
```

## Application Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Data
    
    User->>Frontend: Select Source & Target
    Frontend->>Backend: POST /find-path {source_idx, target_idx}
    Backend->>Data: Load graph, embeddings, profiles
    Backend->>Backend: Calculate shortest path using NetworkX
    Backend->>Backend: Format result with company/title info
    Backend->>Frontend: Return path data
    Frontend->>User: Display connection path
```

## Component Architecture

### HappySense Backend
- **Flask Server** (`app.py`)
  - Health check endpoint: `/`
  - Path finding endpoint: `/find-path` (POST)
- **Pathfinding Engine** (`model.py`)
  - Data loading from files
  - NetworkX shortest path algorithm
  - Result formatting with profile data

### Frontend Applications
1. **Main Frontend** (`frontend/`)
   - React + Vite
   - Clerk authentication
   - Multiple pages (Home, Dashboard, Pricing, etc.)
   - TailwindCSS styling

2. **Foundra** (`happysense/foundra/`)
   - Simple React app
   - Basic Vite setup

## Technology Stack

```mermaid
graph TB
    subgraph "Backend"
        PYTHON[Python]
        FLASK[Flask]
        NUMPY[NumPy]
        PANDAS[Pandas]
        NETWORKX[NetworkX]
    end
    
    subgraph "Frontend"
        REACT[React 19]
        VITE[Vite]
        TAILWIND[TailwindCSS]
        CLERK[Clerk Auth]
        FRAMER[Framer Motion]
        LUCIDE[Lucide Icons]
    end
    
    subgraph "Data"
        CSV[CSV Files]
        NPY[NumPy Arrays]
        PICKLE[Pickle Files]
    end
    
    PYTHON --> FLASK
    FLASK --> NUMPY
    FLASK --> PANDAS
    FLASK --> NETWORKX
    
    REACT --> VITE
    REACT --> TAILWIND
    REACT --> CLERK
    REACT --> FRAMER
    REACT --> LUCIDE
    
    NUMPY --> NPY
    PANDAS --> CSV
    NETWORKX --> PICKLE
```

## Key Features Flow

```mermaid
flowchart TD
    START[User Access] --> AUTH{Authenticated?}
    AUTH -->|No| LANDING[Landing Page]
    AUTH -->|Yes| DASHBOARD[Dashboard]
    
    LANDING --> FEATURES[Feature Pages]
    FEATURES --> CONTACT[Contact/Pricing/Careers]
    
    DASHBOARD --> PATH[Path Finding Interface]
    PATH --> SELECT[Select Source/Target]
    SELECT --> CALCULATE[Calculate Connection Path]
    CALCULATE --> DISPLAY[Display Results]
    
    DISPLAY --> PATH
```

## Deployment Architecture

```mermaid
graph LR
    subgraph "Development"
        DEV_FRONTEND[Frontend Dev Server<br/>:5173]
        DEV_BACKEND[Backend Dev Server<br/>:5000]
    end
    
    subgraph "Production"
        PROD_FRONTEND[Built Frontend]
        PROD_BACKEND[Production Backend]
    end
    
    DEV_FRONTEND --> DEV_BACKEND
    PROD_FRONTEND --> PROD_BACKEND
```

This flowchart illustrates a network-based connection finding application with multiple frontend interfaces, a Python Flask backend for pathfinding algorithms, and data storage in various formats (CSV, NumPy arrays, and Pickle files).
