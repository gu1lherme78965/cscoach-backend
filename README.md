# CSCoach Backend

Backend engine for **CSCoach**, a Counter-Strike performance analysis and coaching platform.

CSCoach aims to transform match data into actionable improvement insights by analyzing gameplay patterns, decision making, mechanics, and tactical performance.

## Vision

CSCoach is built around the idea that every match can become a training session.

The system will eventually:

- Parse Counter-Strike demos
- Extract gameplay events
- Analyze player performance
- Identify strengths and weaknesses
- Generate personalized coaching recommendations
- Track player progression over time

## Architecture

The backend is designed as a modular system with clear separation of responsibilities:

```text
cscoach-backend

├── domain          # Core Counter-Strike concepts
├── application     # Use cases and business logic
├── infrastructure  # External systems (database, parsers, APIs)
├── analytics       # Performance analysis
├── coaching        # Recommendations and improvement plans
└── api             # HTTP interface
```

## Tech Stack

### Current

- Python 3.14+
- FastAPI
- Pydantic

### Planned

- PostgreSQL
- SQLAlchemy
- Counter-Strike demo parsing
- Machine Learning models
- AI-powered coaching system

## Development Setup

### Clone the repository

```bash
git clone <repository-url>
cd cscoach-backend
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -e .
```

### Run the application

```bash
python -m app.main
```

## Project Structure

```text
cscoach-backend/

├── app/
│   ├── api/              # API endpoints
│   ├── application/      # Application logic and use cases
│   ├── domain/           # Core business concepts
│   ├── infrastructure/   # External integrations
│   ├── analytics/        # Performance analysis systems
│   ├── coaching/         # Coaching and recommendations
│   └── ml/               # Machine learning components
│
├── tests/                # Automated tests
├── data/                 # Local development data
├── pyproject.toml        # Project configuration
├── README.md             # Project documentation
└── .gitignore
```

## Development Roadmap

### Phase 1 — Domain Foundation

- Create core Counter-Strike entities
- Define game events
- Model matches and rounds
- Establish the internal game representation

### Phase 2 — Demo Analysis

- Parse Counter-Strike demos
- Extract gameplay events
- Convert raw data into domain objects

### Phase 3 — Analytics Engine

- Calculate player statistics
- Analyze positioning
- Analyze utility usage
- Analyze decision making
- Identify gameplay patterns

### Phase 4 — Coaching System

- Create rule-based recommendations
- Generate personalized improvement plans
- Track player progression

### Phase 5 — AI Coaching

- Build player performance models
- Predict weaknesses and improvement areas
- Create an AI coaching assistant

## Project Status

Currently in early development.

The first milestone is building a reliable foundation for representing and analyzing Counter-Strike gameplay data.

The long-term goal is to create a complete coaching framework that helps players understand their game and improve systematically.