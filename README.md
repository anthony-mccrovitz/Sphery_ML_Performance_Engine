# 🎯 Sphery Motivational Engine

A production-ready machine learning system that analyzes player performance data from the Sphery/Execube gaming platform to provide personalized motivational targets and increase user retention.

## 🚀 Project Overview

The Sphery Motivational Engine uses Gaussian Mixture Models (GMM) to segment players into performance clusters and provide personalized percentile-based targets. This system is designed to be integrated into the main Sphery application to drive user engagement and retention.

## 📊 Key Features

- **Player Segmentation**: GMM-based clustering to identify performance levels
- **Personalized Targets**: Percentile-based goals tailored to each player's cluster
- **Motivational Messages**: Dynamic, encouraging feedback based on performance
- **Production Ready**: Clean, documented code ready for live database integration
- **Interactive Dashboard**: Streamlit interface for testing and demonstration

## 🏗️ Architecture

```
Sphery_ML_Model/
├── notebooks/                    # Jupyter notebooks for analysis
│   ├── gmm_training_complete.ipynb  # Complete GMM training
│   ├── game_modes_analysis.ipynb    # Game mode exploration
│   └── model_training.ipynb         # Initial model setup
├── src/                         # Production code
│   ├── motivational_engine.py   # Core ML engine
│   └── dashboard_motivational_engine.py  # Streamlit dashboard
├── models/                      # Trained models and metadata
├── scripts/                     # Utility scripts
├── plots/                       # Generated visualizations
└── requirements.txt             # Dependencies
```

## 🎮 Current Model Configuration

- **Game Mode**: DualFlow
- **Difficulty**: -1 (Expert)
- **Duration**: 10 minutes
- **Training Data**: 945 player records
- **Clusters**: 4 performance levels
- **Features**: Score, Age, Start Speed, Duration

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv sphery_env
source sphery_env/bin/activate  # On Windows: sphery_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Train the Model

```bash
# Run the complete GMM training notebook
jupyter notebook notebooks/gmm_training_complete.ipynb
```

### 3. Test the Dashboard

```bash
# Launch the Streamlit dashboard
streamlit run src/dashboard_motivational_engine.py
```

### 4. Use the Engine

```python
from src.motivational_engine import load_engine

# Load the engine
engine = load_engine()

# Analyze a player
player_data = {
    'score': 150000,
    'age': 25.5,
    'startSpeed': 5.0,
    'duration_minutes': 10.0
}

analysis = engine.analyze_player_performance(player_data)
print(f"Cluster: {analysis['cluster_prediction']['cluster_label']}")
print(f"Message: {analysis['motivational_message']['message']}")
```

## 📈 Model Performance

The GMM model segments players into 4 performance clusters:

| Cluster | Description | Target Range |
|---------|-------------|--------------|
| 0 | Beginner | 25th-50th percentile |
| 1 | Intermediate | 50th-75th percentile |
| 2 | Advanced | 75th-90th percentile |
| 3 | Expert | 90th-95th percentile |

Each cluster has specific percentile targets for personalized motivation.

## 🔧 API Reference

### MotivationalEngine Class

```python
class MotivationalEngine:
    def __init__(self, model_path: str)
    def predict_player_cluster(self, player_data: Dict) -> Dict
    def get_performance_targets(self, cluster: int) -> Dict
    def get_motivational_message(self, player_score: int, cluster: int) -> Dict
    def analyze_player_performance(self, player_data: Dict) -> Dict
    def get_model_info(self) -> Dict
```

### Key Methods

- `analyze_player_performance()`: Complete analysis with cluster prediction and motivational message
- `get_performance_targets()`: Get percentile targets for a specific cluster
- `get_motivational_message()`: Generate personalized motivational feedback

## 🎯 Integration Guide

### Database Integration

The engine is designed to work with the Sphery database schema:

```sql
-- Key tables for integration
Workouts (score, userId, completedWorkout)
RaceConfigs (difficulty, workoutId, duration)
Users (id, username)
HealthData (dob, weight, height, userId)
```

### Live Application Integration

```python
# Example integration code
def get_player_motivation(user_id, game_mode, difficulty, duration):
    # Fetch player data from database
    player_data = fetch_player_data(user_id, game_mode, difficulty, duration)
    
    # Analyze with motivational engine
    engine = load_engine()
    analysis = engine.analyze_player_performance(player_data)
    
    return {
        'cluster': analysis['cluster_prediction']['cluster_label'],
        'message': analysis['motivational_message']['message'],
        'next_target': analysis['motivational_message']['next_target']
    }
```

## 📊 Dashboard Features

The Streamlit dashboard provides:

- **Player Analysis**: Interactive input for testing individual players
- **Model Information**: Detailed model statistics and configuration
- **Batch Testing**: Upload CSV files for bulk analysis
- **Visualizations**: Performance targets and cluster distributions

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Test the engine directly
python src/motivational_engine.py
```

## 📝 Development Workflow

1. **Data Analysis**: Use notebooks in `notebooks/` for exploration
2. **Model Training**: Complete training in `gmm_training_complete.ipynb`
3. **Production Code**: Develop in `src/` with proper documentation
4. **Testing**: Use dashboard for interactive testing
5. **Integration**: Deploy to live database

## 🎯 Next Steps (2-Week Plan)

### Week 1: Core Completion
- [x] Complete GMM training
- [x] Create production engine
- [x] Build Streamlit dashboard
- [ ] Test with live database connection
- [ ] Validate model performance

### Week 2: Integration & Deployment
- [ ] Create database integration functions
- [ ] Build API endpoints
- [ ] Implement real-time predictions
- [ ] Add monitoring and logging
- [ ] Deploy to staging environment

## 🔍 Model Validation

The model has been validated on:
- **Data Quality**: 945 clean records from DualFlow mode
- **Feature Engineering**: Age calculation, duration normalization
- **Cluster Analysis**: 4 distinct performance levels identified
- **Target Accuracy**: Percentile-based targets for each cluster

## 📊 Performance Metrics

- **Model Convergence**: ✅ GMM converged successfully
- **Cluster Quality**: 4 distinct performance clusters identified
- **Target Coverage**: 25th, 50th, 75th, 90th, 95th percentiles
- **Confidence Levels**: High confidence cluster assignments

## 🤝 Contributing

1. Follow the coding standards in the project rules
2. Use type hints and comprehensive docstrings
3. Test all new functionality
4. Update documentation as needed

## 📄 License

This project is proprietary to Sphery/Execube.

## 👨‍💻 Author

Anthony McCrovitz - Machine Learning Engineer

---

**Status**: Production-ready motivational engine with 2-week deployment timeline 