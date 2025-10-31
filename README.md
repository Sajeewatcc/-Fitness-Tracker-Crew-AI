# FitnessTrackerCrew Crew

Welcome to the FitnessTrackerCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/fitness_tracker_crew/config/agents.yaml` to define your agents
- Modify `src/fitness_tracker_crew/config/tasks.yaml` to define your tasks
- Modify `src/fitness_tracker_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/fitness_tracker_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the fitness_tracker_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The fitness_tracker_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

# 🏋️‍♂️ Fitness Tracker Crew AI 🤖💪  
A comprehensive AI-powered fitness workout tracking system built with **CrewAI**, featuring multiple specialized agents working together to create a complete fitness application.

---

![CrewAI](https://img.shields.io/badge/CrewAI-Project-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Fitness](https://img.shields.io/badge/Fitness-Tracking-orange)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Agents](#-agents)
- [Output](#-output)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview
**Fitness Tracker Crew AI** demonstrates the power of multi-agent AI systems using **CrewAI**.  
The project coordinates multiple specialized AI agents to design, develop, and document a complete fitness workout tracking application from scratch.

---

## ✨ Features

### 🏋️ Exercise Management
- Pre-loaded exercise database with **50+ exercises**  
- Categorized exercises (Strength, Cardio, Flexibility)  
- Custom exercise creation  
- Exercise search and filtering  

### 📊 Workout Logging
- Comprehensive workout tracking with **sets, reps, and weights**  
- Support for different exercise types  
- **RPE (Rate of Perceived Exertion)** tracking  
- Workout templates and routines  

### 📈 Advanced Analytics
- **1RM (One Rep Max)** estimation  
- Training volume calculations  
- Progress tracking and visualization  
- Performance insights and trends  

### 🎯 Goal Tracking
- Personal goal setting  
- Progress monitoring  
- Achievement tracking  
- Milestone celebrations  


